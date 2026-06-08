# Student Grade Tracker

Student Grade Tracker is a command-line Python script that uses object-oriented programming to manage and report student grades. It features a `Student` class for storing individual names and numeric grades, and a `GradeBook` class for computing averages and printing a formatted terminal report. The entire tool runs from a single `.py` file with no setup or dependencies required.

## Features

- **Object-Oriented Design:** Built with `Student` and `GradeBook` classes for clean, modular code.
- **Automated Grade Calculations:** Computes each student's individual average and the overall class average.
- **Formatted Terminal Report:** Prints a clear, readable grade summary directly to the terminal.
- **Single-File Script:** No packages or project folders needed — just one `.py` file.

## How It Works

> **Quick note:** Students and grades are hardcoded in the script. To use your own data, edit the student list at the bottom of `grade_tracker.py` before running.

The `Student` class stores a student's name and a list of numeric grade values, and includes a method to calculate their individual average. The `GradeBook` class holds a list of `Student` objects and handles adding students, computing the class-wide average, and printing the full summary report.

## Prerequisites

- Python 3.8 or higher

## Installation

No installation or additional packages required:

1. Download or clone this repository.
2. Open a terminal and navigate to the folder containing `grade_tracker.py`.

```bash
git clone https://github.com/Dylonspithotfire/student-grade-tracker.git
cd student-grade-tracker
```

## Usage

Run the script from your terminal:

```bash
python grade_tracker.py
```

Expected output:

```
Student Grade Report
--------------------
Alice: Average: 89.00
Bob: Average: 75.80
Carol: Average: 92.00
David: Average: 67.00
Eva: Average: 97.60
--------------------
Class Average: 84.28
```

## Customizing Student Data

Open `grade_tracker.py` and edit the student list inside the `if __name__ == "__main__":` block:

```python
gradebook.add_student(Student("Your Student Name", [85, 90, 78, 92, 88]))
```

Each `Student` takes:
- A name as a string
- A list of numeric grade values (integers or floats)

## Project Structure

```
student-grade-tracker/
├── grade_tracker.py   # Main script containing Student and GradeBook classes
├── .gitignore
├── LICENSE
└── README.md
```

## Dependencies

None. This project uses only the Python Standard Library.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
