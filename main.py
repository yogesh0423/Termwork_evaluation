import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import csv
import os

WEIGHTS = {
    "Attendance": 0.10,
    "Unit Test": 0.40,
    "Achievements": 0.20,
    "Mock Practical": 0.30
}

def calculate_score(attendance, unit_test, achievements, mock):
    try:
        attendance_score = (float(attendance) / 100) * 10
        unit_test_score = float(unit_test)
        achievements_score = float(achievements)
        mock_score = float(mock)

        final_score = (
            attendance_score * WEIGHTS["Attendance"] +
            unit_test_score * WEIGHTS["Unit Test"] +
            achievements_score * WEIGHTS["Achievements"] +
            mock_score * WEIGHTS["Mock Practical"]
        )
        return round(final_score, 2)
    except:
        return "Error"

class TermWorkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Term Work Evaluation System")

        self.tree = ttk.Treeview(root, columns=("Name", "Final Score"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Final Score", text="Final Score")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        load_btn = tk.Button(btn_frame, text="Load CSV", command=self.load_csv)
        load_btn.grid(row=0, column=0, padx=5)

        export_btn = tk.Button(btn_frame, text="Export Results", command=self.export_csv)
        export_btn.grid(row=0, column=1, padx=5)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return

        self.data = []

        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                self.tree.delete(*self.tree.get_children())
                for row in reader:
                    name = row['Name']
                    score = calculate_score(
                        row['Attendance (%)'],
                        row['Unit Test Marks'],
                        row['Achievements Score'],
                        row['Mock Practical']
                    )
                    self.data.append({'Name': name, 'Score': score})
                    self.tree.insert('', 'end', values=(name, score))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV:\n{str(e)}")

    def export_csv(self):
        if not hasattr(self, 'data') or not self.data:
            messagebox.showwarning("No Data", "No data to export.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return

        try:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Final Score'])
                for entry in self.data:
                    writer.writerow([entry['Name'], entry['Score']])
            messagebox.showinfo("Success", f"Results exported to {os.path.basename(file_path)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export CSV:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TermWorkApp(root)
    root.geometry("500x400")
    root.mainloop()
