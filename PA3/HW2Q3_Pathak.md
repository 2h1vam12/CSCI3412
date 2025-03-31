# Loop Invariant Proof for Merge Sort's Merging Function

## 3.1 Understanding the Loop Invariant Approach
A loop invariant is a key tool for proving the correctness of an algorithm. It ensures that conditions holds **before**, **during**, and **after** each iteration of a loop.

- **Initialization**: The invariant must be true before the first iteration.
- **Maintenance**: If the invariant holds before an iteration, it continues to hold afterward.
- **Termination**: When the loop ends, the invariant will make sure that the algorithm has completed correctly.

This approach is helpful for iterative algorithms( like sorting methods).

## 3.2 Identifying the Loop Invariant in the Merge Function
For the **merge()** function in merge sort, the loop invariant states that **at the start of each iteration, the merged section of the array is sorted and has the smallest available elements from both the left and right subarrays**.

After this, elements from the left and right subarrays are selected and inserted in order, ensuring that the invariant is still valid.

## 3.3 Initialization Step
Before first iteration:
- The merged portion of the array is empty.
- The left and right subarrays have been sorted by recursive merge sort calls.
- Since no elements have been merged, the invariant holds trivially.

## 3.4 Maintenance Step
During each iteration:
- The smallest remaining element from either the left or right subarray is selected and go to the merged array.
- This makes sure that the merged array remains sorted at all times.
- The indices tracking positions in both subarrays are updated properly, ensuring that no elements are skipped or misplaced.
- Because these steps keep the correct order, the loop invariant holds after every iteration.

## 3.5 Termination Step
Once the loop is done:
- One of the subarrays has been fully merged, and any remaining elements are directly appended.
- Since those remaining elements are already sorted within their original subarrays, appending them maintains the overall order.
- The final merged array is fully sorted, proving that **merge()** correctly combines two sorted arrays into one sorted array.

### **Conclusion**
By proving **initialization, maintenance, and termination**, we confirm that the **merge()** function is correct, ensuring that merge sort successfully produces a sorted array.



