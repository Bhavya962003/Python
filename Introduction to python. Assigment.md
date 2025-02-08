1. What are the types of Applications?

Web Applications: Websites and web services (e.g., Google, Amazon, Facebook).
Desktop Applications: Software running on personal computers (e.g., Microsoft Office, Adobe Photoshop).
Mobile Applications: Apps for smartphones and tablets (e.g., Instagram, WhatsApp).
Enterprise Applications: Software for large organizations (e.g., SAP, Oracle).
Scientific Applications: Used in research and data analysis (e.g., MATLAB, Mathematica).
Embedded Systems: Software within devices (e.g., smartwatches, cars).

2. What is programming?

Programming is the process of creating instructions for a computer to perform specific tasks. It involves writing code using a programming language, which the computer then interprets and executes.


3. What is Python?

Python is a high-level, general-purpose programming language known for its simplicity and readability. It's widely used for web development, 
data science, machine learning, automation, and more.


4. Write a Python program to check if a number is positive ,nagative,or zero.

 num =float(input("Enter a number :"))
 if num > 0:
     print("Positive number")
 elif num <0:
     print("Nagative number")
 else:
      print("Zero")


5. Write a Python program to get the Factorial number of given number.
def factorial(n):
    if n==0:
        return 1

    else:
        return n * factorial(n-1)

num= int(input("Enter a number:"))
print("Factorial of",num,"is",factorial(num))


6. Write aPython program to get the Fibonacci series of given range.

def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a,end="")
        a,b=b,a+b

num =int(input("Enter the range:"))
fibonacci(num)
        
7. How memory is managed in Python?

Python uses a garbage collector to manage memory automatically.
It tracks objects that are no longer in use and reclaims their
memory.


8. What is the purpose of the continue statement in python?

The continue statement skips the rest of the code within a loop and moves 
on to the next iteration.


9. Write a Python program that swaps two numbers with atemp variable and without a temp variable.

# With temp variable
a = 5
b = 10

temp = a
a = a
b = temp

# Without temp variable
      
a = 5         
b = 10

a,b = b,a


10. Write a python program to find whether a given number is even or old,
print out an appropriate message to the user.

 num = int(input("Enter a number:"))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num,"is odd")


11. Write a python program to test whether a passed letter is a vowel or not.

letter = input("Enter a letter:")

if letter in 'aeiouAEIOU':
    print(letter,"is a vowel")
else:
    print(letter,"is not a vowel")


12. Write a python program to sum of three given integers . However,
if two values are equal,sum will be zero.

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
 if a == b or a == c or b == c:
     print("sum is zero")
 else:
    print("sum is",a+b+c)

13. Write a Python program that will return true if the two given 
integer values are equal or their sum or difference is 5. 

def check_values(x, y):
    return x == y or x + y == 5 or abs(x - y) == 5

print(check_values(2, 2))  # True
def check_values(x, y):
    return x == y or x + y == 5 or abs(x - y) == 5

print(check_values(2, 2))  # True
print(check_values(2, 3))  # True
print(check_values(7, 2))  # True
print(check_values(1, 6))  # False


14. Write a python program to sum of the first n positive integers. 
    
def sum_of_n_integers(n):
  sum = 0
  for i in range(1, n+1):
    sum += i
  return sum
def sum_of_n_integers(n):
  sum = 0
  for i in range(1, n+1):
    sum += i
  return sum

n = int(input("Enter a positive integer: "))
print("The sum of the first", n, "positive integers is", sum_of_n_integers(n))


15. Write a Python program to calculate the length of a string.

# Get the input string from the user
string = input("Enter a string: ")

def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count

# Get the input string from the user
string = input("Enter a string: ")

# Calculate and print the length of the string
length = string_length(string)
print("Length of the string is:", length)


16. Write a Python program to count the number of characters 
(character frequency) in a string

def char_frequency(string):
  freq = {}
  for char in string:
    if char in freq:
      freq[char] += 1
    else:
      freq[char] = 1
  return freq

string = "Hello, World!"
print(char_frequency(string))
    
 
17. What are negative indexes and why are they used? 

Negative indexes in Python allow you to access elements from the end of a sequence (like a string or list). For example, -1 refers to the last element, -2 refers to the second-to-last element, and so on. They're useful for accessing elements from the end without knowing the exact length of the sequence."))18. Write a Python program to count occurrences of a substring in a string. 


18. Write a Python program to count occurrences of a substring in a string. 


def count_substring(string, sub_string):
  return string.count(sub_string)

print(count_substring("Hello, World!", "o"))




19. Write a Python program to count the occurrences of each word in a
given sentence.




 def count_words(sentence):
  """Counts the occurrences of each word in a given sentence."""

  words = sentence.split()  # Split sentence into words
  word_counts = {}          # Dictionary to store word counts

  for word in words:
    word = word.lower()  # Convert to lowercase for case-insensitive counting
    if word in word_counts:
      word_counts[word] += 1
    else:
      word_counts[word] = 1

  return word_counts

# Example usage
sentence = "The quick brown fox jumps over the lazy dog."
word_counts = count_words(sentence)
print(word_counts)   


20. Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string.


def swap_and_join(str1, str2):
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    return new_str1 + ' ' + new_str2

print(swap_and_join('Manan', 'Ankita')) 
    
    

21.  Write a Python program to add 'in' at the end of a given string (length 
should be at least 3). If the given string already ends with 'ing' then 
add 'ly' instead if the string length of the given string is less than 3, 
leave it unchanged. 

def add_ing_or_ly(str1):
    if len(str1) < 3:
        return str1
    elif str1.endswith('ing'):
        return str1 + 'ly'
    else:
        return str1 + 'ing'

print(add_ing_or_ly('abc'))     
print(add_ing_or_ly('string')) 
print(add_ing_or_ly('ab'))  


22. Write a Python function to reverses a string if its length is a multiple 
of 4. 

def reverse_if_multiple_of_4(str1):
    if len(str1) % 4 == 0:
        return str1[::-1]
    else:
        return str1

print(reverse_if_multiple_of_4('abcd')) 
print(reverse_if_multiple_of_4('abc'))  


23. Write a Python program to get a string made of the first 2 and the last 
2 chars from a given a string. If the string length is less than 2, return 
instead of the empty string.


def first_and_last_two(str1):
    if len(str1) < 2:
        return ''
    else:
        return str1[:2] + str1[-2:]

print(first_and_last_two('abcdef'))  
print(first_and_last_two('ab'))       
print(first_and_last_two('a'))        




24. Write a Python function to insert a string in the middle of a string. 


def insert_in_middle(str1, str2):
  mid_index = len(str1) // 2
  return str1[:mid_index] + str2 + str1[mid_index:]

print(insert_in_middle('{{}}', 'Python'))  



25. What is List? How will you reverse a list? 

A list is a data structure in Python that can store a collection of items.
To reverse a list, you can use the reverse() method:

my_list = [1, 2, 3]
my_list.reverse()
print(my_list)     


26. How will you remove last object from a list?

my_list = [1, 2, 3] 
my_list.pop(2)
print(my_list) 


27. Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-
1]? 

 list1[-1] will return the last element of the list, which is 25.




28. Differentiate between append() and extend() methods?


append() adds a single element to the end of a list.

extend() adds the elements of another iterable (e.g., list, tuple, string) to the end of the list.

my_list = [1, 2, 3]

# append() adds a single element
my_list.append(4) 
print(my_list)  # Output: [1, 2, 3, 4]

# extend() adds multiple elements from another iterable
my_list.extend([5, 6]) 
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]



29. Write a Python function to get the largest number, smallest num 
and sum of all from a list. 


def analyze_list(lst):
  largest = max(lst)
  smallest = min(lst)
  total = sum(lst)
  return largest, smallest, total

lst=[20,60,40,30]   
largest, smallest, total= analyze_list(lst)
print("Largest:", largest)
print("Smallest:", smallest)
print("Total:", total)


30. How will you compare two lists? 


1. Equality:
Use the == operator to check if two lists have the same elements in the same order:

list1 = [1, 2, 3]
list2 = [1, 2, 3]
if list1 == list2:
    print("Lists are equal")
else:
    print("Lists are not equal") 
 

2. Length:
Use the len() function to compare the lengths of two lists:

list1 = [1, 2, 3]
list2 = [4, 5]
if len(list1) == len(list2):
    print("Lists have the same length")   
else:
    print("Lists have different lengths")   


3. Membership:
Use the in operator to check if a specific element exists in a list:

list1 = [1, 2, 3]
   
if 2 in list1:
       print("2 is in list1")
else:
       print("2 is not in list1")



4. Set operations:
Convert lists to sets using the set() function to perform set operations like:
Union: Combine all elements from both lists (no duplicates).
Intersection: Find elements that exist in both lists.
Difference: Find elements that exist in one list but not the otherlist1 = [1, 2, 3]
   list2 = [2, 3, 4]
   
   set1 = set(list1)
   set2 = set(list2)
   
   union = set1.union(set2)
   intersection = set1.intersection(set2)
   difference = set1.difference5. Element-wise comparison:
Use a loop to compare elements at corresponding indices in both lists.
This is useful for comparing values or performing custom comparisons.(set2).31. ) Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given list 
of strings. 

def count_matching_strings(list_of_strings):
  count = 0
  for string in list_of_strings:
    if len(string) >= 2 and string[0] == string[-1]:
      count += 1
  return count

# Example usage:
strings = ['abc', 'xyz', 'aba', '1221', 'a']
result = count_matching_strings(strings)
print(result)  



  

32. Write a Python program to remove duplicates from a list.

numbers = [1, 2, 2, 3, 4, 4, 5]

econ = list(set(numbers))


print(econ)

# output[1, 2, 3, 4, 5]



33. Write a Python program to check a list is empdef Bhavya(hhh):
    return not hhh
    
kriti=[]
manan=[1,2,3]
print(Bhavya(kriti))
print(Bhavya(manan))ty# output:True
         False
     34. Write a Python function that takes two lists and returns true if they 
have at least one common member.   def have_common_member(list1, list2):
  for item in list1:
    if item in list2:
      return True
  return False

# Example usage
list1 = [1, 2, 3]
list2 = [3, 4, 5]
print(have_common_member(list1, list2)) or not.35. Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30. 
 def generate_list():
  squares = [x**2 for x in range(1, 31)]
  return squares[:5] + squares[-5:]

# Example usage
print(generate_list()) 








36. Write a Python function that takes a list and returns a new list with 
unique elements of the first list.

def unique_elements(list1):
  return list(set(list1))

# Example usage
numbers = [1, 2, 2, 3, 4, 4, 5]
print(unique_elements(numbers)) # Output: [1, 2, 3, 4, 5]


37. Write a Python program to convert a list of characters into a string. 

def list_to_string(char_list):
  return ''.join(char_list)

# Example usage
chars = ['H', 'e', 'l', 'l', 'o']
print(list_to_string(chars))

# Output: Hello



38. Write a Python program to select an item randomly from a list. 

import random

def select_random_item(my_list):
    return random.choice(my_list)

my_list = [1, 2, 3, 4, 5]
print(select_random_item(my_list)) 



39. Write a Python program to find the second smallest number in a list. 

def second_smallest(my_list):
    unique_list = sorted(set(my_list))
    if len(unique_list) < 2:
        return None
    return unique_list[1]

my_list = [1, 2, 2, 3, 4, 5]
print(second_smallest(my_list))


# output:2



40. Write a Python program to get unique values from a list.


def get_unique_values(my_list):
    return list(set(my_list))

my_list = [1, 2, 2, 3, 4, 5]
print(get_unique_values(my_list))  


# output:[1, 2, 3, 4, 5]



41. Write a Python program to check whether a list contains a sublist.

def contains_sublist(main_list, sub_list):
    for i in range(len(main_list) - len(sub_list) + 1):
        if main_list[i:i+len(sub_list)] == sub_list:
            return True
    return False

main_list = [1, 2, 3, 4, 5]
sub_list = [2, 3]
print(contains_sublist(main_list, sub_list)ent variables. 42. Write a Python program to split a list into different variables.True


my_list = [1, 2, 3]
a, b, c = my_list
print(a)  
print(b)  
print(c) 

# output:1
         2
         3



43. What is tuple? Difference between list and tuple.


A tuple is an ordered, immutable sequence of elements. The key difference between a list and a tuple is that lists are mutable (can be changed), while tuples are immutable (cannot be changed).




44. Write a Python program to create a tuple with different data types. 

my_tuple = (1, "Hello", 3.14)
print(my_tuple) 



45. Write a Python program to unzip a list of tuples into individual lists. 


my_list = [(1, 'a'), (2, 'b'), (3, 'c')]
list1, list2 = zip(*my_list)
print(list1)  
print(list2) 

 # output: (1, 2, 3)
            ('a', 'b', 'c')

46. Write a Python program to convert a list of tuples into a dictionary. 

a = [("a", 1), ("b", 2), ("c", 3)]
res = dict(a)
print(res)

# output:{'a': 1, 'b': 2, 'c': 3}



47. How will you create a dictionary using tuples in python?

my_tuple = (("x", 10), ("y", 20))
my_dict = dict(my_tuple)
print(my_dict)

# Output: {'x': 10, 'y': 20}




48. Write a Python script to sort (ascending and descending) a 
dictionary by value.


my_dict = {"a": 3, "b": 1, "c": 2}

# Ascending sort
asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(asc_sorted)  

# Descending sort
desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(desc_sorted)  


output: {'b': 1, 'c': 2, 'a': 3}
        {'a': 3, 'c': 2, 'b': 1}


49. Write a Python script to concatenate following dictionaries to create 
a new one. 


dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

new_dict = {**dict1, **dict2}
print(new_dict) 

# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}



50. Write a Python script to check if a given key already exists in a 
dictionary. 



my_dict = {"a": 1, "b": 2, "c": 3}
key_to_check = "b"

if key_to_check in my_dict:
    print("Key exists")
else:
    print("Key does not exist")

                                        

51. How Do You Traverse Through a Dictionary Object in Python?


my_dict = {"a": 1, "b": 2, "c": 3}

# Using .items()
for key, value in my_dict.items():
    print(key, value)

# Using .keys()
for key in my_dict.keys():
    print(key)

# Using .values()
for value in my_dict.values():
    prioutput: a 1
        b 2
        c 3 
        a
        b
        c
        1
        2
        3
         t(52. How Do You Check the Presence of a Key in A Dictionary?


my_dict = {"a": 1, "b": 2, "c": 3}
key_to_check = "b"

if key_to_check in my_dict:
    print("Key exists")
else:
    print("Key does not exist")



53. Write a Python script to print a dictionary where the keys are 
numbers between 1 and 15. 

my_dict = {i: i**2 for i in range(1, 16)}
print(my_dict) 

# Output: {1: 1, 2: 4, 3: 9, ..., 15: 225}


v54. Write a Python program to check multiple keys exists in a dictionary aludef check_multiple_keys(dict1, keys):
    return all(key in dict1 for key in keys)

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(check_multiple_keys(my_dict, ['a', 'b'])) 
print(check_multiple_keys(my_dict, ['a', 'd']))e)

 # output: True
          False
          




55. Write a Python script to merge two Python dictionaries 


def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print(merge_dictionaries(dict1, dict2))


# output:# {'a': 1, 'b': 2, 'c': 3, 'd': 4}



56. Write a Python program to map two lists into a dictionary 
Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).



def map_lists_to_dict(list1, list2):
    return dict(zip(list1, list2))

keys = ['a', 'b', 'c']
values = [1, 2, 3]
print(map_lists_to_dict(keys, values))

# {'a': 1, 'b': 2, 'c': 3}



57. Write a Python program to find the highest 3 values in a dictionary

from collections import Counter
def find_highest_3_values(dict1):
    return dict(Counter(dict1).most_common(3))

my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
print(find_highest_3_values(my_dict))

# {'e': 500, 'd': 400, 'c': 300}


58. )Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
300}, o {'item': 'item1', 'amount': 750}] 
Expected Output:
• Counter ({'item1': 1150, 'item2': 300})


from collections import Counter

def combine_values(data):
    result = Counter()
    for d in data:
        result[d['item']] += d['amount']
    return result

sample_data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

print(combine_values(sample_data))




59. Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string. 


def create_dict_from_string(string):
    result = {}
    for char in string:
        result[char] = result.get(char, 0) + 1
    return result

sample_string = 'w3resource'
print(create_dict_from_strin
Sample string:
 'w3resource' Expected output:
• {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
g(sample_string))  



60. 



def count_characters(string):
  """Counts the occurrences of each character in a string."""

  char_count = {}
  for char in string:
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1

  return char_count

string = 'w3resource'
print

 ક61) Write a Python function to calculate the factorial of a number (a nonnegative integer)
def factorial(n):
if n == 0:
return 1
else:
return n * factorial(n-1)
print(factoria:# Output: 120 
162) Write a Python function to check whether a number is in a given range
def is_in_range(n, start, end):
return n in range(start, end+1)
print(is_in_range(5, 1, 10rue
print(is_in_range(15, 1, 1se0ાર્# Output: Trueય# Output: False  t_char


63) Write a Python function to check whether a number is perfect or not.
def is_perfect(n):
if n <= 0:
return False
sum_of_divisors = 0
for i in range(1, n):
if n % i == 0:
sum_of_divisors += i
return sum_of_divisors == n
print(is_perput: True
print(is_per
print(is_perfect(12)) 

# Output: Trueu# Output: Truet# Output: False: Fal64) Write a Python function that checks whether a passed string is palindrome or not


def is_palindrome(s):
s = s.lower()
return s == s[::-1]
print(is_palindrome("racecarTrue
print(is_palindrome("A man, a plan, a canal: Panam True
print(is_palindrome("helF# Output: True
# Output: True
# Output: False

65) How Many Basic Types of Functions Are Available in Python?

There are two basic types of functions available in Python:

Built-in Functions: These functions are already defined in Python and are always available. Examples include print(), len(), and range().

User Defined Functions: These functions are created by the user and used to perform specific tasks.



66) How can you pick a random item from a list or tuple?

import random
my_list = [1, 2, 3, 4, 5]
random_item = random.choice(my_list)
print(random_item)



67) How can you pick a random item from a range?

random_item = random.randrange(1, 10) 
print(random_item)


68) How can you get a random number in python?

import random
random_number = random.random()
print(random_number)


69) How will you set the starting value in generating random numbers?

import random
random.seed(10)
print(random.random())




70) How do you randomize the items of a list in place?
import random
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list) # Output will be a shuffled version of the list



71) What is a File function in Python? What are keywords to create and write a file?
● File function: In Python, file functions are used to interact with files on your computer's
file system. This includes tasks like opening files, reading their contents, writing to them,
and closing them.
● Keywords:
○ open(): This is the primary function to open a file. You specify the file name and the
mode (e.g., 'r' for reading, 'w' for writing, 'a' for appending).
○ with: It's best practice to use the with statement when working with files. It ensures
that the file is automatically closed, even if errors occur.
○ write(): Used to write data to a file.




72) Write a Python program to read an entire text file.
with open('my_file.txt', 'r') as file:
content = file.read()
print(content)



73) Write a Python program to append text to a file and display the text.
with open('my_file.txt', 'a') as file:
file.write("This is new text.\n")
with open('my_file.txt', 'r') as file:
content = file.read()
print(content)


74) Write a Python program to read the first n lines of a file.
def read_first_n_lines(filename, n):
with open(filename, 'r') as file:
for _ in range(n):
line = file.readline()
if not line: # Handle cases where the file has fewer than
n lines
break
print(line, end='') # Prevent extra newlines
read_first_n_lines('my_file.txt', 3) # Reads and prints the first 3
lines


75) Write a Python program to read the last n lines of a file.
def read_last_n_lines(filename, n):
with open(filename, 'r') as file:
lines = file.readlines()
last_n_lines = lines[-n:] # Get the last n lines
for line in last_n_lines:
print(line, end='')
read_last_n_lines('my_file.txt', 2) # Reads and prints the last 2
lines


76) Write a Python program to read a file line by line and store it into a list.
lines = []
with open('my_file.txt', 'r') as file:
for line in file:
lines.append(line.strip()) # Remove newline characters
print(lines)


77) Write a Python program to read a file line by line and store it into a variable.
content = ""
with open('my_file.txt', 'r') as file:
for line in file:
content += line
print(content)



78) Write a Python program to find the longest words in a file.
def find_longest_words(filename):
longest_words = []
max_length = 0
with open(filename, 'r') as file:
for line in file:
words = line.split()
for word in words:
word = word.strip('.,!?"').lower() # Clean up words
if len(word) > max_length:
max_length = len(word)
longest_words = [word] # Start a new list
elif len(word) == max_length:
longest_words.append(word) # Add to the existing
list
return longest_words
longest = find_longest_words('my_file.txt')
print(longest)



79) Write a Python program to count the number of lines in a text file.
with open('my_file.txt', 'r') as file:
num_lines = sum(1 for line in file)
print("Number of lines:", num_lines)



80) Write a Python program to count the frequency of words in a file.
from collections import Counter
word_counts = Counter()
with open('my_file.txt', 'r') as file:
for line in file:
words = line.split()
for word in words:
word = word.strip('.,!?"').lower()
word_counts[word] += 1
print(word_counts)



81) Write a Python program to write a list to a file.
my_list = ["apple", "banana", "cherry"]
with open('output.txt', 'w') as file:
for item in my_list:
file.write(item + "\n")



82) Write a Python program to copy the contents of a file to another file.
with open('source.txt', 'r') as source_file, open('destination.txt',
'w') as dest_file:
for line in source_file:
dest_file.write(line)



83) Explain Exception handling? What is an Error in Python?
● Exception handling: It's a way to gracefully manage errors that might occur during the
execution of your program. Instead of the program crashing, you can handle the error and
potentially take corrective actions.
● Error: An error is an issue that prevents your program from running correctly. It could be a
syntax problem, a runtime issue (like dividing by zero), or something else.



84) How many except statements can a try-except block have? Name some built-in
exception classes.
● You can have multiple except statements in a try-except block to handle different types of
exceptions.
● Built-in exception classes:
○ ZeroDivisionError
○ TypeError
○ ValueError
○ FileNotFoundError
○ IOError



85) When will the else part of try-except-else be executed?
The else block is executed if no exceptions occur in the try block.



86) Can one block of except statements handle multiple exceptions?
Yes, you can use a tuple of exceptions in a single except block:
try:
# Some code
except (TypeError, ValueError) as e:
print("Caught either a TypeError or ValueError:", e)



87) When is the finally block executed?
The finally block is always executed, whether an exception occurred or not. It's often used for
cleanup tasks (like closing files).



88) What happens when "1" + 1 is executed?
This will result in a TypeError. You can't directly add a string ("1") and an integer (1). Python will
try to concatenate them, but it won't work as intended.



89) How Do You Handle Exceptions with Try/Except/Finally in Python? Explain with
coding snippets.
try:
result = 10 / 0 # This will cause a ZeroDivisionError
except ZeroDivisionError:
print("Cannot divide by zero!")
finally:
print("This will always execute.")




90) Write a Python program that prompts the user to enter only odd numbers, else will
raise an exception.
while True:
try:
num = int(input("Enter an odd number: "))
if num % 2 == 0:
raise ValueError("Even numbers are not allowed.")
else:
print("Thank you for entering an odd number.")
break # Exit the loop if an odd number is entered
except ValueError as e:
print("Error:", e)
alsese









acters(string))











       



    
