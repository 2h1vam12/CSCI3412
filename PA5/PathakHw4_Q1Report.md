### **Code Output**

0  Heap Merge (O(n log k))        0.519557
1      Naive Merge (O(nk))        8.690537

![img.png](img.png)<Figure size 800x500 with 1 Axes>

### **Performance Comparison Report: Heap Merge vs. Naive Merge**

This code compares two approaches to merging `k = 100` sorted sublists, each containing 10,000 integers, into one single sorted list of 1,000,000 integers.

- The **heap-based merge algorithm** uses a **min-heap (priority queue)** to select the smallest next element across all lists in `O(log k)` time which is very efficient.
- The **naive merge algorithm** manually scans all `k` heads of the lists at each step, leading to `O(k)` work per inserted element which is a lot less efficient.

---

#### **Theoretical Time Complexities explained in my code**
| Approach | Time Complexity | Explanation |
|----------|------------------|-------------|
| **Heap Merge** | `O(n log k)` | Each of the `n` total elements is inserted and extracted from a min-heap of size `k`, which takes `O(log k)` per operation. |
| **Naive Merge** | `O(nk)` | For each of the `n` insertions, the algorithm performs a linear scan across all `k` list heads to find the smallest. |

---

#### **Results (From Code Benchmarking)**

| Method | Time (seconds) |
|--------|----------------|
| Heap Merge (`O(n log k)`) | ~0.52 seconds |
| Naive Merge (`O(nk)`)     | ~8.69 seconds |

> This shows the **heap merge is ~17 seconds faster** than the naive merge at this scale.

#### **Conclusion**
The results confirm the expected advantage of the `O(n log k)`runtime from the heap-based merge algorithm. While both approaches produce the correct output, the naive method ois very inefficient as the number of lists (`k`) grows. The heap-based approach is more scalable and is ideal for large datasets where merging speed is critical.

