# ------------ Conditional Basics ------------
# 1. Prompt the user for a day of the week, print out whether the day is Monday or not
day_input = input("What is today? (Saturday, Sunday, Monday, ...): ")
if day_input == "Monday":
    print("Today is Monday: True")
else:
    print("Today is Monday: False")

# 2. Prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day_input = input("What is today? (Saturday, Sunday, Monday, ...): ")
if day_input == "Saturday" or day_input == "Sunday":
    print("It's the weekend: True")
else:
    print("It's the weekend: False")

# 3. Create variables and make up values for: 
# - The number of hours worked in one week
# - The hourly rate
# - How much the week's paycheck will be
# Write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours
hrs = 40
rate = 12
if hrs > 40:
    pay_for_week = hrs * rate * 1.5
else:
    pay_for_week = hrs * rate
print("Amount earned this week:", pay_for_week)

# ------------ While ------------
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i < 100:
    i += 2
    print(i)

# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i > -10:
    i -= 5
    print(i)

# Create a while loop that starts at 2, and 
# displays the number squared on each line while the number is less than 1,000,000. 
i = 2
while i < 1000000:
    i = i ** 2
    if i > 1000000:
        break
    print(i)

# Write a loop that uses print to create the output: 100, 95, 90, 85, ... 15, 10, 5
i = 100
while i > 0:
    print(i)
    i -= 5

# ------------ For Loops ------------
# Write some code that prompts the user for a number, then 
# shows a multiplication table up through 10 for that number.
number = input("Enter a number for the multiplication table: ")
i = 0
for i in range(0,10):
    i += 1
    print(str(number), "*", str(i), "=", str(int(number) * int(i)))

# Create a for loop that uses print to create the output: 1 22 333 4444 ... 999999999
i = 1
for i in range(1,10):
    print(str(i) * int(i))

# ------------ break and continue ------------
# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for 
# the number the user entered.
number = 0
while number == number:
    number = int(input("Enter an odd number between 1 and 50: "))
    if number >= 1 and number <= 50 and number % 2 == 1:
        print('nice')
        break

i = 1
while i < 50:
    if i == number:
        print("Yikes! Skipping number:", number)
        i += 2
        continue
    print("Here is an odd number:", i)
    i += 2

# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also 
# note that the input function returns a string, so you'll need to convert this to a numeric type.)

# Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

# Display a table of powers.
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.