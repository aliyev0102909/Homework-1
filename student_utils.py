def calculate_average(scores):
    """Return the average score."""
    return sum(scores) / len(scores) if scores else 0.0


def get_highest_score(scores):
    """Return the highest score in the list."""
    return max(scores)


def get_lowest_score(scores):
    """Return the lowest score in the list."""
    return min(scores)


def process_students(student_list):
    """Display each student name and the total number of students."""
    print("Students:")
    for student in student_list:
        print(student)
    print(f"Total Students: {len(student_list)}")


def register_students(*students):
    """Display any number of registered student names and their total."""
    print("Registered Students:")
    for student in students:
        print(student)
    print(f"Total: {len(students)}")
