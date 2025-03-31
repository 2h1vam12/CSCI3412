
# Q1-3: Finding a Counterfeit Token (Induction Proof)

## Statement to Prove
To find a counterfeit coin among \( 3^n \) coins, the minimum number of weighings required is **n weighings**.

## Proof by Induction

### **Base Case (n=1):**
For \( n = 1 \), we have **3 coins**. One weighing determines the counterfeit, so the base case holds.

### **Inductive Hypothesis:**
Assume for some \( n = k \), we can find the counterfeit among \( 3^k \) coins using \( k \) weighings.

### **Inductive Step:**
For \( n = k+1 \), divide \( 3^{k+1} \) coins into three groups of \( 3^k \) coins each. One weighing identifies the correct group. By the hypothesis, we solve the remaining \( 3^k \) coins in \( k \) weighings, so the total is \( k+1 \) weighings.

### **Conclusion:**
By induction, the formula holds for all \( n \).

