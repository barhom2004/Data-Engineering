import csv
from models import Student, Classroom


def load_students(file_name):
    classroom = Classroom()

    try:
        with open(file_name, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student.from_dict(row)
                classroom.add_student(student)
    except FileNotFoundError:
        print("File not found, starting empty.")

    return classroom


def save_students(classroom, file_name):
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        fields = ["name", "student_id", "grades"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()

        for s in classroom.students:
            grades_text = ",".join(str(g) for g in s.grades)
            writer.writerow({
                "name": s.name,
                "student_id": s.student_id,
                "grades": grades_text
            })


def get_text_input(msg):
    while True:
        value = input(msg).strip()
        if value:
            return value
        print("Value cannot be empty.")


def get_grade_input(msg):
    while True:
        try:
            value = float(input(msg))
            if Student.valid_grade(value):
                return value
            print("Grade must be 0-100.")
        except ValueError:
            print("Invalid number.")