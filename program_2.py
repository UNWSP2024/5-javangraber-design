# Programmer: Javan Graber
# Date: 2/19/2026
# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#   247

# + 129

# ------

# The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect a message showing the correct answer should be displayed.
# The program must use a function that accomplishes part of the needed tasks.


# Generate the two random numbers to be added
import random
number1 = random.randint(1, 1000)
number2 = random.randint(1, 1000)

# Print the two numbers and a line in a nice pattern
print(f'   {number1}')
print(f'+  {number2}')
print('---------')

# Create a function that finds the total
def find_total ():
    total = number1 + number2
    return total

# Run this function and assign the total
total = find_total()

# Create a function that asks for the answer and checks it
def ask_answer_and_check (total):
    answer = int(input(f'Enter the sum of the two numbers (no commas needed): '))
    if answer == total:
        print('Congratulations! You are correct!')
    else:
        print(f'Sorry, you are incorrect. The correct answer is {total:,}')

# Run the second function
ask_answer_and_check(total)
