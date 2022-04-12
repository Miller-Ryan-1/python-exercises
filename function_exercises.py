#1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(n):
    if n in (2,'2'):
        return True
    else:
        return False
# Don't forget - you can test this WITHOUT if/else just looking at if it is true or not (and allows for lambda1)


#2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(string):
    return string.lower() in ('a','e','i','o','u')
    #     return True
    # else:
    #     return False

#3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(string):
    if string.lower() in ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'):
        return True
    else:
        return False

#4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def constant_capitalizer(string):
    if string[0].lower() not in ('a','e','i','o','u'):
        return string.capitalize()
    else:
        return string

#5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(rate, bill):
    if rate in (0,1):
        return bill * rate
    else:
        print('Invalid tip rate.  Please enter a number between zero and one.')
        return

 #6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(price,discount):
    return price*(1-discount)

#7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
handle_commas = lambda num_string: int(num_string.replace(',',''))

#8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(num_grade):
    if num_grade > 90:
        return 'A'
    elif num_grade > 80:
        return 'B'
    elif num_grade > 70:
        return 'C'
    elif num_grade > 65:
        return 'D'
    else:
        return 'F'

#9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(string):
    newstring = []
    for letter in string:
        if letter not in ('A','a','E','e','I','i','O','o','U','u'):
            newstring.append(letter)
    return ''.join(newstring)
#Don't forget, you can add letters to string simply by + (add concat)!  No need to turn to list!!

#10. Define a function named normalize_name. It should accept a string and return a valid python identifier.
def normalize_name(string):
    if type(string) != str:
        print('Invalid input, please enter a string')
        return
    string = string.strip()
    string = string.lower()
    string_list = []
    for letter in string:
        if letter.isalnum() == True:
            string_list.append(letter)
        if letter == ' ':
            string_list.append('_')
    return ''.join(string_list)
#Look into .isidentifier() function

#11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
def cumulative_sum(list):
    sum_list = []
    sum = 0
    for n in list:
        sum += n
        sum_list.append(sum)
    return sum_list

#12a (Bonus). Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format.
def twelveto24(string):
    # Here I would check format, but don't want to spend hours figuring out the regex so assuming proper input
    # Determine am/pm:
    ampm = string[-2]
    # slice last two letters out
    string = string[0:-2]
    # then split remaining string by ':'
    stringlist = string.split(':')
    # use the first letter of the splice to determine whether or not to add 12
    if ampm == 'p':
        #convert to int to add the 12 then back to string - *there must be an easier way to do this!
        x = int(stringlist[0]) 
        x += 12
        x = str(x)
        stringlist[0] = x
    # if not adding 12 and the first number is a single digit, add a leading zero
    string = ''.join(stringlist)
    if len(string) == 4:
        return string
    else:
        return '0' + string

#12b (Bonus). Convert from 24 hour to 12 hour
def twentyfourto12(string):
    #Split into two parts
    string_hours = string[0:2]
    string_minutes = string[2:]
    #if there is a leading zero, remove the zero, and concat with colon, minutes and am
    if string_hours[0] == '0':
        return string_hours[1] + ':' + string_minutes + 'am'
    #if first is 10 or 11, concat with colon, minutes and am
    if string_hours == '10' or string_hours == '11':
        return string_hours + ':' + string_minutes + 'am'
    #if first is 12, concat with minutes and pm
    if string_hours == '12':
        return string_hours + ':' + string_minutes + 'pm'
    #if first has leading zeropart greater than 12, convert to number, subtract 12 from it convert back to and store it as a pm
    string_hours = int(string_hours) - 12
    return str(string_hours) + ':' + string_minutes + 'pm'

#13 (Bonus). Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
def col_index(string):
  #create letter string with zero prefix (so that A=1, Z=26)
  letter_value = ('0ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  #split and reverse input string into list
  string_list = list(string)
  string_list.reverse()
  #create index variable and initialize to the zero index value of input list, looking for the index in letter string
  index = 0
  #Loop through input list determining value from input string and multiplying by 26 to the index power, but skipping over the first letter (because 26**0 = 1)
  for i in range(len(string_list)):
    index += letter_value.index(string_list[i]) * (26 ** i)
  return index
