#1a. Prompt the user for a day of the week, print out whether the day is Monday or not
user_input_1a = input('What day of the week is it? ')
if user_input_1a in ['Monday' or 'monday']:
  print('It is Monday.')
elif user_input_1a in ['Sunday','Tuesday','Wednesday','Thursday','Friday','Saturday'] or user_input_1a in ['sunday','tuesday','wednesday','thursday','friday','saturday']:
  print('It is not Monday.')
else:
  print('That is not a valid day of the week')

#1b. Prompt the user for a day of the week, print out whether the day is a weekday or a weekend
user_input_1b = input('What day of the week is it? ')
if user_input_1b in ['Sunday','Saturday', 'sunday', 'Saturday']:
  print('It\'s the weekend!')
elif user_input_1b in ['Monday','Tuesday','Wednesday','Thursday','Friday'] or user_input_1b in ['monday','tuesday','wednesday','thursday','friday']:
  print('It\'s a weekday.')
else:
  print('That is not a valid day of the week')

#1c. Create variables and make up values for (i)the number of hours worked in one week, (ii) the hourly rate, (iii) how much the week's paycheck will be and (iv) write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
weekly_hours_worked = 50
hourly_rate = 200
if(weekly_hours_worked <= 40):
    weekly_paycheck = (weekly_hours_worked * hourly_rate)
else:
    weekly_paycheck = 40* hourly_rate + ((weekly_hours_worked - 40) * (hourly_rate * 1.50))
print ('You made $' + str(int(weekly_paycheck)) + ' this week.')

#2a. (See while loop prompts)
i = 5
while i <= 15:
    print(i)
    i += 1

j = 0
while j <= 100:
    print(j)
    j += 2

k = 100
while k >= -10:
    print(k)
    k -= 5

l = 2
while l < 1000000:
    print(l)
    l *= l

m = 100
while m > 0:
    print(m)
    m -= 5

#2b. (See for loop prompts)
#(i)
user_input = input('Gimme a number: ')
if user_input.isdigit() != True:
    print('Not a valid number; restart and try again.')
else:
  for n in range(1,11):
    x = int(user_input) * n
    print(user_input + ' x ' + str(n) + ' = ' + str(x))

#(ii)
for n in range(1,10):
    x = str(n) * n
    print(str(x))

#2c. (See break and continue prompts)
#(i)
x = 0
while x < 1:
    user_input = input('Enter an odd number between 1 and 50: ')
    if user_input.isdigit() != True or int(user_input) % 2 == 0 or int(user_input) < 1 or int(user_input) > 50:
        print('Not a valid entry, try again')
        continue
    else:
        break
print('\nNumber to skip is: ' + user_input + '\n')
for n in range (1,50):
    if n % 2 == 0:
        continue
    elif n == int(user_input):
        print('Yikes! Skipping number: ' + user_input)
        continue
    else:
        print('Here is an odd number: ' + str(n))

#2d. The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
user_input = input('Enter a positive integer: ')
if user_input.isdigit() != True or int(user_input) < 1:
    print('Invalid input.  Run program again with integer greater than 0')
else:
    user_input = int(user_input)
    for i in range(user_input+1):
    print(i)

#2e.  Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
user_input = input('Enter a positive integer: ')
if user_input.isdigit() != True or int(user_input) < 1:
    print('Invalid input.  Run program again with integer greater than 0')
else:
    user_input = int(user_input)
    while user_input > 0:
      print(user_input)
      user_input -= 1

#3. Fizzbuzz Program
for i in range(1,101):
    if i % 15 == 0:
        print('Fizzbuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

#4.  Display a table of powers.
from tabulate import tabulate
user_continue = True
while user_continue == True:
  user_input = input('What number would you like to go up to? ')
  a = int(user_input)
  print('\nHere is your table!\n')
  result = []
  for i in range(a+1):
    result.append([i,i**2,i**3])
  print(tabulate(result, headers=['number', 'squared', 'cubed'], tablefmt='presto', colalign=("left",'left','left')))
  choose_continue = input('Do you want to continue? (y/n): ')
  if choose_continue in ['y', 'Y']:
    continue
  else:
    user_continue = False

#5.  Convert given number grades into letter grades.
user_continue = True
while user_continue == True:
  user_input = int(input('Enter a numerical grade to get letter grade: '))
  if user_input >= 97:
    grade = 'A+'
  elif user_input in range(92,97):
    grade = 'A'
  elif user_input in range(88,92):
    grade = 'A-'
  elif user_input in range(87,88):
    grade = 'B+'
  elif user_input in range(83,87):
    grade = 'B'
  elif user_input in range(80,83):
    grade = 'B-'
  elif user_input in range(77,80):
    grade = 'C+'
  elif user_input in range(70,77):
    grade = 'C'
  elif user_input in range(67,70):
    grade = 'C-'
  elif user_input in range(60,67):
    grade = 'D'
  else:
    grade = 'F'
  print('Letter grade is:',grade)
  choose_continue = input('Do you want to continue? (y/n): ')
  if choose_continue in ['y', 'Y']:
    continue
  else:
    user_continue = False

#6. Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.  Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre. 
booklist = [
{'title':'Moby Dick', 
 'author':'Herman Melville',
 'genre':'Historical Fiction'},
{'title':'Once an Eagle', 
 'author':'Anton Meyer',
 'genre':'war fiction'},
{'title':'The Three Body Problem', 
 'author':'Liu Cixin',
 'genre':'Science Fiction'},
{'title':'The Expanse', 
 'author':'James S. A. Corey',
 'genre':'Science Fiction'},
{'title':'The Mathematical Universe',
 'author':'Max Tegmark',
 'genre':'Science'},
{'title':'Progress and Poverty',
'author':'Henry George',
'genre':'Economics'}]

user_input = input('Enter a genre to see my favorite books in that genre: ')
validator = 0
genre = user_input.lower()
for book in booklist:
  if book['genre'].lower() == genre:
    print(book['title'] + ' by ' + book['author'])
    validator = 1
if validator == 0:
  print('I have no favorite books in this genre')
