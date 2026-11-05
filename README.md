# Password Strength Checker 🔐

An interactive password strength evaluation tool built with Python and NumPy.

This program analyzes passwords based on their length, character diversity, and repetition frequency to determine whether a password is Strong or Weak.

### Features
- **Special Character Detection:** Identifies special characters and assigns them higher scores.
- **Number Detection:** Counts numeric characters and evaluates their contribution.
- **Uppercase Detection:** Analyzes uppercase letters.
- **Lowercase Detection:** Analyzes lowercase letters.
- **Repetition Analysis:** Detects frequently repeated characters.
- **Strength Evaluation:** Uses a scoring system to classify passwords as Strong or Weak.
- **Input Validation:** Rejects passwords containing only numeric characters.
- **Interactive CLI:** Supports continuous password checking.

### Scoring System

| Character Type | Score |
|---|---:|
| Special Characters | 2 |
| Numbers | 1.5 |
| Uppercase Letters | 1.5 |
| Lowercase Letters | 1 |

The program calculates the average character score and evaluates it alongside password length and repetition frequency.

### Technologies Used
- Python
- NumPy
- Lists & List Comprehensions
- Functions
- String Methods
- Conditional Statements
- Loops
- OS Module

### How to Run

Install NumPy:
```bash
pip install numpy
```

Run the program:
```bash
python main.py
```

### Classification Rules
A password is classified as **Strong** when:
- Its length is at least 8 characters.
- Its average character score meets the required threshold.
- Its repetition count does not exceed the allowed limit.

Otherwise, it is classified as Weak.

**A Python project focused on string analysis, data processing, scoring algorithms, and NumPy operations.**
