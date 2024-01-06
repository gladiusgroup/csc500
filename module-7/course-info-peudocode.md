# Course Information App

## Function: print_course_details

- Inputs: 
  - Prints the details of the specified course including room number, instructor, and meeting time
  - course: String
  - course_rooms: Dictionary
  - course_instructors: Dictionary
  - course_times: Dictionary

## Function: format_course_input

- Inputs:
  - course_input: String
- Removes whitespace
- Converts to uppercase
- Validates that the input is alphanumeric
- Return the formatted input or None

## Function: main

- Initialize initial dictionaries:
  -- course rooms
  -- instructors
  -- times
- Welcome user
- Loop:
  - Prompt for course number or an exit
  - Call format_course_input on imput
  - Checks if the course exists in the dictionaries
  - If exists, call print_course_details
  - If not exist, tell the user and try again

## Execution Flow

- Call `main` function when the script is executed.
