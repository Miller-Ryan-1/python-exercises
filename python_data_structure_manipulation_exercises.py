from audioop import avg


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

#1. How many students are there?
student_count = len(students)

#2. How many students prefer light coffee? For each type of coffee roast?
light_count = 0
medium_count = 0
dark_count = 0

for student in students:
    if student['coffee_preference'] == 'light':
        light_count += 1
    elif student['coffee_preference'] == 'medium':
        medium_count += 1
    elif student['coffee_preference'] == 'dark':
        dark_count += 1

print(f'{light_count} students prefer light coffee, {medium_count} prefer medium and {dark_count} prefer dark.')

#3. How many types of each pet are there?
pet_types = []
for student in students:
    for pet in student['pets']:
        if pet['species'] in pet_types:
            continue
        else:
            pet_types.append(pet['species'])
print(f'There are {len(pet_types)} types of pets in the class')
print(pet_types)

#4. How many grades does each student have? Do they all have the same number of grades?
grade_count_initializer = len(students[0]['grades'])
same_number = True
for student in students:
    grade_count = len(student['grades'])
    print(student['student'] + f'has {grade_count} grades.')
    if grade_count != grade_count_initializer:
        same_number = False
if same_number == True:
    print('\n' + f'All students have {grade_count} grades.')
else:
    print('Students do not have the same number of grades')

#5. What is each student's grade average?
for student in students:
    student_total = 0
    for grade in student['grades']:
        student_total += grade
    student_average = student_total/len(student['grades'])
    print(student['student'] + f' has an average of {student_average}')

#6. How many pets does each student have?
for student in students: 
  print(student['student'] + ' has ' + str(len(student['pets'])) + ' pet(s).')

#7. How many students are in web development? data science?
web_dev_stud_count = 0
data_science_stud_count = 0
for student in students:
    if student['course'] == 'data science':
        data_science_stud_count += 1
    else:
        web_dev_stud_count += 1

#8. What is the average number of pets for students in web development?
wd_pet_count = 0
for student in students:
    if student['course'] == 'web development':
        wd_pet_count += len(student['pets'])
wd_pet_count/web_dev_stud_count #from above problem

#9. What is the average pet age for students in data science?
ds_total_pet_age = 0
ds_pet_count = 0
for student in students:
    if student['course'] == 'data science':
        for pets in student['pets']:
            ds_pet_count += 1
            ds_total_pet_age += pets['age']
ds_total_pet_age/ds_pet_count

#10. What is most frequent coffee preference for data science students?
ds_light_count = 0
ds_medium_count = 0
ds_dark_count = 0
for student in students:
    if student['course'] = 'data science'
        if student['coffee_preference'] == 'light':
            ds_light_count += 1
        elif student['coffee_preference'] == 'medium':
            ds_medium_count += 1
        else:
            ds_dark_count += 1
max({'light':ds_light_count,'medium':ds_medium_count,'dark':ds_dark_count})

#11. What is the least frequent coffee preference for web development students?
ds_light_count = 0
ds_medium_count = 0
ds_dark_count = 0
for student in students:
    if student['course'] = 'data science'
        if student['coffee_preference'] == 'light':
            ds_light_count += 1
        elif student['coffee_preference'] == 'medium':
            ds_medium_count += 1
        else:
            ds_dark_count += 1
max({'light':ds_light_count,'medium':ds_medium_count,'dark':ds_dark_count})

#12. What is the average grade for students with at least 2 pets?
total_grades = 0
studs_w_two_pets = 0
for student in students:
    if len(student['pets']) >= 2:
        studs_w_two_pets += 1
        for grade in student['grades']:
            total_grades += grade
total_grades/(studs_w_two_pets * 4)

#13. How many students have 3 pets?
studs_w_three_pets = 0
for student in students:
    if len(student['pets']) == 3:
        studs_w_three_pets += 1
studs_w_three_pets

#14. What is the average grade for students with 0 pets?
total_grades = 0
studs_w_no_pets = 0
for student in students:
    if len(student['pets']) == 0:
        studs_w_no_pets += 1
        for grade in student['grades']:
            total_grades += grade
total_grades/(studs_w_no_pets * 4)

#15. What is the average grade for web development students? data science students?
ds_total_grade = 0
wd_total_grade = 0
for student in students:
    if student['course'] == 'data science':
        for grade in student['grades']:
            ds_total_grade += grade
    else:
        for grade in student['grades']:
            wd_total_grade += grade
ds_grade_avg = ds_total_grade/(data_science_stud_count * 4)
wd_grade_avg = wd_total_grade/(web_dev_stud_count * 4)
ds_grade_avg,wd_grade_avg

#16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
dc_drinkers_grades = []
for student in students:
    if student['coffee_preference'] == 'dark':
        for grade in student['grades']:
            dc_drinkers_grades.append(grade)
max(dc_drinkers_grades) - min(dc_drinkers_grades)

#17. What is the average number of pets for medium coffee drinkers?
medium_pets = 0
for student in students:
    if student['coffee_preference'] == 'medium':
        medium_pets += len(student['pets'])
avg_medium_pets = medium_pets/medium_count

#18. What is the most common type of pet for web development students?
wd_pet_dict = {}
for student in students:
    if student['course'] == 'web development':
        for pet in student['pets']:
            if pet['species'] in wd_pet_dict:
                wd_pet_dict[pet['species']] += 1
            else:
                wd_pet_dict[pet['species']] = 1
max(wd_pet_dict)

#19. What is the average name length?
name_lengths =[]
for student in students:
    name_lengths.append(len(student['student'].replace(' ','')))
sum(name_lengths)/len(name_lengths) #note: space removed from between names

#20. What is the highest pet age for light coffee drinkers?
max_pet_age = 0
for student in students:
    if student['coffee_preference'] == 'light':
      for pets in student['pets']:
        if pets['age'] > max_pet_age:
          max_pet_age = pets['age']
print(max_pet_age)