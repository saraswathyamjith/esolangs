# Esolangs Benchmarking with AI Models

This repository evaluates the performance of various AI models on benchmarks for coding in esolangs (esoteric programming languages) , including **Minipy**, **Pyth**, **Janus**, and **0815** using datasets like the HumanEval benchmark and a custom created problem set encompassing 30 of the most basic, simple programs, named, EsoEval.

This repository also provides the documentation and examples that were fed in during in-context learning. 

---

## Benchmarks Overview

### Minipy
A shortened version of Python used as an esolang for benchmarking. Due to relatively high accuracy on HumanEval, we did not test on the EsoEval collection of simple problems.  

- **`MiniPyHumanEval.py`**  
  Evaluates **OpenAI's gpt-4o-mini** for code generation in Minipy on the HumanEval benchmark.  
  - **Accuracy**: 66.67%
  - **Non executable by Python + Passed**: 0.0%  
  - **Subset**: 30 problems

- **`MiniPyLLAMAHumanEval.py`**  
  Evaluates **Meta's meta-llama/Llama-3.3-70B-Instruct-Turbo** for code generation in Minipy on the HumanEval benchmark.  
  - **Accuracy**: 66.67%
  - **Non executable by Python + Passed**: 10.0%  
  - **Subset**: 30 problems

- **`MiniPyDeepSeekHumanEval.py`**  
  Evaluates **Meta's meta-llama/Llama-3.3-70B-Instruct-Turbo** for code generation in Minipy on the HumanEval benchmark.  
  - **Accuracy**: 66.67%
  - **Non executable by Python + Passed**: 10.0%  
  - **Subset**: 30 problems

### 0815
0815 is an esolang based around a queue and 3 registers. It only understands hexadecimal, so every numeric input and output is in hexadecimal. Everything that is not an instruction is a comment. 0815 has been tested on two benchmarks, both HumanEval and our own EsoEval (collection of simple problems).

- **`0815HumanEval.py`**  
  Evaluates **OpenAI's gpt-4o-mini** for code generation in 0815 on the HumanEval benchmark with a two-shot approach.  
  - **Accuracy**: 0.0%
  - **Subset**: 10 problems

- **`0815EsoEval.py`**  
  Evaluates **OpenAI's gpt-4o-mini** for code generation in 0815 on a simplistic problem set of basic Python problems.  
  - **Accuracy**: 26.67%
  - **Subset**: 30 problems

- **`0815LLAMAEsoEval.py`**  
  Evaluates **Meta's meta-llama/Llama-3.3-70B-Instruct-Turbo** for code generation in 0815 on the same simplistic problem set.  
  - **Accuracy**: 0.00%  
  - **Subset**: 30 problems

Interestingly, the LLAMA models are much better at coding in Pyth or Minipy than they are at 0815...

### Pyth
A concise esolang inspired by Python tested on two benchmarks, both HumanEval and our own EsoEval (collection of simple problems).

- **`PythHumanEval.py`**  
  Evaluates **OpenAI's gpt-4o-mini** for code generation in Pyth on the HumanEval benchmark with a two-shot approach.  
  - **Accuracy**: 0.0%  
  - **Subset**: 10 problems

- **`PythEsoEval.py`**  
  Evaluates **OpenAI's gpt-4o-mini** for code generation in Pyth on a simplistic problem set of basic Python problems.  
  - **Accuracy**: 10.00%  
  - **Subset**: 30 problems

- **`PythLLAMAEsoEval.py`**  
  Evaluates **Meta's meta-llama/Llama-3.3-70B-Instruct-Turbo** for code generation in Pyth on the same simplistic problem set.  
  - **Accuracy**: 20.00%  
  - **Subset**: 30 problems

### Janus
A reversible programming language. Since the 0.00% accuracy via OpenAI's gpt-4o-mini was alarming and raised red flags, the researcher also manually pasted in generated code to https://topps.diku.dk/pirc/?id=janusP, where it also failed to compile with the same errors for a subset of 5 problems. 

- **`JanusEsoEval.py`**  
  Evaluates **OpenAI's gpt-4o-mini** for code generation in Pyth on a simplistic problem set of basic Python problems.  
  - **Accuracy**: 0.00%  
  - **Subset**: 30 problems

- **`JanusLLAMAEsoEval.py`**  
  Evaluates **Meta's meta-llama/Llama-3.3-70B-Instruct-Turbo** for code generation in Pyth on the same simplistic problem set.  
  - **Accuracy**: 0.00%  
  - **Subset**: 30 problems

---

## EsoEval: Simple Problems for Pyth, 0815, and Janus Benchmarks

Below is the problem set used for evaluating esolangs that are more divergent from standard languages. The problem set was tested via OPENAI's gpt-4o-mini which achieved a 93.33% accuracy in Python. Since it achieved such high accuracy, these problems are able to be labeled as a standard, simple benchmark. 

1. Print "hello world".
2. Given a number `n` as input, return the `n`th factorial number.
3. Given a number `n`, return `"Even"` if `n` is even, else `"Odd"`.
4. Given two numbers `a` and `b`, return their sum.
5. Given a number `n`, return `True` if it is prime, else `False`.
6. Given a string `s`, return the reversed string.
7. Print "Hello, Pyth!".
8. Given two numbers `a` and `b`, return their product.
9. Given a number `n`, return `True` if it is positive, else `False`.
10. Given two strings `s1` and `s2`, return their concatenation.
11. Given a number `n`, return its square.
12. Given a string `s`, return the number of characters in the string.
13. Given two numbers `a` and `b`, return the smaller number.
14. Given a string `s`, return `True` if all characters in the string are vowels, else `False`.
15. Given two numbers `a` and `b`, return the absolute difference between them.
16. Given a string `s` and a number `n`, return the string repeated `n` times.
17. Given a number `n`, return the Fibonacci sequence up to the nth term.
18. Given a list of numbers, return the maximum number.
19. Given a string `s` , return True if it is a palindrome, else False.
20. Given two numbers `a` and `b`, return their greatest common divisor.
21. Given a list of numbers, return the list sorted in ascending order.
22. Given a number `n`, return True if it is a perfect square, else False.
23. Given a string  `s` , return the number of vowels in the string.
24. Given a list of numbers, return the sum of all numbers in the list.
25. Given a number `n`,, return its binary representation as a string.
26. Given two strings `s1` and `s2`, return True if s1 is an anagram of s2, else False.
27. Given a number `n`, return the sum of digits in n.
28. Given a list of numbers, return True if all numbers are even, else False.
29. Given a string `s`, return the string in title case.
30. Given two numbers  `a` and `b`, return True if a is divisible by b, else False.
    
