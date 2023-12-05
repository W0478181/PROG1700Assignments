#Author: Aiden Connolly
#Student ID: W0478181
#Course: IT Generalist
#Date: 11/28/2023
#Project:Python exercises
#Version:Python

#STRINGS

#Concatenation
str1 = "hello, "
str2 = "world!"
result_str = str1 + str2
print(result_str)

#Substring
substr = "How to code for beginners"
print(substr[0:5])

#Formatting
str_f = "the code is {}, {}, {}."
print(str_f.format(263, 35, -160))

#LOOPS

#Print Numbers
for i in range(1,11):
    print(i)

#Factorial
n = 5
fac = 1
result = 1
while fac <= n:
    result *= fac
    fac += 1
print(result)

#SETS

#Intersection
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersectionset = set1.intersection(set2)
print(intersectionset)

#LISTS

#List Operations
list1 = [1, 2, 3, 4, 5, 6]
print(sum(list1))
print(sum(list1)/len(list1))
print(max(list1), min(list1))

#List Comprehension
squares = [x**2 for x in range(1, 11)]
print(squares)

#TUPLES

#Tuple Unpacking
tuple = ("money", "dollars", "bucks")
(one, two, three) = tuple
print(one)
print(two)
print(three)

#DICTIONARIES

#Operations Dictionary
dict1 = {"name": "aiden", "age": 19, "city": "st.andrews"}
for key, value in dict1.items():
    print(f"{key}: {value}")

#Nested Dictionary
dict2 = {
    "bryan": {"gr1": 42, "gr2": 10},
    "joe": {"gr1": 69, "gr2": 68}
}

for student, grades in dict2.items():
    avg_grade = sum(grades.values()) / len(grades)
    print(f"{student}'s average grade: {avg_grade}")

#FUNCTIONS

#Function basics
def Func(x, y):
    print(x+y)

Func(20, 30)

#Default Values
def defval(x = 69, y = 420):
    print(x+y)

defval()

#Read/Write External Files

#Read Files
z = open("sample.txt", "r")
print(z.read())

#Write FIles
a = open("output.txt", "x")

b = open('output.txt', 'w')
b.write('test')
b.close()

c = open('output.txt', 'r')
print(c.read())

#Avg func
numbers=[1,2,3,4,5]
total = 0
count = 0
avg = 0
for t in numbers:
    total += t
    count += 1
avg = total / count
print(avg)

#Max func
numbers = [1,2,3,4,5]
print(max(numbers))


#Min func
numbers = [1,2,3,4,5]
print(min(numbers))


numbers = [1,2,3,4,5]
numbers.sort(reverse=True)
print(numbers(0))

numbers = [2,5,3,1,4]
numbers.sort()
print(numbers[len(numbers)-1])

data_to_write = ["hello","world","python"]
try:
    with open ('output.txt','w') as file:
        for line in file:
            print(line)
except IOError:
    print("an error has occured while writing to the file")