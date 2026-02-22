import sys
from models import Student
from analytics import (
    get_top_student,
    get_low_student,
    get_ranking,
    get_grade_count,
)
from utils import (
    load_students,
    save_students,
    get_text_input,
    get_grade_input,
)

FILE_NAME = "data.csv"


def menu():
    print("\n--- Student System ---")
    print("1. Add student")
    print("2. Remove student")
    print("3. Search student")
    print("4. Class average")
    print("5. Top & lowest student")
    print("6. Show ranking")
    print("7. Grade distribution")
    print("8. Save")
    print("9. Exit")


def main():
    classroom = load_students(FILE_NAME)

    while True:
        menu()
        choice = input("Choose: ")

        try:
            if choice == "1":
                name = get_text_input("Name: ")
                sid = get_text_input("ID: ")

                grades = []
                while True:
                    more = input("Add grade? (y/n): ").lower()
                    if more == "y":
                        grade = get_grade_input("Enter grade: ")
                        grades.append(grade)
                    else:
                        break

                student = Student(name, sid, grades)
                classroom.add_student(student)
                print("Student added.")

            elif choice == "2":
                sid = get_text_input("ID to remove: ")
                if classroom.remove_student(sid):
                    print("Removed.")
                else:
                    print("Not found.")

            elif choice == "3":
                sid = get_text_input("ID to search: ")
                s = classroom.find_student(sid)
                if s:
                    print(s.name, "-", s.average())
                else:
                    print("Not found.")

            elif choice == "4":
                print("Class average:", classroom.class_average())

            elif choice == "5":
                top = get_top_student(classroom)
                low = get_low_student(classroom)
                if top:
                    print("Top:", top.name)
                if low:
                    print("Lowest:", low.name)

            elif choice == "6":
                ranked = get_ranking(classroom)
                for s in ranked:
                    print(s.name, "-", s.average())

            elif choice == "7":
                print(get_grade_count(classroom))


            elif choice == "8":

                save_students(classroom, FILE_NAME)

                print("Data saved successfully.")


            elif choice == "9":

                print("Goodbye.")

                sys.exit()

            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()