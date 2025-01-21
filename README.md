# Esolangs Benchmarking with AI Models

This repository evaluates the performance of various AI models on esolangs (esoteric programming languages) benchmarks, including **Minipy** and **Pyth**, using datasets like the HumanEval benchmark and custom problem sets.

---

## Benchmarks Overview

### Minipy
A shortened version of Python used as an esolang for benchmarking.

- **`Minipyeval.py`**  
  Evaluates **OpenAI's gpt-4o-mini** for code generation in Minipy on the HumanEval benchmark.  
  - **Accuracy**: 80.0%  
  - **Subset**: 30 problems

- **`LLAMAminieval.py`**  
  Evaluates **Meta's meta-llama/Llama-3.3-70B-Instruct-Turbo** for code generation in Minipy on the HumanEval benchmark.  
  - **Accuracy**: 76.67%  
  - **Subset**: 30 problems

### Pyth
A concise esolang inspired by Python, tested on two benchmarks:

- **`Pytheval.py`**  
  Evaluates **OpenAI's gpt-4o-mini** for code generation in Pyth on the HumanEval benchmark.  
  - **Accuracy**: 0.0%  
  - **Subset**: 10 problems

- **`Pythsimple.py`**  
  Evaluates **OpenAI's gpt-4o-mini** for code generation in Pyth on a simplistic problem set of basic Python problems.  
  - **Accuracy**: 12.50%  
  - **Subset**: 16 problems

- **`LLAMApythsimple.py`**  
  Evaluates **Meta's meta-llama/Llama-3.3-70B-Instruct-Turbo** for code generation in Pyth on the same simplistic problem set.  
  - **Accuracy**: 18.75%  
  - **Subset**: 16 problems

---

## Simple Problems for Pyth Benchmarks

Below is the problem set used for **Pythsimple.py** and **LLAMApythsimple.py**:

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

---

## Repository Structure

