# Python Algorithm Practice – CSCI 3412 (PA2)

This assignment includes five Python programs that explore algorithmic thinking and Python programming fundamentals. Topics covered include binary search, time efficiency analysis, brute-force vs. random guessing strategies, Collatz conjecture, and decorators.


---

## Q1: Binary Search Number Guessing Game

Write a program that generates a random integer within a given range (e.g., 1–1,000 and 1–1,000,000), and uses the binary search algorithm to guess that number automatically. The goal is to simulate this process multiple times (10,000+) and compute the average number of guesses it takes to find the correct number.

---

## Q2: Custom Time Efficiency Function

Implement a timing function called `timeEfficiency()` that takes another function and its arguments as input, runs it, and prints the start time, end time, and total runtime. Then write a second function, `listPrimeNumbers()`, to generate all prime numbers up to a user-specified limit, and test it using the `timeEfficiency()` function.

---

## Q3: Brute Force vs. Pure Random Guessing Game

Create a program that randomly generates three digits (0–9) where the order matters. Write two guessing algorithms:
- **Brute-force approach**: Systematically permutes all possible 3-digit combinations without repeats.
- **Pure random approach**: Randomly guesses 3-digit combinations with no memory of past guesses.
Simulate each method multiple times and compare the number of guesses it takes to correctly guess the digits.

---

## Q4: Collatz Conjecture Exploration

Write a program to explore the Collatz 3n + 1 conjecture. For every number from 1 to 10,000,000, calculate the sequence length and the largest value it hits. Store and analyze the results, then report the top 10 numbers that produce the longest sequences.

---

## Extra Credit: Decorator-Based Efficiency Timing

Re-implement the `timeEfficiency()` function using Python decorators. Learn how decorators work, and apply them to measure the performance of your `listPrimeNumbers()` function. Then, write a Markdown file that answers several conceptual questions about:
- Higher-order functions
- First-class objects
- Inner functions
- The `@` syntax and its benefits
- Python decorators and encapsulation

---

## Topics Practiced

- Binary search
- Timing functions and benchmarking
- Algorithm comparison (brute-force vs. random)
- Mathematical sequence exploration
- Python functional programming with decorators




