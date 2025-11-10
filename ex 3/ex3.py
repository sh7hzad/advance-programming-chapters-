import tkinter as tk
from tkinter import simpledialog, messagebox
import os

# --- Constants ---
FILE_PATH = 'studentsmarks.txt'
TOTAL_POSSIBLE_MARKS = 160
WINDOW_TITLE = "Student Performance Manager"
MAX_LINES = 250

# --- Helper Functions ---

def create_mock_file():
    """Creates a mock studentMarks.txt file if it doesn't exist.
    Updated with 10 student records from the user query."""
    if not os.path.exists(FILE_PATH):
        content = (
            "10\n"
            "1001,Ava Williams,13,15,17,70\n"
            "1002,Liam Thompson,11,13,15,60\n"
            "1003,Sophia Brown,17,18,19,80\n"
            "1004,Noah Wilson,9,11,13,50\n"
            "1005,Mia Garcia,14,13,12,65\n"
            "1006,James Lee,14,16,18,75\n"
            "1007,Isabella Scott,12,14,16,68\n"
            "1008,Mason Harris,13,15,17,72\n"
            "1009,Lily Adams,11,13,14,58\n"
            "1010,Ethan Moore,15,17,19,78\n"
        )
        with open(FILE_PATH, 'w') as f:
            f.write(content)

def calculate_student_metrics(data_line):
    """Parses a data line and calculates all required metrics."""
    parts = data_line.strip().split(',')
    
    # Clean and assign basic data
    code = parts[0]
    name = parts[1].strip()
    
    # Parse marks, they are strings, need conversion
    try:
        cw_marks = [int(m.strip()) for m in parts[2:-1]]
        exam_mark = int(parts[-1].strip())
    except ValueError:
        return None # Skip invalid lines

    total_cw_mark = sum(cw_marks)
    total_score = total_cw_mark + exam_mark
    percentage = (total_score / TOTAL_POSSIBLE_MARKS) * 100
    
    # Determine grade
    if percentage >= 70: grade = 'A'
    elif percentage >= 60: grade = 'B'
    elif percentage >= 50: grade = 'C'
    elif percentage >= 40: grade = 'D'
    else: grade = 'F'
    
    return {
        'code': code,
        'name': name,
        'total_cw': total_cw_mark,
        'exam': exam_mark,
        'total_score': total_score,
        'percentage': percentage,
        'grade': grade
    }

def format_student_output(student):
    """Formats a single student's data into a readable string."""
    return (
        f"--- Student Record ---\n"
        f"Name: {student['name']}\n"
        f"Student Number: {student['code']}\n"
        f"Total Coursework Mark (Max 60): {student['total_cw']}\n"
        f"Exam Mark (Max 100): {student['exam']}\n"
        f"Overall Percentage: {student['percentage']:.2f}%\n"
        f"Student Grade: {student['grade']}\n"
        f"----------------------\n"
    )

class StudentManagerApp:
    def __init__(self, master):
        self.master = master
        master.title(WINDOW_TITLE)
        master.geometry("600x650")
        master.configure(bg='#f0f4f8')
        
        self.students = self.load_data()
        
        # UI Setup
        self.output_frame = tk.Frame(master, padx=10, pady=10, bg='#f0f4f8')
        self.output_frame.pack(fill='both', expand=True)
        
        self.output_text = tk.Text(self.output_frame, wrap='word', height=25, font=('Inter', 10), bg='white', fg='#333', padx=10, pady=10, relief=tk.FLAT)
        self.output_text.pack(fill='both', expand=True)
        
        self.menu_frame = tk.Frame(master, bg='#e0e6ed', padx=10, pady=5)
        self.menu_frame.pack(fill='x')

        self.create_buttons()
        self.display_message("Welcome to the Student Manager. Please select an option from the menu below.")

    def create_buttons(self):
        """Creates the main menu buttons."""
        buttons_info = [
            ("1. View All", self.view_all_records),
            ("2. View Individual", self.view_individual_record),
            ("3. Highest Score", self.show_highest_score),
            ("4. Lowest Score", self.show_lowest_score),
        ]
        
        for text, command in buttons_info:
            tk.Button(self.menu_frame, text=text, command=command, bg='#4299e1', fg='white', font=('Inter', 10, 'bold'), 
                      padx=10, pady=5, relief=tk.FLAT, activebackground='#3182ce', activeforeground='white',
                      cursor='hand2').pack(side='left', padx=5, pady=5, fill='x', expand=True)

    def display_message(self, message):
        """Clears the text area and displays a new message."""
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, message)

    def load_data(self):
        """Loads and processes student data from the file."""
        create_mock_file() # Ensure the file exists
        students = []
        try:
            with open(FILE_PATH, 'r') as f:
                lines = f.readlines()
                # The first line is the student count, which we can skip for processing
                for i, line in enumerate(lines[1:]):
                    student_data = calculate_student_metrics(line)
                    if student_data:
                        students.append(student_data)
        except FileNotFoundError:
            messagebox.showerror("Error", "Data file not found.")
        return students

    # --- Menu Item 1: View all student records ---
    def view_all_records(self):
        if not self.students:
            self.display_message("No student records loaded.")
            return

        output = "--- All Student Records ---\n\n"
        total_percentage_sum = 0
        
        # Header for table-like output
        output += f"{'Code':<6} {'Name':<20} {'CW Mark':<9} {'Exam Mark':<10} {'Percentage':<12} {'Grade':<6}\n"
        output += "-" * 70 + "\n"

        for student in self.students:
            output += (
                f"{student['code']:<6} "
                f"{student['name']:<20} "
                f"{student['total_cw']:<9} "
                f"{student['exam']:<10} "
                f"{student['percentage']:.2f}%{'':<10} "
                f"{student['grade']:<6}\n"
            )
            total_percentage_sum += student['percentage']

        # Summary
        num_students = len(self.students)
        avg_percentage = total_percentage_sum / num_students if num_students > 0 else 0
        
        output += "\n" + "=" * 70 + "\n"
        output += f"SUMMARY:\n"
        output += f"Total students in class: {num_students}\n"
        output += f"Average percentage mark obtained: {avg_percentage:.2f}%\n"

        self.display_message(output)

    # --- Menu Item 2: View individual student record ---
    def view_individual_record(self):
        input_value = simpledialog.askstring("Input", "Enter Student Name or Code (e.g., Ava Williams or 1001):", parent=self.master)
        
        if input_value is None or input_value.strip() == "":
            self.display_message("Individual search cancelled.")
            return

        query = input_value.strip().lower()
        found_student = None

        for student in self.students:
            # Check for exact code match or name substring match
            if student['code'] == query or query in student['name'].lower():
                found_student = student
                break

        if found_student:
            self.display_message(format_student_output(found_student))
        else:
            self.display_message(f"No student found matching '{input_value}'.")

    # --- Menu Item 3 & 4: Highest/Lowest Score ---
    def find_extremum_student(self, mode):
        """Finds student with highest or lowest total score."""
        if not self.students:
            self.display_message(f"Cannot determine {mode} score: No student records loaded.")
            return

        if mode == 'highest':
            best_student = max(self.students, key=lambda s: s['total_score'])
            title = "--- Student with Highest Total Score ---"
        else: # mode == 'lowest'
            best_student = min(self.students, key=lambda s: s['total_score'])
            title = "--- Student with Lowest Total Score ---"
        
        output = title + "\n" + format_student_output(best_student)
        self.display_message(output)

    def show_highest_score(self):
        self.find_extremum_student('highest')

    def show_lowest_score(self):
        self.find_extremum_student('lowest')


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagerApp(root)
    root.mainloop()