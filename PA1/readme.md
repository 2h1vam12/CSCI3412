#  HW1a - Substitution Cipher (CSCI 3421)
---

##  Environment Setup

Before writing the program, I completed the following:
- ✅ Installed Python 3
- ✅ Installed Jupyter Notebook
- ✅ (Optional) Set up REPL.it and VS Code with Python extensions
- ✅ Verified all tools were running

---

##  Assignment Description

Create a **substitution cipher** that:
- Accepts an integer `n` (1-25) and a string `message` from the user.
- Encodes the message by shifting each letter by `n` positions in the alphabet.
  - Handles wraparound (e.g., `z` + 2 = `b`)
  - Preserves uppercase, lowercase, and numbers
  - Leaves non-alphanumeric characters unchanged
- Implements a **decoding function** that reverses the process
- Uses a `main()` function to demonstrate:
  - Original input
  - Encoded output
  - Decoded message (should match original)

---
##  Concepts Practiced

- ASCII manipulation with `ord()` and `chr()`
- String processing in Python
- Python program structure and input/output
- Jupyter Notebook / Python script workflows
