# Write some Python code, that is, variables and operators, to describe the following scenarios.

# 1. You have rented some movies for your kids: 
# The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), and 
# Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?
price_per_day = 3
mermaid_days = 3 # could ask user "add movie? y/n: " with input, then ask "rented for how many days? enter number: " to gather days_rented
bear_days = 5
hercules_days = 1
days_rented = mermaid_days + bear_days + hercules_days
cost = days_rented * price_per_day
print(cost);

# 2. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
g_pay = 400 # can ask user "worked for another company? y/n: " then ask user "pay per hour" and "how many hours"
a_pay = 380
fb_pay = 350
fb_hrs = 10
g_hrs = 6
a_hrs = 4
total_pay = (g_pay * g_hrs) + (a_pay * a_hrs) + (fb_pay * fb_hrs) # can use [(c1_pay, c1_hrs), (c2_pay, c2_hrs), ...] and then list[0][0] * list[1][1] for x in list[x]
print(total_pay);

# 3. A student can be enrolled to a class only if the class is not full and 
# the class schedule does not conflict with her current schedule.
def enroll_status(full, conflict):
    return not full and not conflict
full = False # can ask user "is the class full" and "is there a schedule conflict"
conflict = False
eligible = str(enroll_status(full, conflict))
print("Student can enroll: " + eligible);

# 4. A product offer can be applied only if people buys more than 2 items, and 
# the offer has not expired. Premium members do not need to buy a specific amount of products.
def eligible(count, still_good, premium):
    return still_good and (count > 2 or premium)
count = 5 # can ask user "how many items" and use other criteria to determine eligibility
still_good = True
premium = False
check_eligible = str(eligible(count, still_good, premium))
print("Offer is available: " + check_eligible)

# 5. Use the following code to follow the instructions below:
# username = 'codeup'
# password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace
username = 'codeup'
password = 'notastrongpassword'
pass_len_at_least_5 = len(password) >= 5
name_len_at_most_20 = len(username) <= 20
name_not_same_as_pass = username != password
not_start_with_space = username.strip() == username and password.strip() == password
# print(str(pass_len_at_least_5), str(name_len_at_most_20), str(name_not_same_as_pass), str(not_start_with_space))
# print(username, password)