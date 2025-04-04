# 📂 CSCI 3412 - Homework 4/PA5: Sorting, Merging, BSTs & Web Scraping

This repository contains my solutions to Homework 2 for CSCI 3412. The assignment covers three main parts: 
(This assingment is still a work in progress and all materials will be uploaded on the due date 4/5/25

- Efficient merging of sorted lists
- Binary Search Tree (BST) analysis and manipulation
- Web scraping and data visualization using Python

---

## 📁 Directory Structure

```
.
├── merging_algorithm/
│   ├── merge_k_sorted_lists.py
│   ├── radix_sort.py
│   ├── bucket_sort.py
│   ├── sorted_sublists/  # 100 sublists saved here
│   ├── performance_report.md
│   └── merged_output.txt
├── bst_analysis/
│   ├── bst_fill_algorithm.py
│   ├── fixed_shape_bst.png
│   ├── red_black_tree_rotation.png
│   └── bst_answers.md
├── web_scraping/
│   ├── course_scraper.py
│   ├── cs_courses.html
│   ├── course_graph.png
│   ├── covid_scraper.py
│   ├── covid_data.html
│   └── scraping_review.md
├── HW2_Report.pdf
└── README.md
```

---

## ✅ Question 1: Merging k Sorted Lists (25 points)

### Description:
Implements an efficient O(n log k) algorithm to merge 100 sorted sublists into a single sorted list. Sorting is done using:

- **Radix Sort** for the first 50 sublists
- **Bucket Sort** for the remaining 50 sublists

### Files:
- `merge_k_sorted_lists.py`: Implements the merging algorithm using a priority queue (heap).
- `radix_sort.py`: Contains implementation for radix sort using counting sort as a subroutine.
- `bucket_sort.py`: Implements bucket sort.
- `performance_report.md`: Compares the runtime of O(nk) vs O(n log k) strategies.
- `sorted_sublists/`: Contains all 100 sorted sublists.
- `merged_output.txt`: Final merged output.

---

## ✅ Question 2: Comparisons Among Lists (5 points)

### Description:
Provides filled answers and explanations for CLRS Problem 10-1 on page 249. Focuses on the difference between keys and pointers.

### Files:
- Answers are included in: `HW2_Report.pdf` or `bst_answers.md` (based on your submission choice).

---

## ✅ Question 3: Binary Search Trees (10 points)

### Description:
Answers a series of conceptual and visual questions on BST insertion, fixed-shape population, red-black tree validation, and rotation correction.

### Files:
- `bst_fill_algorithm.py`: Algorithm to systematically fill a fixed-shape BST.
- `fixed_shape_bst.png`: Image of the fixed-shape tree used in questions.
- `red_black_tree_rotation.png`: Final RB tree after performing necessary rotations.
- `bst_answers.md`: Written explanations for all parts (a-e).

---

## ⭐ Extra Credit: Web Scraping with Python (10 points)

### Description:
Explores web scraping through two major exercises:
1. Extracting course information and prerequisites from the CU Denver CS catalog.
2. Extracting and displaying live COVID-19 metrics from Colorado's health department site.

Also includes reviews of beginner web scraping tutorials.

### Files:
- `course_scraper.py`: Scrapes course titles, codes, hours, and prerequisites.
- `cs_courses.html`: HTML file displaying the scraped catalog data.
- `course_graph.png`: Directed graph of course prerequisites using NetworkX.
- `covid_scraper.py`: Scrapes and presents COVID data from the Colorado Department of Public Health.
- `covid_data.html`: Table of COVID metrics by county.
- `scraping_review.md`: Reviews and links to additional scraping resources.

---

## 📜 Final Submission

- `HW2_Report.pdf`: Contains all answers and explanations in one clean file (if submitted this way).
- OR all individual `.md`, `.py`, `.png`, `.html` files as shown above.

---

## 🛠️ How to Run

Make sure you have the following dependencies installed:

```bash
pip install beautifulsoup4 requests matplotlib networkx pandas
```

To run individual scripts:

```bash
python merge_k_sorted_lists.py
python course_scraper.py
python covid_scraper.py
```

To view HTML output:

```bash
open cs_courses.html
open covid_data.html
```
