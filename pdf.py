import os
from fpdf import FPDF

BASE_FOLDER = "class"  # Folder where the student folders are located
OUTPUT_FOLDER = "student_pdfs"  # Folder where PDFs will be saved
OUTPUT_PDF = "all_students_data.pdf"  # Name of the single PDF file containing all student data

# Create output folder if it doesn't exist
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Function to generate the main PDF for all students
def generate_all_students_pdf(all_students_data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set title and font
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(200, 10, txt="Student Records - NAS Academy", ln=True, align='C')
    pdf.ln(10)  # Line break

    # Add student data
    pdf.set_font("Arial", size=10)
    for student_id, student_data in all_students_data.items():
        pdf.cell(200, 10, txt=f"Student ID: {student_id}", ln=True)
        for key, value in student_data.items():
            pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
        pdf.ln(5)  # Line break after each student

    # Save the PDF
    output_pdf_path = os.path.join(OUTPUT_FOLDER, OUTPUT_PDF)
    pdf.output(output_pdf_path)

    print(f"Generated PDF for all students: {output_pdf_path}")

# Get all student data
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
                            student_id = file.replace(".txt", "")
                            students[student_id] = student_data
                    except Exception as e:
                        print(f"Error reading {file}: {e}")
                        continue
    return students

# Main function to generate the single PDF with all students' data
def main():
    students = get_all_students()

    if not students:
        print("No student data found.")
        return

    print(f"\nGenerating PDF for {len(students)} students...")

    # Generate PDF with all students' data
    generate_all_students_pdf(students)

    print(f"\nAll student data has been generated and saved in the '{OUTPUT_FOLDER}/{OUTPUT_PDF}'.")

if __name__ == "__main__":
    main()
