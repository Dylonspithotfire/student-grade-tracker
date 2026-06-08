# grade_tracker.py
# Student Grade Tracker - A command-line Python script using object-oriented
# programming to manage and report student grades.
#
# Usage: python grade_tracker.py
# No external dependencies required (Python Standard Library only).


class Student:
    """Represents a single student with a name and a list of grades."""

    def __init__(self, name, grades):
        """
        Initialize a Student.

        Args:
            name (str): The student's full name.
            grades (list of float): A list of numeric grade values.
        """
        self.name = name
        self.grades = grades

    def get_average(self):
        """Calculate and return the student's grade average."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __repr__(self):
        return f"Student(name={self.name!r}, grades={self.grades})"


class GradeBook:
    """Manages a collection of Students and produces grade reports."""

    def __init__(self):
        """Initialize an empty GradeBook."""
        self.students = []

    def add_student(self, student):
        """
        Add a Student object to the GradeBook.

        Args:
            student (Student): The student to add.
        """
        self.students.append(student)

    def get_class_average(self):
        """Calculate and return the overall class average across all students."""
        if not self.students:
            return 0.0
        total = sum(s.get_average() for s in self.students)
        return total / len(self.students)

    def print_report(self):
        """Print a formatted grade summary report to the terminal."""
        print("Student Grade Report")
        print("-" * 20)
        for student in self.students:
            avg = student.get_average()
            print(f"{student.name}: Average: {avg:.2f}")
        print("-" * 20)
        class_avg = self.get_class_average()
        print(f"Class Average: {class_avg:.2f}")


# ---------------------------------------------------------------------------
# Student data - Edit this section to use your own students and grades.
# Each Student takes a name (string) and a list of numeric grade values.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    gradebook = GradeBook()

    gradebook.add_student(Student("Alice", [92, 88, 95, 79, 91]))
    gradebook.add_student(Student("Bob", [74, 80, 68, 85, 72]))
    gradebook.add_student(Student("Carol", [88, 91, 94, 97, 90]))
    gradebook.add_student(Student("David", [60, 72, 65, 70, 68]))
    gradebook.add_student(Student("Eva", [95, 98, 100, 96, 99]))

    gradebook.print_report()
