# Michael Odoom
# July 14th, 2024
# P5HW
# This program simulates a math quiz with addition and subtraction. The user
# can choose to solve either type of problem and will receive feedback on their
# guesses until they answer correctly. The program keeps track of the number of
# guesses and displays a menu for further actions.

import random

def generate_numbers():
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
    return num1, num2

def addition_quiz():
    num1, num2 = generate_numbers()
    answer = num1 + num2
    print(f"{num1}\n+ {num2}")
    attempts = 0

    while True:
        user_answer = int(input("Enter your answer: "))
        attempts += 1
        if user_answer < answer:
            print("Too low. Try again.")
        elif user_answer > answer:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You got it right in {attempts} attempts.")
            break

def subtraction_quiz():
    num1, num2 = generate_numbers()
    answer = num1 - num2
    print(f"{num1}\n- {num2}")
    attempts = 0

    while True:
        user_answer = int(input("Enter your answer: "))
        attempts += 1
        if user_answer < answer:
            print("Too low. Try again.")
        elif user_answer > answer:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You got it right in {attempts} attempts.")
            break

def main():
    while True:
        print("Welcome to Math Quiz")
        print("1. Addition Quiz")
        print("2. Subtraction Quiz")
        print("3. Exit")
        choice = input("Please choose an option: ")

        if choice == '1':
            addition_quiz()
        elif choice == '2':
            subtraction_quiz()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
