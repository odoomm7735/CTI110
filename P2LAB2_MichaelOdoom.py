# Michael Odoom
# June 27, 2024
# P2LAB2
"""Program that creates a dictionary where the key and value pairs"""

# Create dictionary
cars = {"Camaro" : 18.21,"Prius" : 52.36, "Model S" : 110, "Silverado": 26}

# Display keys
keys = cars.keys()
print(keys)
print()

# get input from user
car_input = input("Enter a vehicle to see its mpg: ")
print()

# Get the mpg associated with the vehicle
mpg_output = cars[car_input]
print(f"The {car_input} gets {mpg_output} mpg.\n")
# get the distance
distance = float(input(f"How many miles will you drive the {car_input}?"))
print()

# Calculate gallons of gas needed
gallons = distance/ mpg_output
# print gallons needed to drive the car
print(f'{gallons:.2f} gallon(s) of gas needed to drive the {car_input} {distance} miles.')