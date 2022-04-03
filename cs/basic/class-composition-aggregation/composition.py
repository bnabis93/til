class Student:
    """Student class"""

    def __init__(self, id: int):
        self.id = id

    def registration_number(self, department_id: int) -> str:
        """Return registration number"""
        return f"{self.id}-{department_id}"


class Department:
    "Department class"

    def __init__(self, id, student_id):
        self.id = id
        self.student = Student(student_id)

    def student_registration(self):
        return self.student.registration_number(self.id)


if __name__ == "__main__":
    department = Department("ENG", 10)
    print(department.student_registration())
    print("Department class : ", department)
    print("Student class : ", department.student)
