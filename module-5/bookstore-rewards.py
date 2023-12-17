# Bookstore Calculator
def calculate_points(books):
    #Calculate the points awarded based on the number of books purchased.
    if 0 <= books <= 1:
        return 0
    elif 2 <= books <= 3:
        return 5
    elif 4 <= books <= 5:
        return 15
    elif 6 <= books <= 7:
        return 30
    elif books >= 8:
        return 60

def main():
    # Prompt the user for the number of books
    books_purchased = input("Enter the number of books you've purchased this month: ")
    
    # Validate input
    while not books_purchased.isdigit() or int(books_purchased) < 0:
        print("Please enter a valid non-negative integer.")
        books_purchased = input("Enter the number of books you've purchased this month: ")

    books_purchased = int(books_purchased)

    # Calculate points
    points = calculate_points(books_purchased)

    # Display the points awarded
    print(f"You have earned {points} points for purchasing {books_purchased} book(s) this month.")

    # Display the points table
    print("\nFor future reference, here is the Points Table:")
    print("Books Purchased | Points Earned")
    print("0-1             | 0")
    print("2-3             | 5")
    print("4-5             | 15")
    print("6-7             | 30")
    print("8 or more       | 60\n")

if __name__ == "__main__":
    main()
