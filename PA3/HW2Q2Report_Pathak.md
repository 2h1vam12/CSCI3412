# Sorting Algorithm Performance Analysis

## - Results 
- **Insertion Sort** handled all data sets at **O(n²) time complexity** but had my code running for an entire day to do so.
- **Merge Sort** handled all datasets efficiently due to its **O(n log n) complexity**.

## - Execution Time Analysis
The following trends were observed:
- **Insertion Sort is extremely slow** for large datasets (100,000+ elements taking 24 hours), making it very impractical.
- **Merge Sort scales efficiently**, maintaining reasonable execution times even for **1,000,000 elements**.
- The time complexity difference between **O(n²) and O(n log n)** is evident in the increasing execution time gap.

## - Comparison Count Analysis
- **Insertion Sort performs excessive comparisons**, making it highly inefficient.
- **Merge Sort makes significantly fewer comparisons**, following an **O(n log n) growth pattern**.

## - Conclusion
The results confirm that **Insertion Sort is only viable for small datasets**, while **Merge Sort is the preferred algorithm for large-scale sorting**.

