# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())

# Exercise 0 - print the list of fruits for comparison to following string changes
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
print(fruits)

# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
uppercased_fruits = []
for fruit in fruits:
    uppercased_fruits.append(fruit.upper())
print("Uppercased Fruits:\n", uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
capitalized_fruits = []
for fruit in fruits:
    if ' ' in fruit:
        capitalized_words = []
        fruit_words = fruit.split(' ')
        for word in fruit_words:
            letters = list(word)
            letters[0] = letters[0].upper()
            word = ''.join(letters)
            capitalized_words.append(word)
        fruit = ' '.join(capitalized_words)
        capitalized_fruits.append(fruit)
    else: capitalized_fruits.append(fruit.capitalize())
print("Capitalized Fruits:\n", capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_with_more_than_two_vowels = []
fruit_test = []
for fruit in fruits:
    fruit_test.append(fruit)
fruit_test.append('test')
for fruit in fruit_test:
    n = 0
    fruit_lower = fruit.lower()
    for char in fruit_lower:
        if char in 'aeiou':
            n += 1
    if n >= 2:
        fruits_with_more_than_two_vowels.append(fruit)
print("Fruits with more than two vowels:\n", fruits_with_more_than_two_vowels)

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_with_only_two_vowels = []
for fruit in fruits:
    n = 0
    fruit_lower = fruit.lower()
    for char in fruit_lower:
        if char in 'aeiou':
            n += 1
    if n == 2:
        fruits_with_only_two_vowels.append(fruit)
print("Fruits with only two vowels:\n", fruits_with_only_two_vowels)

# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
more_than_5 = []
for fruit in fruits:
    if len(fruit) > 5:
        more_than_5.append(fruit)
print("Fruits with more than 5 letters:\n", more_than_5)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
exactly_5 = []
for fruit in fruits:
    if len(fruit) == 5:
        exactly_5.append(fruit)
print("Fruits with exactly 5 letters:\n", exactly_5)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
less_than_5 = []
for fruit in fruits:
    if len(fruit) < 5:
        less_than_5.append(fruit)
print("Fruits with less than 5 letters:\n", less_than_5)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruit_len = []
for fruit in fruits:
    fruit_len.append(len(fruit))
print("Fruit character lengths:\n", fruit_len)


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
contains_a = []
for fruit in fruits:
    if 'a' in fruit.lower():
        contains_a.append(fruit)
print("Fruits containing 'a':\n", contains_a)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print("Even numbers:\n", even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
odd_numbers = []
for number in numbers:
    if number % 2 == 1:
        odd_numbers.append(number)
print("Odd numbers:\n", odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
positive_numbers = []
for number in numbers:
    if number > 0:
        positive_numbers.append(number)
print("Positive numbers:\n", positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
negative_numbers = []
for number in numbers:
    if number < 0:
        negative_numbers.append(number)
print("Negative numbers:\n", negative_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
two_or_more_numerals = [number for number in numbers if len(str(number)) >= 2]
print("Numbers with two or more digits:\n", two_or_more_numerals)

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
numbers_squared = [number ** 2 for number in numbers]
print("Numbers squared:\n", numbers_squared)

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
odd_negative_numbers = [number for number in numbers if number < 0 if number % 2 == 1]
print("Odd negative numbers:\n", odd_negative_numbers)

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
numbers_plus_5 = [number + 5 for number in numbers]
print("Numbers + 5:\n", numbers_plus_5)

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
primes = []
for number in numbers:
    if number > 1:
        for n in range(2, number):
            if number % n == 0:
                primes.append(number)
                break
print("Prime numbers:\n", primes)