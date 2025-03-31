#  CSCI 3421 – Advanced Algorithm Problems & Optimization (PA4)

This assignment includes a mix of application-based algorithm design, time complexity analysis, sorting optimization, and structural recursion. The tasks combine theoretical understanding with hands-on Python programming.


---

##  Q1: Application Problems (10 pts)

### Q1-1: Book & Cover Matching (5 pts)
Design an algorithm (similar to the nuts and bolts problem) to match unsorted books and their unique covers using only book–cover comparisons.

###  Q1-2: Plateau-Valley Sorting (5 pts)
Devise an O(n) algorithm to rearrange a list into a plateau-valley pattern, alternating between increasing and decreasing elements.

---

## Q2: Time Efficiency Questions (10 pts)

- Apply the substitution method to analyze recurrence relations
- Evaluate the truth of complexity relationships
- Order a list of given functions by growth rate

---

##  Q3: Insertion Sort in Divide & Conquer (20 pts)

###  Q3-1: CLRS Problem 2-1 (a–c)
Solve CLRS 2-1 and describe how small subarrays affect divide-and-conquer algorithms like merge sort.

###  Q3-2: Replacing Merge Sort with Quicksort and Bubble Sort (15 pts)
- Implement and test optimized bubble sort and quicksort
- Combine both into a hybrid algorithm
- Experiment with different `k` values to find the optimal cutoff point for switching between the two algorithms
- Plot time efficiency vs. `k` values

---

##  Q4: Loop Invariant Proof (5 pts)

Prove the correctness of your `merge()` logic using the loop invariant technique. Include:
- Invariant description
- Initialization
- Maintenance
- Termination

---

##  Extra Credit (10 pts)

###  a) Types of Recursion (2 pts)
Describe the three recursion types discussed in class.

###  b) Structural Recursion: `myFind()` (8 pts)
Write a recursive Python program that mimics the Unix `find` command:
- Traverse the filesystem without using `os.walk()`
- Use `os.stat()` to identify files
- Print matches and their sizes
- Return total size (bytes) of all matching regular files
- Use a **callback function** to accumulate size

---


