# Michael Odoom
# July 3, 2024
# P3HW2
# Assignment Name: Employee Salary Calculation
# This program calculates the gross pay for an employee based on their working hours, pay rate, and any applicable overtime. 

# Pseudocode:
# 1. Ask the user to enter the name of the employee.
# 2. Ask the user to enter the number of hours the employee worked this week.
# 3. Ask the user to enter the employee's pay rate.
# 4. Evaluate if the employee has worked overtime (more than 40 hours).
#    - If yes, calculate the amount owed to the employee for overtime hours.
# 5. Calculate the amount the employee should be paid for regular hours worked.
# 6. Display the following:
#    - Employee name
#    - Pay rate
#    - Number of hours worked
#    - Overtime hours
#    - Overtime pay
#    - Pay for regular hours
#    - Gross pay

# Program code:

# Step 1: Ask the user to enter the name of the employee.
employee_name = input("Enter the name of the employee: ")

# Step 2: Ask the user to enter the number of hours the employee worked this week.
hours_worked = float(input("Enter the number of hours the employee worked this week: "))

# Step 3: Ask the user to enter the employee's pay rate.
pay_rate = float(input("Enter the employee's pay rate: "))

# Initialize variables for overtime calculation
overtime_hours = 0
overtime_pay = 0

# Step 4: Evaluate if the employee has worked overtime (more than 40 hours).
if hours_worked > 40:
    # Calculate overtime hours
    overtime_hours = hours_worked - 40
    # Calculate overtime pay (1.5 times the regular pay rate)
    overtime_pay = overtime_hours * pay_rate * 1.5
    # Regular pay for 40 hours
    regular_pay = 40 * pay_rate
else:
    # No overtime
    regular_pay = hours_worked * pay_rate

# Step 5: Calculate the gross pay
gross_pay = regular_pay + overtime_pay

# Step 6: Display the results
print("\nEmployee name:", employee_name)
print("Pay rate: ${:.2f}".format(pay_rate))
print("Number of hours worked:", hours_worked)

print("Overtime hours:", overtime_hours)
print("Overtime pay: ${:.2f}".format(overtime_pay))
print("------------------------------")
print("Employee name:", employee_name)
print("Pay for regular hours: ${:.2f}".format(regular_pay))
print("Gross pay: ${:.2f}".format(gross_pay))
