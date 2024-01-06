# Course Information App
# Function to print course details
def print_course_details(course, course_rooms, course_instructors, course_times):
    print(f"Course Number: {course}")
    print(f"Room Number: {course_rooms[course]}")
    print(f"Instructor: {course_instructors[course]}")
    print(f"Meeting Time: {course_times[course]}")

def format_course_input(course_input):
    """Formats the course input by converting to uppercase and removing whitespace."""
    formatted_input = ''.join(course_input.split())  # Remove whitespace
    if formatted_input.isalnum():
        return formatted_input.upper()
    else:
        print("Invalid input. Please enter only letters and numbers.")
        return None

def main():
    # Setup dictionaries containing course details
    course_rooms = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }

    course_instructors = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

    course_times = {
        "CSC101": "8:00 A.M.",
        "CSC102": "9:00 A.M.",
        "CSC103": "10:00 A.M.",
        "NET110": "11:00 A.M.",
        "COM241": "1:00 P.M."
    }

    print("Welcome to the Course Information App.\n")
    print("This program will display the room number, instructor, and meeting time for a given course.\n")
    print("Type exit at any time to quit.\n")

    while True:
        # Collect user input
        course = input("Enter a course number (e.g., CSC101) or type 'exit' to quit: ")
        if course.lower() == 'exit':
            print("Have a good one! Exiting program.")
            break

        course = format_course_input(course)

        # Check if course is None and prompt to try again
        if course is None:
            print("Invalid input. Please try again.")
            continue

        # Validation and Output
        if course in course_rooms:
            print_course_details(course, course_rooms, course_instructors, course_times)
            continue
        else:
            print("Course not found. Please enter a valid course number.")


if __name__ == "__main__":
    main()
