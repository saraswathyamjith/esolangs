p("hello world")

# factorial:

fac = lambda n: fr(lambda x, y: x * y, r(1, n + 1)) if n > 0 else 1

# add two numbers:

s = lambda a, b: sm([a, b])

# checks if a given number `n` is prime
def is_prime(n):
    if n < 2:
        return False
    for i in r(2, int(m.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# reverse a string:

rs = lambda s: sr.join(rvr(s))

# prints "Hello, Pyth!"
p("Hello, Pyth!")

# length of string
def char_count(s):
    return l(s)

# checks if all characters in a string are vowels
def all_vowels(s):
    return al(c in "aeiouAEIOU" for c in s)

# calculates the absolute difference between two numbers `a` and `b
d = lambda a, b: ab(a - b)

# generates the Fibonacci sequence up to the nth term
def fib(n):
    a, b = 0, 1
    seq = []
    for _ in r(n):
        seq.append(a)
        a, b = b, a + b
    return seq

# returns the maximum number from a given list of numbers
mx = lambda lst: fr(lambda x, y: x if x > y else y, lst)

# sorts a list of numbers in ascending order:
srt_ls = lambda ls_nums: srt(ls_nums)

# checks if a given number `n` is a perfect square:
psq = lambda n: (m.isqrt(n) ** 2) == n

# counts the number of vowels in a given string `s
def count_vowels(s):
    return l(ff(lambda x: x in "aeiouAEIOU", s))

# returns the sum of all numbers in a given list
sml = lambda lst: sm(lst)

#  takes a number `n` and returns its binary representation as a string
def bin_str(n):
    return bn(n)[2:]

# checks if two strings are anagrams
def anagram(s1, s2):
    return srt(s(s1)) == srt(s(s2))

# calculates the sum of the digits of a given number `n`
def sum_digits(n):
    return sm(t(c) for c in s(n))

# checks if all numbers in a given list are even
def all_even(nums):
    return al(n % 2 == 0 for n in nums)

# prints hello world
p(tc("hello world"))
