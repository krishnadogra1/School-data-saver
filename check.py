import os
import time
import sys

BASE_FOLDER = "class"

# Typing animation
def type_out(text, delay=0.01, color="\033[1;32m"):
    for char in text:
        sys.stdout.write(f"{color}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Crypy Eyes Logo
def show_logo():
    logo = r"""
 ░█████╗░██████╗░██╗░░░██╗██████╗░██╗░░░░░██╗░░░██╗███████╗░██████╗
██╔══██╗██╔══██╗██║░░░██║██╔══██╗██║░░░░░██║░░░██║██╔════╝██╔════╝
███████║██████╦╝██║░░░██║██████╦╝██║░░░░░██║░░░██║█████╗░░╚█████╗░
██╔══██║██╔══██╗██║░░░██║██╔══██╗██║░░░░░██║░░░██║██╔══╝░░░╚═══██╗
██║░░██║██████╦╝╚██████╔╝██████╦╝███████╗╚██████╔╝███████╗██████╔╝
╚═╝░░╚═╝╚═════╝░░╚═════╝░╚═════╝░╚══════╝░╚═════╝░╚══════╝╚═════╝░
"""
    type_out(logo, delay=0.0015)

# Loading animation
def show_loading(task="Searching"):
    for i in range(4):
        sys.stdout.write(f"\r\033[1;32m{task}{'.' * i}   \033[0m")
        sys.stdout.flush()
        time.sleep(0.4)
    print()

# Get all students from folders
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
                            for line in lines:
                                if line.lower().startswith("name:"):
                                    student_id = file.replace(".txt", "")
                                    student_name = line.strip().split(":", 1)[1].strip()
                                    students[student_id] = (student_name, filepath)
                    except:
                        continue
    return students

# Show full detail of a student by file path
def show_full_details(file_path):
    show_loading("Loading full details")
    print("\n\033[1;32m--- STUDENT DETAILS ---\033[0m")
    with open(file_path, "r") as f:
        for line in f:
            type_out(line.strip(), delay=0.01)

# Main function
def main():
    show_logo()
    type_out("Enter password to access: ", delay=0.01)
    password = input().strip()

    if password != "Krishna":
        print("\033[1;31mAccess Denied. Incorrect Password.\033[0m")
        return

    show_loading("Accessing student database")
    student_data = get_all_students()

    print("\n\033[1;32m--- STUDENT RECORDS ---\033[0m")
    for sid, (name, _) in student_data.items():
        print(f"\033[1;34m{sid}\033[0m = {name}")

    print(f"\n\033[1;32mTotal Students Found:\033[0m {len(student_data)}\n")

    # Search by name
    type_out("Enter name to find student ID (optional): ", delay=0.01)
    name_input = input().strip().lower()
    found = False
    for sid, (name, _) in student_data.items():
        if name_input and name_input in name.lower():
            print(f"\n\033[1;34mStudent ID:\033[0m {sid} \033[1;32m=>\033[0m {name}")
            found = True
            break
    if name_input and not found:
        print("\033[1;31mStudent name not found.\033[0m")

    # Search by ID for full details
    type_out("\nEnter Student ID to see full details (optional): ", delay=0.01)
    sid_input = input().strip().upper()
    if sid_input and sid_input in student_data:
        _, file_path = student_data[sid_input]
        show_full_details(file_path)
    elif sid_input:
        print("\033[1;31mStudent ID not found.\033[0m")

if __name__ == "__main__":
    main()
