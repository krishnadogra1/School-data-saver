import os
from fpdf import FPDF

BASE_FOLDER = "class"  # Class folders like class/10A/
OUTPUT_FOLDER = "student_pdfs"
OUTPUT_PDF = "all_students_data.pdf"
PRINCIPAL_FILE = "principal.txt"  # Optional file for principal details

# Ensure output folder exists
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Read optional principal details
def get_principal_info():
    if os.path.exists(PRINCIPAL_FILE):
        try:
            with open(PRINCIPAL_FILE, "r") as f:
                return f.read().strip()
        except:
            return None
    return None

# Custom FPDF class with optional principal header
class PDF(FPDF):
    def __init__(self, principal_info=None):
        super().__init__()
        self.principal_info = principal_info

    def header(self):
        self.set_font("Arial", style='B', size=14)
        self.set_text_color(0, 0, 128)
        self.cell(0, 10, "NAS Academy - Student Records", ln=True, align="C")
        if self.principal_info:
            self.set_font("Arial", size=10)
            self.set_text_color(0, 0, 0)
            self.cell(0, 10, self.principal_info, ln=True, align="C")
        self.ln(5)

# Generate final PDF with all student data
def generate_all_students_pdf(all_students_data, principal_info=None):
    pdf = PDF(principal_info=principal_info)
    pdf.set_auto_page_break(auto=True, margin=15)

    for student_id, student_data in all_students_data.items():
        pdf.add_page()

        # Student ID title
        pdf.set_font("Arial", style='B', size=12)
        pdf.set_text_color(0, 100, 0)
        pdf.cell(0, 10, f"Student ID: {student_id}", ln=True)
        pdf.ln(5)

        # Student fields
        pdf.set_font("Arial", size=10)
        pdf.set_text_color(0, 0, 0)
        for key, value in student_data.items():
            pdf.set_font("Arial", style='B', size=10)
            pdf.cell(40, 8, f"{key}:", ln=0)
            pdf.set_font("Arial", size=10)
            pdf.cell(0, 8, value, ln=True)

    output_pdf_path = os.path.join(OUTPUT_FOLDER, OUTPUT_PDF)
    pdf.output(output_pdf_path)
    print(f"\nGenerated PDF for all students: {output_pdf_path}")

# Read student data from class folders
def get_all_students():
    students = {}
    for class_folder in os.listdir(BASE_FOLDER):
        class_path = os.path.join(BASE_FOLDER, class_folder)
        if os.path.isdir(class_path):
            for file in os.listdir(class_path):
                if file.endswith(".txt"):
                    filepath = os.path.join(class_path, file)
                    try:
                        with open(filepath, "r") as f:
                            lines = f.readlines()
                            student_data = {}
                            for line in lines:
                                if ":" in line:
                                    key, value = line.strip().split(":", 1)
                                    student_data[key.strip()] = value.strip()
                            student_data["Class"] = class_folder  # Add class name
                            student_id = file.replace(".txt", "")
                            students[student_id] = student_data
                    except Exception as e:
                        print(f"Error reading {file}: {e}")
    return students

# Main function
def main():
    students = get_all_students()
    if not students:
        print("No student data found.")
        return

    principal_info = get_principal_info()

    print(f"\nGenerating PDF for {len(students)} students...")
    generate_all_students_pdf(students, principal_info=principal_info)
    print(f"\nAll student data saved in '{OUTPUT_FOLDER}/{OUTPUT_PDF}'.")

if __name__ == "__main__":
    main()