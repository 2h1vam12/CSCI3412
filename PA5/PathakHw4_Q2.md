## Q2 Answer 

### **SEARCH(L, k)**  
| Type                          | Big-O     | Explanation                                                         |
|-------------------------------|-----------|---------------------------------------------------------------------|
| Unsorted, Singly Linked       | O(n)      | Scans the list node by node to find key `k`, since it's unsorted.   |
| Sorted, Singly Linked         | O(n)      | Might still need to scan up to the end to find or fail to find `k`. |
| Unsorted, Doubly Linked       | O(n)      | Being doubly linked doesn't help; still need to scan for key `k`.   |
| Sorted, Doubly Linked         | O(n)      | Can’t jump directly to a key; needs to search sequentially for `k`. |

---

### **INSERT(L, x)**  
| Type                          | Big-O     | Explanation |
|-------------------------------|-----------|-------------|
| Unsorted, Singly Linked       | O(1)      | Can insert at the head of the list with a constant-time pointer update. |
| Sorted, Singly Linked         | O(n)      | Must find the correct position to maintain sorted order, requiring traversal. |
| Unsorted, Doubly Linked       | O(1)      | Can insert at head/tail directly with pointer updates. |
| Sorted, Doubly Linked         | O(n)      | Still need to find the insertion point even though links are bidirectional. |

---

### **DELETE(L, x)**  
| Type                          | Big-O     | Explanation                                                  |
|-------------------------------|-----------|--------------------------------------------------------------|
| Unsorted, Singly Linked       | O(n)      | Need to find the previous node and update its .next pointer (traversal). |
| Sorted, Singly Linked         | O(n)      | Same as above — previous node not directly accessible, even if sorted. |
| Unsorted, Doubly Linked       | O(1)      | Given a pointer x, update .prev and .next pointers directly. |
| Sorted, Doubly Linked         | O(1)      | Same as above; sorting doesn't impact deletion when x is known. |

---

### **SUCCESSOR(L, x)**  
| Type                          | Big-O     | Explanation |
|-------------------------------|-----------|-------------|
| Unsorted, Singly Linked       | O(1)      | Can access the .next node of x directly. |
| Sorted, Singly Linked         | O(1)      | Same as unsorted — the .next pointer is available. |
| Unsorted, Doubly Linked       | O(1)      | Also has .next, no need to scan. |
| Sorted, Doubly Linked         | O(1)      | Same — .next is always a direct pointer. |

---

### **PREDECESSOR(L, x)**  
| Type                          | Big-O     | Explanation |
|-------------------------------|-----------|-------------|
| Unsorted, Singly Linked       | O(n)      | No backward pointers; must scan from the head to find the previous node. |
| Sorted, Singly Linked         | O(n)      | Same as above — sorting doesn’t change the structure. |
| Unsorted, Doubly Linked       | O(1)      | You can access x.prev directly in constant time. |
| Sorted, Doubly Linked         | O(1)      | Same — bidirectional links make predecessor access immediate. |

---

### **MINIMUM(L)**  
| Type                          | Big-O     | Explanation |
|-------------------------------|-----------|-------------|
| Unsorted, Singly Linked       | O(n)      | Must scan the entire list to find the smallest value. |
| Sorted, Singly Linked         | O(1)      | The minimum is always at the head of the list. |
| Unsorted, Doubly Linked       | O(n)      | Still must scan the entire list despite having backward links. |
| Sorted, Doubly Linked         | O(1)      | Minimum is at the head and can be accessed directly. |

---

### **MAXIMUM(L)**  
| Type                          | Big-O   | Explanation |
|-------------------------------|---------|-------------|
| Unsorted, Singly Linked       | O(n)    | Must scan all nodes to find the largest key. |
| Sorted, Singly Linked         | O(n)    | Maximum is at the tail, but you must traverse from the head to reach it. |
| Unsorted, Doubly Linked       | O(n)    | Still requires a full scan — list is not sorted. |
| Sorted, Doubly Linked         | O(1)    | Can access the tail node directly to retrieve the maximum. |

