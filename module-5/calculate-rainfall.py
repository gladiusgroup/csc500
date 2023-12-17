# Calculate the average rainfall over a period of years
def main():
    # Initialize total rainfall and month count
    total_rainfall = 0
    total_months = 0

    # User input validation for years
    years = input("Enter the number of years: ")
    while not years.isdigit() or int(years) <= 0:
        print("Please enter a positive integer for the number of years.")
        years = input("Enter the number of years: ")
    years = int(years)

    # Outer loop for each year
    for year in range(1, years + 1):
        print(f"\nYear {year}:")
        # Inner loop for each month
        for month in range(1, 13):
            # Input validation for rainfall input
            rainfall = input(f"Enter the rainfall for month {month} (in inches): ")
            while not rainfall.replace('.', '', 1).isdigit() or float(rainfall) < 0:
                print("Invalid input. Please enter a non-negative number.")
                rainfall = input(f"  Enter the rainfall for month {month} (in inches): ")
            rainfall = float(rainfall)

            # Add to total rainfall and increment month count
            total_rainfall += rainfall
            total_months += 1

    # Calculate average rainfall
    average_rainfall = total_rainfall / total_months

    # Display results
    print("\nRainfall Statistics:")
    print(f"  Total number of months: {total_months}")
    print(f"  Total inches of rainfall: {total_rainfall:.2f}")
    print(f"  Average rainfall per month: {average_rainfall:.2f} inches")

if __name__ == "__main__":
    main()
