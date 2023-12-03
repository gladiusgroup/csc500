# python 3.6 script to set an alarm time based on the 24-hour clock

def calculate_alarm_time():
    try:
        #Get current time
        current_time = int(input("Enter the current 24-hour clock time in hours and whole numbers (0-23): "))
        
        #Users...
        if current_time < 0 or current_time > 23:
            print("There are only 24 hours in a day. Enter between 0 ans 23 in whole numbers.")
            return

        #Get alarm wait time
        wait_time = int(input("Enter the number of hours to wait for the alarm in whole numbers: "))
        
        #Users again...
        if wait_time < 0:
            print("Can't go back in time, please enter positive whole number to indicate how many hours to wait for the alarm.")
            return

        #Calculate future time for alarm
        alarm_time = (current_time + wait_time) % 24

        #Show the user the alarm time
        print(f"The alarm will go off at {alarm_time:02d}:00.")

    except ValueError:
        print("Please enter valid, whole numbers (0-23).")

def main():
    calculate_alarm_time()

if __name__ == "__main__":
    main()
