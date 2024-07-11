# Michael Odoom
# July 9, 2024
# P4HW2_OdoomMichael
# This program calculates the gross pay for multiple employees, including
# totals for regular pay, overtime pay, and the total gross pay for all employees.

# Pseudocode
"""
1. Display program title and description
2. Initialize variables to store totals:
   - total_overtime_pay
   - total_regular_pay
   - total_gross_pay
   - employee_count
3. Start a loop to collect employee information:
   a. Ask user to enter employee's name or "Done" to terminate
   b. If user enters "Done", break the loop
   c. Otherwise, ask for employee's pay rate and hours worked
   d. Calculate overtime pay and regular pay:
      i. If hours worked > 40:
         - Calculate regular pay for 40 hours
         - Calculate overtime pay for hours above 40 (1.5 times the pay rate)
      ii. If hours worked <= 40:
         - Calculate regular pay for all hours
         - Overtime pay is 0
   e. Calculate gross pay (regular pay + overtime pay)
   f. Add values to totals:
      - Add to total_overtime_pay
      - Add to total_regular_pay
      - Add to total_gross_pay
      - Increment employee_count by 1
4. After loop ends, display totals:
   - Total number of employees entered
   - Total amount paid for overtime
   - Total amount paid for regular pay
   - Total gross pay for all employees
"""

def main():
    # Initialize variables to store totals
    total_overtime_pay = 0.0
    total_regular_pay = 0.0
    total_gross_pay = 0.0
    employee_count = 0

    while True:
        # Ask for employee name
        employee_name = input("Enter employee's name or 'Done' to terminate: ")

        if employee_name.lower() == 'done':
            break

        # Ask for pay rate and hours worked
        pay_rate = float(input(f"Enter pay rate for {employee_name}: "))
        hours_worked = float(input(f"Enter number of hours worked by {employee_name}: "))

        # Calculate overtime pay and regular pay
        if hours_worked > 40:
            regular_pay = 40 * pay_rate
            overtime_pay = (hours_worked - 40) * (pay_rate * 1.5)
        else:
            regular_pay = hours_worked * pay_rate
            overtime_pay = 0

        # Calculate gross pay
        gross_pay = regular_pay + overtime_pay

        # Add to totals
        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay
        employee_count += 1

        # Display individual employee's pay details
        print(f"\nPay details for {employee_name}:")
        print(f"Regular Pay: ${regular_pay:.2f}")
        print(f"Overtime Pay: ${overtime_pay:.2f}")
        print(f"Gross Pay: ${gross_pay:.2f}\n")

    # Display totals
    print(f"\nTotal number of employees entered: {employee_count}")
    print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
    print(f"Total amount paid for regular pay: ${total_regular_pay:.2f}")
    print(f"Total gross pay for all employees: ${total_gross_pay:.2f}")

if __name__ == "__main__":
    main()
