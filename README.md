# 🎓 Student Term Work Evaluation System

This is a simple Tkinter-based desktop application that calculates and displays
student term work scores based on different weighted parameters.

## ✨ Features
- Load student data from a CSV file.
- Automatically calculate final term work score using weighted formula.
- Display results in a table (Treeview widget).
- Export results to a new CSV file.

## ⚙️ Formula Used
Final Score = (Attendance × 0.10) + (Unit Test × 0.40) + (Achievements × 0.20) + (Mock Practical × 0.30)

bash
Copy code

## 🧮 Example CSV Format
| Name | Attendance (%) | Unit Test Marks | Achievements Score | Mock Practical |
|------|----------------|-----------------|--------------------|----------------|
| Rahul | 90 | 80 | 10 | 85 |

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/termwork_evaluation.git
Navigate into the folder:

bash
Copy code
cd termwork_evaluation
Run the app:

bash
Copy code
python main.py
