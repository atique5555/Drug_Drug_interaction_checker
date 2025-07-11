# 💊 Drug-Drug Interaction Checker
*A beginner-friendly Python project to identify potential drug-drug interactions*

---

## 📌 Project Overview

The **Drug-Drug Interaction Checker** is a command-line Python program designed to help users identify potential interactions between commonly used drugs. With a database of over 100 known drug interaction pairs, this tool allows users to input two drug names and receive instant feedback on whether the combination is safe, should be used with caution, or must be avoided entirely.

This project was developed as part of the **EDGE Basic Python Program**, with the goal of practicing fundamental Python skills while creating a real-world healthcare-related application.

---

## 🚀 Features

- ✅ 100+ commonly known drug interaction pairs  
- ✅ Case-insensitive input handling  
- ✅ Reverse pair detection (A+B or B+A both supported)  
- ✅ Friendly user prompts and warnings  
- ✅ Continuous checking in a loop until user exits  
- ✅ Simple and extendable code structure  

---

## 🛠 Technologies Used

- Python 3  
- Dictionary, Set, Tuple  
- Conditional Statements (`if-else`)  
- Loop (`while`)  
- String methods (`lower()`, `strip()`, `title()`)

---

## 🧪 How It Works

1. The program stores known drug interaction pairs in a dictionary, where each key is a tuple of two drug names, and the value is a message describing the interaction.
2. The user is asked to enter two drug names. The program checks if both drugs exist in the dataset.
3. If the pair exists (in any order), the corresponding interaction message is shown. If the pair is unknown, it notifies the user accordingly.
4. The user can type `stop` to exit the program at any time.

---

## 📸 Sample Output

```text
Enter first drug name: metronidazole  
Drug 1: Metronidazole  

Enter second drug name: alcohol  
Drug 2: Alcohol  

🔍 Metronidazole x Alcohol = ✅ Interaction: Severe nausea and vomiting. Avoid alcohol.
