# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(x):
    # Return True if argument is int or float and equal to two
    if type(x) == int or type(x) == float:
        return x == 2
    # Return True if argument is str and equal to two
    if type(x) == str:
        return x.lower() == 'two'
    # Print error message and return False if argument not int, float, or str type
    print("Error: value not int, float, or str type")
    return False

# print(is_two(2))
# print(is_two(3))
# print(is_two("two"))


# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(x):
    # Return True if argument is str and in vowel list
    if type(x) == str:
        return x.lower() in ('aeiou')
    # Print error message and return False if argument not str type
    print("Error: value not str type")
    return False

# print(is_vowel("a"))
# print(is_vowel("E"))
# print(is_vowel("b"))
# print(is_vowel(2))


# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(x):
    # Return True if argument is str and in consonant list
    if type(x) == str:
        return x.lower() in ('bcdfghjklmnpqrstvwxyz')
    # Print error message if argument not str type
    print("Error: value not str type")
    return False

# print(is_consonant("a"))
# print(is_consonant("E"))
# print(is_consonant("b"))
# print(is_consonant(2))


# Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def cap_word(x):
    # Return capitalized string
    if type(x) == str:
        if x[0] not in 'aeiou':
            x = x.capitalize()
        return x
    print("Error: value not str type")

# print(cap_word("aeiou"))
# print(cap_word("enus"))
# print(cap_word("bill"))
# print(cap_word(2))


# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(percent, cost):
    # Check if percent is float between 0 and 1
    if type(percent) == float:
        if percent > 0.0 and percent < 1.0:
            # Also check if cost is float or int
            if type(cost) == float or type(cost) == int:
                # Return tip amount
                return round(percent * cost, 2)
            # Print error message if cost not numeric
            else:
                print("Error: cost must be numeric")
        # Print error message if percent not between 0 and 1
        else:
            print("Error: Tip percentage must be in decimal form (0.15, 0.2, etc)")
    # Print error message if percent not float
    else:
        print("Error: Tip percentage must be in decimal form (0.15, 0.2, etc)")
    
# calculate_tip(0.15, 100)
# calculate_tip(0.5, "hundred")
# calculate_tip(15, 100)
# calculate_tip("fifteen", 100)


# Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(cost, discount_percentage):
    # Return discounted cost
    return cost - (discount_percentage * cost)

# print(apply_discount(100, .15))


# Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(x):
    # Delete commas from string
    return x.replace(",", "")

# print(handle_commas("1,000,000"))


# Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(x):
    # Try to turn potential float type into int, print error if not float or int
    try: 
        x = int(x)
    except:
        print("Value NaN")
        return None
    # Return letter grade
    if x >= 88:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 67:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'F'

# print(get_letter_grade(91))


# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(x):
    # Make new list for all letters not in vowel list
    unvoweled_list = [letter for letter in x if letter not in 'aeiou']
    # Return joined list
    return "".join(unvoweled_list)

# print(remove_vowels("Hello"))


# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed
def normalize_name(x):
    # Check if argument is str type
    if type(x) == str:
        # Convert to lowercase
        x = x.lower()
        # Convert each non-alphanumeric (each python identifier) value to " "
        for char in x:          
            if char.isnumeric() == False and char.isalpha() == False:
                x = x.replace(char, " ") 
        # Delete whitespace at start and end of string
        x = x.strip()
        # Replace remaining spaces with underscores
        x = x.replace(" ", "_")
        # Move leading numbers to back of string
        while x[0].isnumeric():
            x += x[0]
            x = x[1:]
        # Return normalized string
        return x
    # Print error message if argument is not str type
    else:
        return "not a string"
# print(normalize_name("%1Try me"))

# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
def cumulative_sum(list_of_nums):
    # Set initial values
    running_total = 0
    cumulative_list_of_nums = []
    # Progressively add each value
    for num in list_of_nums:
        running_total += num
        cumulative_list_of_nums.append(running_total)
    # Return cumulative list
    return cumulative_list_of_nums

# print(cumulative_sum([1, 5, 100, 1000]))


# Additional Exercise
# Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.

# Bonus
# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. 
def twelveto24(time):
    # Delete colon from time string
    time = time.replace(":", "")
    # Handle times after noon
    if "pm" in time:
        # Remove 'pm' from time
        time = time[:-2]
        # Change all pm times not in the 12th hour
        if int(time) < 1200:
            # Add 1200 hours
            time = str(int(time) + 1200)
    # Handle times before noon
    else:
        # Remove 'am' from time
        time = time[:-2]
        # Add a leading '0' to times before the 10th hour
        if int(time) < 1000:
            time = "0" + time
    return time

# print(twelveto24("8:45am"))
# print(twelveto24("11:45am"))
# print(twelveto24("12:45pm"))
# print(twelveto24("1:45pm"))


# Bonus: write a function that does the opposite.
def backtotwelve(time):
    # Add colon into 4-digit-long 24hr time
    time = time[0:2] + ':' + time[2:4]
    # Handle times before 1000
    if time[0] == '0':
        time = time[1:] + 'am'
    # Handle times at 1300 and later
    elif int(time[0:2]) >= 13:
        time = str(int(time[0:2]) - 12) + time[2:] + 'pm'
    # Handle 1200 - 1259
    elif int(time[0:2]) >= 12:
        time = time + 'pm'
    # Handle 1000 - 1159
    else:
        time = time + 'am'
    # Return standardized time
    return time

# print(backtotwelve("0845"))
# print(backtotwelve("1145"))
# print(backtotwelve("1245"))
# print(backtotwelve("1345"))


# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27