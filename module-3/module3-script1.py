# python 3.6 script to calculate costs associated with a restaraunt meal

def calculate_total_meal_cost():
    try:
        #Get the cost of the meal
        meal_cost = float(input("Enter the cost of the meal before tax and tip: $"))

        if meal_cost < 0:
            print("Negative meal cost? Please enter a positive number.")
            return

        tip = meal_cost * 0.18  # 18% tip
        tax = meal_cost * 0.07  # 7% tax

        total_cost = meal_cost + tip + tax

        #Display the associated cost results
        print(f"Base Cost: ${meal_cost:.2f}")
        print(f"Tip (18%): ${tip:.2f}")
        print(f"Tax (7%): ${tax:.2f}")
        print(f"Total Cost: ${total_cost:.2f}")

    except ValueError:
        print("Please enter a valid number for the meal cost.")

def main():
    calculate_total_meal_cost()

if __name__ == "__main__":
    main()
