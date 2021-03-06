# The following questions reference the students data structure below. Write the python code to answer the following questions:
students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]

# 1. How many students are there?
print("--------1. How many students are there?--------")
print(f"There are {len(students)} students.")

# 2. How many students prefer light coffee? For each type of coffee roast?
print("--------2. How many students prefer light coffee? For each type of coffee roast?--------")
num_students_prefer_light = 0
for student in students:
    if student["coffee_preference"] == "light":
        num_students_prefer_light += 1
print(num_students_prefer_light, "students prefer light coffee.")

# 3. How many types of each pet are there?
print("--------3. How many types of each pet are there?--------")
pet_types = []
for student in students:
    for pet in student["pets"]:
        if pet["species"] not in pet_types:
            pet_types.append(pet["species"])
pet_type_string = ", ".join(pet_types)
print(f"The students have {len(pet_types)} pet types:", pet_type_string)

# 4. How many grades does each student have? Do they all have the same number of grades?
print("--------4. How many grades does each student have? Do they all have the same number of grades?--------")
student_iteration = 0
same_grades = True
for student in students:
    number_of_grades = 0
    for grade in student["grades"]:
        number_of_grades += 1
    if student_iteration == 0:
        gradecount = number_of_grades
    if number_of_grades != gradecount:
        gradecount = "a disimilar amount of"
        same_grades = False
    student_iteration += 1
print(f"Students have {gradecount} grades. They have the same amount of grades: {str(same_grades)}")

# 5. What is each student's grade average?
print("--------5. What is each student's grade average?--------")
for student in students:
    grades_added_together = 0
    num_of_grades = len(student["grades"])
    for grade in student["grades"]:
        grades_added_together += grade
    grade_average = grades_added_together / num_of_grades
    print(student["student"], "has an average grade of", grade_average)

# 6. How many pets does each student have?
print("--------6. How many pets does each student have?--------")
for student in students:
    number_of_pets = 0
    for pet in student["pets"]:
        number_of_pets += 1
    if number_of_pets == 1:
        print(student["student"], "has", number_of_pets, "pet.")
    else:
        print(student["student"], "has", number_of_pets, "pets.")

# 7. How many students are in web development? data science?
print("--------7. How many students are in web development? data science?--------")
number_of_webdev_students = 0
number_of_ds_students = 0
for student in students:
    if student["course"] == "web development":
        number_of_webdev_students += 1
    if student["course"] == "data science":
        number_of_ds_students += 1
print(f"There are {str(number_of_webdev_students)} web development students and {str(number_of_ds_students)} data science students.")

# 8. What is the average number of pets for students in web development?
print("--------8. What is the average number of pets for students in web development?--------")
total_number_of_webdev_pets = 0
num_webdev_students = 0
for student in students:
    if student["course"] == "web development":
        num_webdev_students += 1
        for pet in student["pets"]:
            total_number_of_webdev_pets += 1
average_pets_per_webdev_student = total_number_of_webdev_pets / num_webdev_students
print(f"On average, a web development student has {round(average_pets_per_webdev_student, 2)} pets.")

# 9. What is the average pet age for students in data science?
print("--------9. What is the average pet age for students in data science?--------")
number_of_ds_pets = 0
sum_ds_pet_age = 0
for student in students:
    if student["course"] == "data science":
        for pet in student["pets"]:
            number_of_ds_pets += 1
            sum_ds_pet_age += pet["age"]
average_age_ds_pets = sum_ds_pet_age / number_of_ds_pets
print("The average age of data science student pets is", round(average_age_ds_pets, 2), "years.")

# 10. What is most frequent coffee preference for data science students?
print("--------10. What is most frequent coffee preference for data science students?--------")
ds_student_coffee_preferences = {}

for student in students:
    if student["course"] == "data science":
        if student["coffee_preference"] not in ds_student_coffee_preferences.keys():
            ds_student_coffee_preferences[student["coffee_preference"]] = 0
        ds_student_coffee_preferences[student["coffee_preference"]] += 1

coffees = [key for key in ds_student_coffee_preferences.keys()]
choice_counts = [value for value in ds_student_coffee_preferences.values()]

highest_count = max(choice_counts)
count_location = choice_counts.index(highest_count)
highest_count_coffee = coffees[count_location]
print(f"The most preferred coffee for data science students is {highest_count_coffee} with {highest_count} votes.")
        
# 11. What is the least frequent coffee preference for web development students?
print("--------11. What is the least frequent coffee preference for web development students?--------")
webdev_coffee_preferences = {}

for student in students:
    if student["course"] == "web development":
        if student["coffee_preference"] not in webdev_coffee_preferences.keys():
            webdev_coffee_preferences[student["coffee_preference"]] = 0
        webdev_coffee_preferences[student["coffee_preference"]] += 1

coffees = [key for key in webdev_coffee_preferences.keys()]
choice_counts = [value for value in webdev_coffee_preferences.values()]

lowest_count = min(choice_counts)
count_location = choice_counts.index(lowest_count)
lowest_count_coffee = coffees[count_location]
print(f"The least preferred coffee for web development students is {lowest_count_coffee} with {lowest_count} votes.")

# 12. What is the average grade for students with at least 2 pets?
print("--------12. What is the average grade for students with at least 2 pets?--------")
average_grades_per_student = []
for student in students:
    if len(student["pets"]) >= 2:
        average_grades_per_student.append(sum(student["grades"]) / len(student["grades"]))
print(f"The average grade for students with at least 2 pets is {sum(average_grades_per_student) / len(average_grades_per_student)}.")

# 13. How many students have 3 pets?
print("--------13. How many students have 3 pets?--------")
count_of_students_with_3_pets = 0
for student in students:
    if len(student["pets"]) == 3:
        count_of_students_with_3_pets += 1
if count_of_students_with_3_pets == 1:
    print(f"Only one student has 3 pets.")
else:
    print(f"There are {count_of_students_with_3_pets} students with 3 pets.")

# 14. What is the average grade for students with 0 pets?
print("--------14. What is the average grade for students with 0 pets?--------")
average_grades_per_student = []
for student in students:
    if len(student["pets"]) == 0:
        average_grades_per_student.append(sum(student["grades"]) / len(student["grades"]))
print(f"The average grade for students with no pets is {round((sum(average_grades_per_student) / len(average_grades_per_student)), 2)}.")


# 15. What is the average grade for web development students? data science students?
print("--------15. What is the average grade for web development students? data science students?--------")
average_grades_per_student = []
for student in students:
    if student["course"] == "web development":
        average_grades_per_student.append(sum(student["grades"]) / len(student["grades"]))
print(f"The average grade for students in web development is {round((sum(average_grades_per_student) / len(average_grades_per_student)), 2)}.")

# 16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
print("--------16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?--------")
average_grades_per_student = []
for student in students:
    if student["coffee_preference"] == "dark":
        average_grades_per_student.append(sum(student["grades"]) / len(student["grades"]))
highest_grade_average = max(average_grades_per_student)
lowest_grade_average = min(average_grades_per_student)
print(f"The range of grade averages for dark coffee drinkers is {lowest_grade_average} to {highest_grade_average}.")

# 17. What is the average number of pets for medium coffee drinkers?
print("--------17. What is the average number of pets for medium coffee drinkers?--------")
pet_count = 0
student_count = 0
for student in students:
    if student["coffee_preference"] == 'medium':
        student_count += 1
        for pet in student["pets"]:
            pet_count += 1
print(f"The average number of pets for medium coffee drinkers is {round((pet_count / student_count), 2)}.")

# 18. What is the most common type of pet for web development students?
print("--------18. What is the most common type of pet for web development students?--------")
pet_types_and_their_counts = {}

for student in students:
    if student["course"] == 'web development':
        for pet in student["pets"]:
            if pet["species"] not in pet_types_and_their_counts.keys():
                pet_types_and_their_counts[pet["species"]] = 0
            pet_types_and_their_counts[pet["species"]] += 1

types = [pet for pet in pet_types_and_their_counts.keys()]
type_counts = [pet for pet in pet_types_and_their_counts.values()]

high_count = max(type_counts)
high_index = type_counts.index(high_count)
most_common_type = types[high_index]

print("The most common type of pet for web development students is", most_common_type)

# 19. What is the average name length?
print("--------19. What is the average name length?--------")
total_characters = 0
total_students = 0
for student in students:
    total_students += 1
    total_characters += len(student["student"]) - 1
print(f"The average name length is {round((total_characters / total_students), 2)} characters long.")

# 20. What is the highest pet age for light coffee drinkers?
print("--------20. What is the highest pet age for light coffee drinkers?--------")
highest_pet_age = 0
for student in students:
    if student["coffee_preference"] == 'light':
        for pet in student["pets"]:
            if pet["age"] > highest_pet_age:
                highest_pet_age = pet["age"]
print("Highest pet age for light coffee drinkers is", highest_pet_age)