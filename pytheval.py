# -*- coding: utf-8 -*-
"""pytheval.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cjxXvuqUFA6c5eOsq9Ana_LJ8HhIIm0P
"""

!git clone https://github.com/isaacg1/pyth.git

!pip install pymupdf

import fitz

from google.colab import drive
drive.mount('/content/drive')

pdf_path = ['/content/drive/MyDrive/10. The Language Specification - Comparisons — Pyth 1.0 documentation.pdf',
            '/content/drive/MyDrive/11. The Language Specification - Sequences — Pyth 1.0 documentation.pdf',
            '/content/drive/MyDrive/2. More Details About Pyth — Pyth 1.0 documentation.pdf',
            '/content/drive/MyDrive/3. Some Simple Programs — Pyth 1.0 documentation.pdf',
            '/content/drive/MyDrive/4. Some Simple Programs - Part II — Pyth 1.0 documentation.pdf',
            '/content/drive/MyDrive/5. Learning More - Documentation and Errors — Pyth 1.0 documentation.pdf',
            '/content/drive/MyDrive/6. Adding to Pyth — Pyth 1.0 documentation.pdf',
            '/content/drive/MyDrive/7. The Language Specification - Variables — Pyth 1.0 documentation.pdf',
            '/content/drive/MyDrive/8. The Language Specification - Control Flow — Pyth 1.0 documentation.pdf',
            '/content/drive/MyDrive/9. The Language Specification - Arithmetic — Pyth 1.0 documentation.pdf']

text_content = ""

for path in pdf_path:
  with fitz.open(path) as pdf:
      for page_num in range(len(pdf)):
          page = pdf[page_num]
          text_content += page.get_text()

print("Sample extracted text:\n", text_content[:100])

import openai
import os
import os
import subprocess
import re
from openai import OpenAI

# Uncomment the line below and replace 'your-api-key' with your actual API key
os.environ["OPENAI_API_KEY"] = 'your-api-key'
results = []
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Prompt engineered prompt
def mod_prompt(prompt):
   modified_prompt = (
        f"Write a function in Pyth, an esoteric programming language."
        f"The function should perform the following: {prompt}"
        f"The documentation for Pyth is provided here: '{text_content}'. "

    )
   return modified_prompt

# Commented out IPython magic to ensure Python compatibility.
# collects human eval problems from github
!git clone https://github.com/openai/human-eval.git
# %cd human-eval
!ls data
!gunzip data/HumanEval.jsonl.gz
!ls data
!pip install transformers torch jsonlines
import jsonlines

problems = []

# Load the problems from the JSONL file
with jsonlines.open("data/HumanEval.jsonl") as f:
    for obj in f:
        problems.append(obj)

# Path to your local Pyth interpreter. Adjust if needed:
PYTH_INTERPRETER_PATH = "/content/pyth/pyth.py"

def execute_pyth_function(code: str, input_data: Any = "") -> str:
    """
    Executes Pyth code with the given input and returns the output or a concise error message.
    """
    try:
        if not os.path.isfile(PYTH_INTERPRETER_PATH):
            return f"Error: Pyth interpreter not found at {PYTH_INTERPRETER_PATH}."

        temp_pyth_path = "temp.pyth"
        with open(temp_pyth_path, "w") as f:
            f.write(code)

        # Convert input_data to string, ensuring it's properly formatted for Pyth
        input_str = str(input_data)

        result = subprocess.run(
            ["python3", PYTH_INTERPRETER_PATH, temp_pyth_path],
            input=input_str,
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode != 0:
            error_message = result.stderr.strip().split('\n')[-1]
            return f"Error: {error_message}"

        return result.stdout.strip()

    except subprocess.TimeoutExpired:
        return "Error: Execution timed out."
    except Exception as e:
        return f"Error during execution: {str(e)}"

def extract_pyth_code(generated_content: str) -> str:
    """
    Extracts Pyth code enclosed within ```pyth ... ``` blocks.
    """
    pattern = r"```pyth\s+([\s\S]*?)```"
    pyth_codes = re.findall(pattern, generated_content, re.MULTILINE)
    if pyth_codes:
        return pyth_codes[0].strip()
    else:
        lines = generated_content.splitlines()
        code_lines = []
        capture = False
        for line in lines:
            if line.strip().startswith("```pyth"):
                capture = True
                continue
            if line.strip().startswith("```") and capture:
                break
            if capture:
                code_lines.append(line)
        return "\n".join(code_lines).strip()

def parse_test_cases(test_str: str) -> List[Tuple[Any, Any]]:
    """
    Parses a string containing Python assert statements to extract test cases.
    Returns a list of tuples: (input_args, expected_output).
    """
    test_cases = []

    # Patterns for different assert types
    pattern_eq = re.compile(
        r'assert\s+candidate\((.*?)\)\s*==\s*('
        r'\[.*?\]|True|False|None|".*?"|\'.*?\'|[-+]?\d*\.\d+|\d+'
        r')',
        re.DOTALL
    )
    pattern_approx_eq = re.compile(
        r'assert\s+abs\s*\(\s*candidate\((.*?)\)\s*-\s*(.*?)\s*\)\s*<\s*('
        r'[-+]?\d*\.\d+|\d+'
        r')',
        re.DOTALL
    )

    # Extract direct equality test cases
    for args_str, expected_str in pattern_eq.findall(test_str):
        try:
            input_args = ast.literal_eval(args_str.strip())
            expected_output = ast.literal_eval(expected_str.strip())
            test_cases.append((input_args, expected_output))
        except Exception as e:
            print(f"Error parsing direct equality test case: {e}")

    # Extract approximate equality test cases
    for args_str, expected_str, tolerance_str in pattern_approx_eq.findall(test_str):
        try:
            input_args = ast.literal_eval(args_str.strip())
            expected_output = ast.literal_eval(expected_str.strip())
            # Tolerance is currently not used; can be implemented if needed
            test_cases.append((input_args, expected_output))
        except Exception as e:
            print(f"Error parsing approximate equality test case: {e}")

    return test_cases

def mod_prompt(prompt: str, feedback: str = "") -> str:
    """
    Modifies the prompt by including feedback from previous attempts.
    """
    if feedback:
        modified_prompt = (
            f"Write a function in Pyth, an esoteric programming language. "
            f"The function should perform the following: {prompt} "
            f"The documentation for Pyth is provided here: '{text_content}'. "
            f"Here is the feedback from the previous attempt: {feedback}"
        )
    else:
        modified_prompt = (
            f"Write a function in Pyth, an esoteric programming language. "
            f"The function should perform the following: {prompt} "
            f"The documentation for Pyth is provided here: '{text_content}'. "
        )
    return modified_prompt

##############################################################################
# Evaluation Loop with Retry for 2-shotting purposes

results = []
max_retries = 2  # Maximum number of attempts per problem

for idx, problem in enumerate(problems[:10]):
    print(f"\nEvaluating Problem {idx+1}/{len(problems)}: {problem['task_id']}")
    attempt = 0
    success = False
    feedback = ""

    while attempt < max_retries and not success:
        print(f"Attempt {attempt + 1} for Problem {problem['task_id']}")

        try:
            # Generate Pyth code using OpenAI API
            response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages = [
    {
        "role": "system",
        "content": (
            f"You are an assistant that writes Pyth, the esolang, code. "
            f"The documentation for Pyth {text_content} is provided here. "
        ),
    },
    {
        "role": "user",
        "content": mod_prompt(problem['prompt']),
    }
],
            temperature=0.0,  # Lower temperature for deterministic output
            max_tokens=500  # Adjust based on expected code length
        )
            generated_content = response.choices[0].message.content.strip()
            print(f"Generated Content:\n{generated_content[:500]}...\n")

            # Extract Pyth code from the generated content
            pyth_code = extract_pyth_code(generated_content)
            print(f"Extracted Pyth Code:\n{pyth_code}\n")

            if not pyth_code:
                raise ValueError("No Pyth code found in the response.")

            # Parse test cases
            parsed_test_cases = parse_test_cases(problem['test'])
            print(f"Parsed Test Cases: {parsed_test_cases}\n")

            # Initialize pass status
            all_pass = True
            failed_tests = []

            # Execute and evaluate each test case
            for test_idx, (inputs, expected) in enumerate(parsed_test_cases, start=1):
                output = execute_pyth_function(pyth_code, inputs)

                # Limit the output printed to prevent long error messages
                if output.startswith("Error:"):
                    display_output = output  # Short error message
                else:
                    display_output = output[:20] + "..." if len(output) > 20 else output  # Truncate long outputs

                print(f"Test {test_idx}: Input: {inputs}, Expected: {expected}, Output: {display_output}")

                pass_test = (str(expected) in output)
                if not pass_test:
                    all_pass = False
                    failed_tests.append({
                        "test_idx": test_idx,
                        "input": inputs,
                        "expected": expected,
                        "output": output
                    })
                print(f"Pass: {pass_test}\n")

            if all_pass:
                print(f"Problem {problem['task_id']} passed all test cases.")
                results.append({
                    "problem": problem["task_id"],
                    "status": "Passed",
                    "attempts": attempt + 1
                })
                success = True
            else:
                print(f"Problem {problem['task_id']} failed some test cases.")

                failed_test_descriptions = [
                    f"Test {ft['test_idx']}: Expected {ft['expected']}, Got {ft['output']}"
                    for ft in failed_tests
                ]
                feedback = f"The following test cases failed: {'; '.join(failed_test_descriptions)}"
                attempt += 1

        except Exception as e:
            print(f"Error during evaluation: {e}")
            feedback = f"Encountered an error: {e}"
            attempt += 1

    if not success:
        print(f"Problem {problem['task_id']} failed after {max_retries} attempts.")
        results.append({
            "problem": problem["task_id"],
            "status": "Failed",
            "attempts": attempt
        })

print("\nFinal Results:")
totalpassed = 0
for res in results:
    print(f"Problem: {res['problem']}, Status: {res['status']}, Attempts: {res['attempts']}")
    if res['status'] == True:
         totalpassed += 1

print("percentage passed: " + str(100*totalpassed/ len(results)) + "%")