#1. What are the types of Applications?

"""Web Applications:

Websites and web services (e.g., Google, Amazon, Facebook).

Desktop Applications: 
Software running on personal computers (e.g., Microsoft Office, Adobe Photoshop).

Mobile Applications:

Apps for smartphones and tablets (e.g., Instagram, WhatsApp).
Enterprise Applications:

Software for large organizations (e.g., SAP, Oracle).
Scientific Applications: 

Used in research and data analysis (e.g., MATLAB, Mathematica).
Embedded Systems: Software within devices (e.g., smartwatches, cars)."""

#2. What is programming?

"""Programming is the process of creating instructions for a computer to perform specific tasks. It involves writing code using a programming language, which the computer then interprets and executes."""


#3. What is Python?

''''Python is a high-level, general-purpose programming language known for its simplicity and readability. Its widely used for web development, 
data science, machine learning, automation, and more.'''


#4. Write a Python program to check if a number is positive ,nagative,or zero.

number =int(input("Enter a number :"))
if number > 0:
     print("Positive number")
elif number <0:
     print("Nagative number")
else:
      print("Zero")


#5. Write a Python program to get the Factorial number of given number.
def factorial(n):
    if n==0:
        return 1

    else:
        return n * factorial(n-1)

Bhavya_num= int(input("Enter a number:"))
print("Factorial of",Bhavya_num,"is",factorial(num))



#6. Write a Python program to get the Fibonacci series of given range.

def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a,end="")
        a,b=b,a+b

num =int(input("Enter the range:"))
fibonacci(num)
        
#7. How memory is managed in Python?

"""Python uses a private heap managed by its memory manager .
it employs reference counting and garbage collection to 
automatically allocate and deallocate memory."""


#8. What is the purpose of the continue statement in python?

"""he continue statement skips the rest of the code within a loop and moves 
on to the next iteration."""


#9. Write a Python program that swaps two numbers with atemp variable and without a temp variable.

 #With temp variable
a = 5
b = 10

temp = a
a = a
b = temp

# Without temp variable
      
a = 5         
b = 10

a,b = b,a


#10. Write a python program to find whether a given number is even or old,
#print out an appropriate message to the user.

number1 = int(input("Enter a number:"))

if number1 < 6:
    print(number1, "is even")
else:
    print(number1,"is odd")


#11. Write a python program to test whether a passed letter is a vowel or not.

letter_Bhavya = input("Enter a letter:")

if letter_Bhavya in 'aeiouAEIOU':
    print("is a vowel ")
else:
    print("is not a vowel")



#12. Write a python program to sum of three given integers . However,
#if two values are equal,sum will be zero.

L1 = int(input("Enter a number"))
L2 = int(input("Enter a number"))
L3 = int(input("Enter a number"))

if L1==L2 or L1==L3 or L2==L3 :
    print("sum zero")
elif L1+L2+L3 :
    print("sum is")

#13. Write a Python program that will return true if the two given 
#integer values are equal or their sum or difference is 5. 

x = int(input("print1"))
y = int(input("print2"))

if x==y or x+y==5 or x-y==5:
    print("true")
else:
    print("false")

#14. Write a python program to sum of the first n positive integers. 
    

n = int(input("Enter a positive integer: "))
sum = 0
for i in range(1,n+1):
    sum=sum+i
print("The sum of the first", n, "positive integers is", sum_of_n_integers(n))


#15. Write a Python program to calculate the length of a string.

def string_length(str1 ):
    count = 0
    for char in str1:
        count += 1
    return count
string = input("Enter a string: ")
length = string_length(string)
print("Length of the string is:", length)

#16. Write a Python program to count the number of characters 
(character frequency) in a string
def char_frequency(string2):
  freq = {}
  for char in string2:
    if char in freq:
      freq[char] += 1
    else:
      freq[char] = 1
  return freq
    
string2 = "Bhavya"
print(char_frequency(string2))
    
    
 
#17. What are negative indexes and why are they used? 

""""Negative indexes in Python allow you to access elements from the end of a sequence (like a string or list). For example, -1 refers to the last element, -2 refers to the second-to-last element, and so on. They're useful for accessing elements from the end without knowing the exact length of the sequence."))18. Write a Python program to count occurrences of a substring in a string. """"


#18. Write a Python program to count occurrences of a substring in a string. 


def count_substring(string, sub_string):
  return string.count(sub_string)

print(count_substring("Bhavya, Patel!","P"))




#19. Write a Python program to count the occurrences of each word in a
#given sentence.




 def count_words(sentence):

  words = sentence.split()  
  word_counts = {}         

  for word in words:
    word = word.lower()  
    if word in word_counts:
      word_counts[word] += 1
    else:
      word_counts[word] = 1

  return word_counts


sentence = "bhavya m patel."
word_counts = count_words(sentence)
print(word_counts)   


#20. Write a Python program to get a single string from two given strings, 
#separated by a space and swap the first two characters of each string.


new_str1 = 'Ankita'[:2] + 'Manan'[2:]
new_str2 = 'Manan'[:2] + 'Ankita'[2:]
print(new_str1 + ' ' + new_str2)
    

"""21.  Write a Python program to add in at the end of a given string (length 
should be at least 3). If the given string already ends with 'ing' then 
add 'ly' instead if the string length of the given string is less than 3, 
leave it unchanged. """

def Bhavya(str1):
  if len(str1)<3:
    return str1
  elif str1.endswith('ing'):
    return str1+'ly'
  else:
    return str1+'ing'  

print(Bhavya('abc'))
print(Bhavya('string'))  
  

#22. Write a Python function to reverses a string if its length is a multiple of 4. 

def Bhavya_reverse(str1):
  if len(str1) % 4 == 0:
    return str1[::-1]
  else:
    return str1  
print(Bhavya_reverse('abcd'))
print(Bhavya_reverse('abc'))


"""23. Write a Python program to get a string made of the first 2 and the last 
2 chars from a given a string. If the string length is less than 2, return 
instead of the empty string."""


def Bhavya_first_last(str_tt):
  if  len(str_tt)<2:
    return '' 
  else:
    return str_tt[:2] + str_tt[-2:]
print(Bhavya_first_last('ab'))
print(Bhavya_first_last('abcdef'))



#24. Write a Python function to insert a string in the middle of a string. 


def bhavya_patel(tt,rr):
  mid_index = len(tt) //2
  return  tt[:mid_index] + rr + tt[mid_index:]

print(bhavya_patel('{{}}','Rutvik'))  


#25. What is List? How will you reverse a list? 

"""A list is a data structure in Python that can store a collection of items.
To reverse a list, you can use the reverse() method."""

bhavya2 = [1, 2, 3]
bhavya2.reverse()
print(bhavya2)     


#26. How will you remove last object from a list?

gg = [1, 2, 3] 
gg.pop(2)
print(gg) 


#27. Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]? 

 #list1[-1] will return the last element of the list, which is 25.

yy = [2, 33, 222, 14, 25]
hh = yy[-1]
print(hh)


#28. Differentiate between append() and extend() methods?



 append() adds a single element
Add = [3,4,5]
Add.append(6)
print(Add)

 #extend() adds multiple elements from another iterable

Add = [3,4,5]
tt = [6,7]
Add.extend(tt)
print(Add)


#29. Write a Python function to get the largest number, smallest num 
#and sum of all from a list. 


lst=[20,60,40,30] 
print('largest',max(lst))
print('smallest',min(lst))
print('total',sum(lst))


#30. How will you compare two lists? 


#1. Equality


list1 = [1, 2, 3]
list2 = [1, 2, 3]
if list1 == list2:
  print('equal to')
else:
  print('not equal')  

#2. Length


list1 = [1, 2, 3]
list2 = [4, 5]
if len(list1) == len(list2):
    print("Lists have the same length")   
else:
    print("Lists have different lengths")   


#3. Membership


list1 = [1, 2, 3]
   
if 2 in list1:
       print("2 is in list1")
else:
       print("2 is not in list1")






#32. Write a Python program to remove duplicates from a list.

numbers = {1, 2, 2, 3, 4, 4, 5}


print(numbers)






#33. Write a Python program to check a list is emp

def Bhavya(hhh):
    return not hhh
    
kriti=[]
manan=[1,2,3]
print(Bhavya(kriti))
print(Bhavya(manan))
     

#34. Write a Python function that takes two lists and returns true if they 
#have at least one common member.   

def common(list1,list2):
  for element in list1:
    if element in list2:
      return 'true'
  return 'false'  

dss = [1,2,3,4,5]
hhh = [5,6,7,8,9]
jjj = [10,11,12]
print(common(dss,hhh))
print(common(dss,jjj))






#36. Write a Python function that takes a list and returns a new list with 
#unique elements of the first list.

def unique_elements(list1):
  return list(set(list1))


numbers = [1, 2, 2, 3, 4, 4, 5]
print(unique_elements(numbers)) 


#37. Write a Python program to convert a list of characters into a string. 

chars = ['H', 'e', 'l', 'l', 'o']
print(''.join(chars))



#38. Write a Python program to select an item randomly from a list. 

import random

Anjana = [1, 2, 2, 3, 4, 5]
print(random.choice(Anjana))



#39. Write a Python program to find the second smallest number in a list. 

def second_small(ert):
  unique_list = sorted(set(ert))
  if len(unique_list) < 2:
    return None
  return unique_list[1]

ert = [1, 2, 2, 3, 4, 5]
print(second_small(ert))






#40. Write a Python program to get unique values from a list.


def get_unique_values(my_list):
    return list(set(my_list))

my_list = [1, 2, 2, 3, 4, 5]
print(get_unique_values(my_list))  






#41. Write a Python program to check whether a list contains a sublist.

    
Bhavya_list = [1, 2, 3, 4, 5]
sub_list = [2, 8]
for i in range(len(Bhavya_list) - len(sub_list) + 1):
  if Bhavya_list[i:i+len(sub_list)] == sub_list:
    print(True)
    break
else:
    print(False)



#42. Write a Python program to split a list into different variables.

Dharmik = [4,5,6,7]
a,b,c,d = Dharmik
print(a)
print(b)
print(c)
print(d)




#43. What is tuple? Difference between list and tuple.


#A tuple is an ordered, immutable sequence of elements. 
#The key difference between a list and a tuple is that lists are mutable, 
#while tuples are immutable (cannot be changed).




#44. Write a Python program to create a tuple with different data types. 

my_tuple = (1, "Hello", 3.14)
print(my_tuple) 
print(type(my_tuple))



#45. Write a Python program to unzip a list of tuples into individual lists. 


Bhavya_rr = [(1, 'a'), (2, 'b'), (3, 'c')]
list1, list2 = zip(*Bhavya_rr)
print(list1)  
print(list2) 
print(type(Bhavya_rr))



#46. Write a Python program to convert a list of tuples into a dictionary. 

a = [("a", 1), ("b", 2), ("c", 3)]
res = dict(a)
print(res)



#47. How will you create a dictionary using tuples in python?

manan = (("x", 10), ("y", 20))
manan = dict(manan)
print(manan)




#48. Write a Python script to sort (ascending and descending) a 
#dictionary by value.


Bhavya_oo = {"a": 3, "b": 1, "c": 2}

# Ascending sort
asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(asc_sorted)  

# Descending sort
desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(desc_sorted)  


#49. Write a Python script to concatenate following dictionaries to create a new one. 


dict6  = {"a": 1, "b": 2}
dict7  = {"c": 3, "d": 4}
Bhavya4 = {**dict6,**dict7}
print(Bhavya4)



#50. Write a Python script to check if a given key already exists in a dictionary. 

Bhavya_dict = {"a": 1, "b": 2, "c": 3}
Bhavya_check = "c"
if Bhavya_check in Bhavya_dict:
  print("Key exists")
else:
    print("Key does not exist")


     

#51. How Do You Traverse Through a Dictionary Object in Python?

Bhavya_dict = {"a": 1, "b": 2, "c": 3}

# Using .items()
for b, value in Bhavya_dict.items():
    print(b, value)

# Using .keys()
for key in Bhavya_dict.keys():
    print(key)

# Using .values()
for value in Bhavya_dict.values():
  print(value)

    
    
    
#52. How Do You Check the Presence of a Key in A Dictionary?

Bhavya_dict = {"a": 1, "b": 2, "c": 3}
Bhavya_check = "a"
if Bhavya_check in Bhavya_dict:
  print("Key exists")
else:
    print("Key does not exist")


#53. Write a Python script to print a dictionary where the keys are numbers between 1 and 15. 

Manan = {i:i**2 for i in range(1,16)}
print(Manan)



#54. Write a Python program to check multiple keys exists in a dictionary alu

def check_multiple_keys(Gita, keys_to_check):


    for key in keys_to_check:
        if key not in Gita:
            return False
    return True

Gita = {'a': 1, 'b': 2, 'c': 3}
print(check_multiple_keys(Gita, ['a', 'b']))
print(check_multiple_keys(Gita, ['a', 'd']))




#55. Write a Python script to merge two Python dictionaries 

dict6  = {"a": 1, "b": 2}
dict7  = {"c": 3, "d": 4}
Bhavya4 = {**dict6,**dict7}
print(Bhavya4)



#56. Write a Python program to map two lists into a dictionary 
Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).



def Anjana(list1,list2):
  return dict(zip(list1,list2))

list1 = ["x","y","z"]
list2 = [1,2,3]
print(Anjana(list1,list2))


#57. Write a Python program to find the highest 3 values in a dictionary

from collections import Counter
def Sonnnn(dict1):
  return dict(Counter(dict1).most_common(4))

Sonnnn_disc = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
print(Sonnnn(Sonnnn_disc))




#59. Write a Python program to create a dictionary from a string. 
#Note: Track the count of the letters from the string. 


def Bhavya_from_string(string):
    result = {}
    for char in string:
        result[char] = result.get(char, 0) + 1
    return result

sample = 'Bhavya'
print(Bhavya_from_string(sample))



"""60. Sample string:
 w3resource' Expected output:
• {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}"""


def count_characters(string):
  Counts the occurrences of each character in a string.

  char_count = {}
  for char in string:
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1

  return char_count

string = 'w3resource'
print



#61) Write a Python function to calculate the factorial of a number (a nonnegative integer)
def factorial(n):
if n == 0:
return 1
else:
return n * factorial(n-1)
print(factoria(5))


  
  
#62) Write a Python function to check whether a number is in a given range


def Bhavya_range(n, start, end):
  return n in range(start, end+1)
print(Bhavya_range(5, 1, 100))
print(Bhavya_range(15, 1, 100))



#63) Write a Python function to check whether a number is perfect or not.
def Bhavya_e(n):
  if n <= 1:
    return False  

  sum_of_divisors = 1  

  for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            sum_of_divisors += i
            if i * i != n:  
                sum_of_divisors += n // i

  return sum_of_divisors == n


print(Bhavya_e(6))   
print(Bhavya_e(28))  
print(Bhavya_e(12))  
print(Bhavya_e(496)) 
print(Bhavya_e(8128)) 



#64) Write a Python function that checks whether a passed string is palindrome or not

def is_palindrome(s):
   
    
    s = s.lower() 
    return s == s[::-1]


print(is_palindrome("મલયાલમ"))  
print(is_palindrome("ગુજરાત"))  
print(is_palindrome("નયન")) 



                    
#65. How Many Basic Types of Functions Are Available in Python?

"""There are two basic types of functions available in Python:

Built-in Functions: These functions are already defined in Python and are always available. Examples include print(), len(), and range().

User Defined Functions: These functions are created by the user and used to perform specific tasks."""



#66) How can you pick a random item from a list or tuple?

import random 
Anjana = [1,2,3,4,5]
print(random.choice(Anjana))



#67) How can you pick a random item from a range?

kavya = random.randrange(1,10)
print(kavya)


#68) How can you get a random number in python?

import random
Random_number = random.random()
print(Random_number)

#69) How will you set the starting value in generating random numbers?


random.seed(10)
print(random.random())



#70) How do you randomize the items of a list in place?

Sager = [1,2,3,4,5]
random.shuffle(Sager)
print(Sager)



""""71) What is a File function in Python? What are keywords to create and write a file?
● File function: In Python, file functions are used to interact with files on your computers
file system. This includes tasks like opening files, reading their contents, writing to them,
and closing them.
● Keywords:
○ open(): This is the primary function to open a file. You specify the file name and the
mode (e.g., 'r' for reading, 'w' for writing, 'a' for appending).
○ with: It's best practice to use the with statement when working with files. It ensures
that the file is automatically closed, even if errors occur.
○ write(): Used to write data to a file.""""




#72) Write a Python program to read an entire text file.
tt = open(r"Bhavya.txt","r")
tt.read()
tt.close()



#73) Write a Python program to append text to a file and display the text.

tt =open(r"Bhavya.txt","r+")
tt.write("Hello Dosto")
tt.close()
tt =open(r"Bhavya.txt","r+")
tt.read()


#74) Write a Python program to read the first n lines of a file.

tt =open(r"Bhavya.txt","r+")
tt.readline()


#75) Write a Python program to read the last n lines of a file.

tt =open(r"Bhavya.txt","r")
ff = tt.readlines()[-1]
print(ff)


#76) Write a Python program to read a file line by line and store it into a list.

tt =open(r"Bhavya.txt","r+")
ll = []
for i in tt:
  ll.append(i.strip())
print(ll)  


#77) Write a Python program to read a file line by line and store it into a variable.

tt= open(r"Bhavya.txt","r+")
uu =""
for i in tt:
  uu=uu+i
print(uu)  


#78) Write a python program to find the longest words. 


def find_longest_words(filename):
    longest_words = []
    max_length = 0     
    with open(filename, 'r') as file: 
        for line in file:           
            words = line.split()      
            for word in words:        
                word = word.strip('.,!?"').lower() 
                if len(word) > max_length:        
                    max_length = len(word)        
                    longest_words = [word] 
                elif len(word) == max_length:      
                    longest_words.append(word) 
    return longest_words                                       
longest = find_longest_words('Bhavya.txt')                     
print(longest)                        



#79) Write a Python program to count the number of lines in a text file.

tt = open(r"Bhavya.txt","r+")
hh = sum(1 for line in tt)
print(hh)


#80) Write a Python program to count the frequency of words in a file.

from collections import Counter
word_counts = Counter()
with open('Bhavya.txt', 'r') as file:
    for line in file: 
        words = line.split()  
        for word in words:  
            word = word.strip('.,!?"').lower()  
            word_counts[word] += 1  
print(word_counts)



#81) Write a Python program to write a list to a file.

my_list = ["apple", "banana", "cherry"]
with open('Bhavya.txt', 'w') as file:
   for item in my_list:
    file.write(item + "\n")



#82) Write a Python program to copy the contents of a file to another file.

with open('source.txt', 'r') as source_file, open('destination.txt',
'w') as dest_file:
for line in source_file:
dest_file.write(line)



"""83) Explain Exception handling? What is an Error in Python?
● Exception handling: It's a way to gracefully manage errors that might occur during the
execution of your program. Instead of the program crashing, you can handle the error and
potentially take corrective actions.
● Error: An error is an issue that prevents your program from running correctly. It could be a
syntax problem, a runtime issue (like dividing by zero), or something else."""



"""84) How many except statements can a try-except block have? Name some built-in
exception classes."""

"""● You can have multiple except statements in a try-except block to handle different types of
exceptions.
● Built-in exception classes:
○ ZeroDivisionError
○ TypeError
○ ValueError
○ FileNotFoundError
○ IOError"""



#85) When will the else part of try-except-else be executed?

#The else block is executed if no exceptions occur in the try block.



#86) Can one block of except statements handle multiple exceptions?
#Yes, you can use a tuple of exceptions in a single except block:
try:
# Some code
except (TypeError, ValueError) as e:
print("Caught either a TypeError or ValueError:", e)



#87) When is the finally block executed?

"""The finally block is always executed, whether an exception occurred or not. It's often used for
cleanup tasks (like closing files)."""


#88) What happens when "1" + 1 is executed?

"""This will result in a TypeError. You can't directly add a string ("1") and an integer (1). Python will
try to concatenate them, but it won't work as intended."""



#89) How Do You Handle Exceptions with Try/Except/Finally in Python? Explain withcoding snippets.

try:
    result = 10 / 0  
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
finally:
    print("This block always executes.")


#90) Write a Python program that prompts the user to enter only odd numbers, else willraise an exception.
while True:
try:
num = int(input("Enter an odd number: "))
if num % 2 == 0:
raise ValueError("Even numbers are not allowed.")
else:
print("Thank you for entering an odd number.")
break # Exit the loop if an odd number is entered
except ValueError as e:p