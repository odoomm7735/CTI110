# Michael Odoom
# July 11, 2014
# P4HW1_OdoomMichael
# This program collects a number of test scores from the user, drops the lowest score,
# calculates the average of the remaining scores, and determines the letter grade.

# Pseudocode
'''1. Display program title and description
   2. Ask user to enter the number of scores they would like to input
   3. Initialize an empty list to store the scores
   4. Create a loop to collect the number of scores specified by the user
    a. Inside the loop, ask the user to enter a score
    b. Validate the score to ensure it is between 0 and 100
    c. If the score is not valid, notify the user and ask for a valid score again
    d. If the score is valid, add it to the list
   5. After collecting all the scores:
    a. Display the lowest score entered
    b. Remove the lowest score from the list
    c. Display the remaining scores
    d. Calculate the average of the remaining scores
    e. Determine the letter grade for the calculated average
   6. Display the average score and the letter grade'''


# Function to determine the letter grade
def determine_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    # Ask user for the number of scores to enter
    num_scores = int(input("Enter the number of scores you would like to enter: "))
    
    # Initialize list to store scores
    scores = []

    # Collect scores
    for i in range(num_scores):
        while True:
            try:
                score = float(input(f"Enter score {i + 1}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Invalid score. Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 100.")
    
    # Display the lowest score
    lowest_score = min(scores)
    print(f"\nLowest score: {lowest_score}")

    # Remove the lowest score and display the modified score list
    scores.remove(lowest_score)
    print(f"Modified score list after dropping the lowest score: {scores}")

    # Calculate and display the average of the remaining scores
    average_score = sum(scores) / len(scores)
    print(f"Average score: {average_score:.2f}")

    # Determine and display the letter grade
    letter_grade = determine_letter_grade(average_score)
    print(f"Letter grade: {letter_grade}")

if __name__ == "__main__":
    main()
