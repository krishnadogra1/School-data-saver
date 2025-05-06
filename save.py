import os

# Function to create class folder if not exist
def create_class_folder(class_name):
    folder_name = f"class/{class_name}"
    os.makedirs(folder_name, exist_ok=True)
    return folder_name

# Function to add student data
def add_student_data():
    print("\033[1;32m" + "-" * 50)
    print("     WELCOME TO NAS ACADEMY SUJWAN")
    print("-" * 50)
    
    # Input class and student details
    student_class = input("\033[1;32mEnter Class (e.g., 1, 2, 6, 10): ").strip()
    student_id = input("\033[1;32mEnter Student ID (e.g., KR01): ").strip().upper()
    name = input("\033[1;32mEnter Student Name: ").strip()
    roll_number = input("\033[1;32mEnter Roll Number: ").strip()
    phone_number = input("\033[1;32mEnter Phone Number: ").strip()
    parent_name = input("\033[1;32mEnter Parent's Name: ").strip()
    address = input("\033[1;32mEnter Address: ").strip()
    height = input("\033[1;32mEnter Height (in cm): ").strip()
    weight = input("\033[1;32mEnter Weight (in kg): ").strip()
    hobbies = input("\033[1;32mEnter Hobbies (comma separated): ").strip()

    # Create class folder if not exist
    class_folder = create_class_folder(student_class)

    # Prepare the student file name
    student_file = os.path.join(class_folder, f"{student_id}.txt")

    # Create or overwrite the student's data file
    with open(student_file, "w") as f:
        f.write(f"Welcome to Nas Academy Sujwan\n\n")
        f.write(f"Student ID: {student_id}\n")
        f.write(f"Name: {name}\n")
        f.write(f"Roll Number: {roll_number}\n")
        f.write(f"Phone Number: {phone_number}\n")
        f.write(f"Parent's Name: {parent_name}\n")
        f.write(f"Address: {address}\n")
        f.write(f"Height: {height} cm\n")
        f.write(f"Weight: {weight} kg\n")
        f.write(f"Hobbies: {hobbies}\n")
        f.write("-" * 30 + "\n")

    print(f"\033[1;32mStudent data for {student_id} saved successfully in Class {student_class}!\n")

# Main function to add multiple students
if __name__ == "__main__":
    while True:
        add_student_data()
        again = input("\n\033[1;33mAdd another student? (yes/no): ").strip().lower()
        if again != "yes":
            print("\033[1;31mEXITING NAS ACADEMY...")
            break
