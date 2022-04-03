class Student:
    """Student class"""

    def __init__(self, id: int):
        self.id = id

    def registration_number(self, department_id: int) -> str:
        """Return registration number"""
        return f"{self.id}-{department_id}"


class Department:
    "Department class"

    def __init__(self, id, student):
        self.id = id
        self.student = student

    def student_registration(self):
        return self.student.registration_number(self.id)


if __name__ == "__main__":
    student = Student(10)
    department = Department("ENG", student)
    print(department.student_registration())
    print("Department class : ", department)
    print("Student class : ", student)
    del department
    print("After del Student class : ", student)
