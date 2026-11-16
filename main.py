from student_utils import (
    calculate_average,
    get_highest_score,
    get_lowest_score,
    process_students,
    register_students,
)


def main():
    """Run the Student Management System."""
    students = ["Ali", "Leyla", "Kamran", "Aysel"]
    scores = [78, 91, 85, 67, 95, 88]

    print(f"Average Score: {calculate_average(scores)}")
    print(f"Highest Score: {get_highest_score(scores)}")
    print(f"Lowest Score: {get_lowest_score(scores)}")
    print()

    process_students(students)
    print()

    register_students("Ali", "Leyla", "Kamran")


if __name__ == "__main__":
    main()
