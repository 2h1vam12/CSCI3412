# 📚 CSCI 3412 HW5 - Algorithms Project
Author: Shivam Pathak  
Course: CSCI 3412 – Algorithms  
Spring 2025

---

## 🛠️ Project Overview
This repository contains solutions for Homework 5 of CSCI 3412, focusing on:

- Server patch sequencing using DFS and post-order traversal
- 0/1 Knapsack Dynamic Programming for stock portfolio optimization
- Bottom-up Levenshtein Edit Distance (LED) Spelling Checker

---

## 📂 Files

| File | Description |
|:---|:---|
| `PathakHw5Q1.md` | Written answers and pseudocode for server patching problem |
| `PathakHw5Q2.ipynb` | Python notebook for stock portfolio optimization (Knapsack) |
| `PathakHw5Q3.ipynb` | Python notebook for spelling checker using LED algorithm |
| `dictionary.txt` | Word list extracted from "The Adventures of Sherlock Holmes" (for spelling checker) |
| `misspelled.txt` | List of misspelled words to correct (for spelling checker) |

---

## 🧠 Highlights

### Q1: Server Patching (DFS + Post-Order Traversal)
- Used Depth-First Search (DFS) with post-order traversal
- Handled directed graph cycle detection
- Managed early halting and server load constraints

### Q2: Stock Portfolio Optimization (0/1 Knapsack)
- Maximized return under a $2500 budget constraint
- Dynamic Programming approach
- Python code accepts any budget up to $2500

### Q3: Spelling Checker (Levenshtein Edit Distance)
- Built dictionary from Sherlock Holmes corpus
- Spelling correction suggestions sorted by edit distance and frequency
- Used **dictionary.txt** and **misspelled.txt** as input files
- Suggestions can be limited by user command-line input

---

## 📈 Technologies Used
- Python 3
- Jupyter Notebook (.ipynb)
- Standard libraries: `collections`, `re`, `sys`

---

## 🚀 How to Run
Clone the repository:

```bash
git clone https://github.com/yourgithubusername/csci3412-hw5-algorithms.git
cd csci3412-hw5-algorithms
```

Make sure **dictionary.txt** and **misspelled.txt** are placed in the same directory.

Open Jupyter Notebook:

```bash
jupyter notebook
```

Run the individual `.ipynb` files as needed!

---

## 📋 Notes
- **dictionary.txt** is required to build the spelling dictionary.
- **misspelled.txt** is required to test the spelling suggestions.
- No Extra Credit was completed for this submission.

---

# 🚀 QUICK INSTRUCTIONS:
- Save this as `README.md`
- Place it at the **root** of your HW5 GitHub folder
- GitHub will automatically format it cleanly!

