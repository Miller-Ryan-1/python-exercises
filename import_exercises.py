#1b. Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly. Call this function with values you choose and print the result.
from function_exercises import calculate_tip
print(calculate_tip(.22,25))

#2(i).  How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
import itertools
print(len(list(itertools.product('abc','123'))))
# ANS: 9

#2(ii). How many different combinations are there of 2 letters from "abcd"?
print(len(list(itertools.permutations('abcd',2))))
# ANS: 12

#2(iii). How many different permutations are there of 2 letters from "abcd"?
print(len(list(itertools.combinations('abcd',2))))
#ANS: 6

