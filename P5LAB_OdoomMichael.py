# Michael Odoom
# July 14, 2024
# P5LAB
# This program simulates a customer using a self-checkout machine. It generates a random
# float value as the total owed for the purchase. The user is prompted to enter the amount
# of money they will put into the self-checkout machine (as a float). The program then displays
# the amount of dollars, quarters, dimes, nickels, and pennies required to make the change.

import random

def disperse_change(change):
    dollars = int(change)
    change = (change - dollars) * 100
    quarters = int(change // 25)
    change %= 25
    dimes = int(change // 10)
    change %= 10
    nickels = int(change // 5)
    change %= 5
    pennies = int(change)
    
    print("Change to be returned:")
    print(f"Dollars: {dollars}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")

def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total owed: ${total_owed}")
    
    amount_paid = float(input("Enter the amount of cash you will put into the self-checkout: "))
    
    if amount_paid < total_owed:
        print("The amount paid is less than the total owed. Please pay the full amount.")
        return
    
    change_owed = amount_paid - total_owed
    print(f"Change owed: ${change_owed:.2f}")
    
    disperse_change(change_owed)

if __name__ == "__main__":
    main()
