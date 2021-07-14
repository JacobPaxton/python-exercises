# Use from to import the calculate_tip function directly. 
# Call this function with values you choose and print the result.
import function_exercises
print(function_exercises.calculate_tip(.1, 100))

# Read about and use the itertools module from the python standard library to 
# help you solve the following problems:
# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
# How many different combinations are there of 2 letters from "abcd"?
# How many different permutations are there of 2 letters from "abcd"?
from itertools import chain, combinations, permutations
print("".join(list(chain('abc', '1', '2', '3')))) # First way to join 'abc' to '1', '2', '3'
print("".join(list(chain.from_iterable(['abc', '1', '2', '3'])))) # Second way to join 'abc' to '1', '2', '3'
print(len(list(combinations("abcd", 2))))
print(len(list(permutations("abcd", 2))))

# Use the load function from the json module to open <this> file.
import json
jfile = json.load(open('profiles.json'))

# Your code should produce a list of dictionaries. 
# Using this data, write some code that calculates and outputs the following information:
# Total number of users
print("---Total number of users:---")
print(len(jfile))

# Number of active users
print("---Number of active users:---")
active_user_count = 0
for user in jfile:
    if user["isActive"] == True:
        active_user_count += 1
print(active_user_count)

# Number of inactive users
print("---Number of inactive users:---")
print(len(jfile) - active_user_count)

# Grand total of balances for all users
print("---Grand total of balances for all users:---")
total_balance = 0
for user in jfile:
    balance_w_commas = user["balance"][1:]
    balance = balance_w_commas.replace(",", "")
    total_balance += float(balance)
print(total_balance)

# Average balance per user
print("---Average balance per user:---")
print(round(total_balance / len(jfile), 2))

# User with the lowest balance
print("---User with lowest balance:---")
user_balance_list_raw = []
balance_list = []
for user in jfile:
    user_balance_list_raw.append(user["balance"])
for balance in user_balance_list_raw:
    balance_w_commas = balance[1:]
    balance = balance_w_commas.replace(",", "")
    balance_list.append(balance)
min_balance = min(balance_list)
min_index = balance_list.index(min_balance)
min_balance_user = jfile[min_index]["name"]
print(min_balance_user)

# User with the highest balance
print("---User with highest balance:---")
user_balance_list_raw = []
balance_list = []
for user in jfile:
    user_balance_list_raw.append(user["balance"])
for balance in user_balance_list_raw:
    balance_w_commas = balance[1:]
    balance = balance_w_commas.replace(",", "")
    balance_list.append(balance)
max_balance = max(balance_list)
max_index = balance_list.index(max_balance)
max_balance_user = jfile[max_index]["name"]
print(max_balance_user)

# Most common favorite fruit
print("---Most common favorite fruit:---")
fruit_iter_dict = {}
for user in jfile:
    if user["favoriteFruit"] not in fruit_iter_dict.keys():
        fruit_iter_dict[user["favoriteFruit"]] = 0
    fruit_iter_dict[user["favoriteFruit"]] += 1

fruit_list = list(fruit_iter_dict.keys())
fruit_nums = list(fruit_iter_dict.values())

most_common_fruit_num = max(fruit_nums)
most_common_fruit_index = fruit_nums.index(most_common_fruit_num)
most_common_fruit = fruit_list[most_common_fruit_index]

print(most_common_fruit)

# Least most common favorite fruit
print("---Least common favorite fruit:---")
fruit_iter_dict = {}
for user in jfile:
    if user["favoriteFruit"] not in fruit_iter_dict.keys():
        fruit_iter_dict[user["favoriteFruit"]] = 0
    fruit_iter_dict[user["favoriteFruit"]] += 1
fruit_list = list(fruit_iter_dict.keys())
fruit_nums = list(fruit_iter_dict.values())
least_common_fruit_num = min(fruit_nums)
least_common_fruit_index = fruit_nums.index(least_common_fruit_num)
least_common_fruit = fruit_list[least_common_fruit_index]
print(least_common_fruit)

# Total number of unread messages for all users
print("---Total number of unread messages for all users:---")
total_unread_messages = 0
for user in jfile:
    unread_message_count = ""
    for char in user["greeting"]:
        if char.isnumeric() == True:
            unread_message_count += char
    total_unread_messages += int(unread_message_count)
print(total_unread_messages)