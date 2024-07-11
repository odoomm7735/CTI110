# P4LAB2_OdoomMichael.py
# July 11, 2024
""" This program asks the user for an integer, displays the multiplication table if the integer 
is zero or higher, and handles the case where the integer is negative. It also allows the 
# user to run the program again based on their input. The code utilizes both a for loop and a while loop."""

def display_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

def main():
    while True:
        try:
            user_input = int(input("Enter an integer: "))
            
            if user_input < 0:
                print("This program cannot accept negative values.")
            else:
                display_multiplication_table(user_input)
            
            run_again = input("Do you wish to run the program again? (yes/no): ").strip().lower()
            if run_again != "yes":
                break
        
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
