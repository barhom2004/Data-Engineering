class Student:
    def __init__(self, name, student_id, grades):
        self.__name = name
        self.__student_id = student_id
        self.__grades = grades if grades else []


    @property
    def name(self):
        return self.__name

    @property
    def student_id(self):
        return self.__student_id

    @property
    def grades(self):
        return self.__grades

    # calculate average
    def average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades) / len(self.__grades)

    # grade category
    def grade_category(self):
        avg = self.average()

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    # create object from csv row
    @classmethod
    def from_dict(cls, data):
        grades = []
        if data.get("grades"):
            grades = [float(g) for g in data["grades"].split(",")]
        return cls(data.get("name"), data.get("student_id"), grades)

    # validation helper
    @staticmethod
    def valid_grade(value):
        return 0 <= value <= 100


class Classroom:
    def __init__(self):
        self.__students = []

    @property
    def students(self):
        return list(self.__students)

    def add_student(self, student):
        self.__students.append(student)

    def remove_student(self, sid):
        for s in self.__students:
            if s.student_id == sid:
                self.__students.remove(s)
                return True
        return False

    def find_student(self, sid):
        for s in self.__students:
            if s.student_id == sid:
                return s
        return None

    def class_average(self):
        if not self.__students:
            return 0
        total = 0
        for s in self.__students:
            total += s.average()
        return total / len(self.__students)