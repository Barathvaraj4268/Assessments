# -*- coding: utf-8 -*-
"""python_internal_assessment_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y9Lyh1Q7QieJwgowBd6yIE65dTtcuu_7
"""

#1

length=float(input("Enter length of rectangle: "))
breadth=float(input("Enter breadth of rectangle: "))
area=length*breadth
print("Area of Rectangle: "+str(area))

#2

weight=float(input("Enter weight in kg: "))
height=float(input("Enter height in m: "))

bmi=weight/(height**2)

print("Your Body Mass Index (MBI) is "+str(bmi))

#3

n=int(input("Enter number of students to store: "))
student_dict={}
for i in range(n):
  student=input("Enter student "+str(i+1)+" name: ")
  score=input("Enter student "+str(i+1)+" score: ")
  student_dict[student]=score
print(student_dict)

#4

age=int(input("Pleas enter your current age: "))

if age<18:
  print("You are a minor")
elif age in range(18,60):
  print("You are an adult")
else:
  print("You are a senior")

#5
even_numbers=[]
for i in range(2,51,2):
  even_numbers.append(i)
print(even_numbers)

#6
password="correct_password"
wrong_password=input("Enter correct password: ")
while(wrong_password!=password):
  wrong_password=input("Wrong! Enter correct password: ")
print("Yes! password is correct")

#7

def average_of_numbers(number_list):
  return sum(number_list)/len(number_list)

number_list=[]
n=int(input("Enter the how many numbers: "))
for i in range(n):
  num=float(input("Enter number "+str(i+1)+": "))
  number_list.append(num)
average_number=average_of_numbers(number_list)
print("Average of given numbers is "+str(average_number))

#8

string=input("Enter string to count vowels: ")
vowels=['a','A','e','E','i','I','o','O','u','U']
sum_v=0
for i in string:
  if i in vowels:
    sum_v+=1
print("Total number of vowels in the string is "+str(sum_v))

#9

import datetime
print(datetime.datetime.today())

#10

try:
  num1=int(input("Enter number 1: "))
  num2=int(input("Enter number 2: "))
  sum=num1+num2
  print(sum)
except:
  print("Please enter only integer and not any other datatype")

#11
try:
  integer=int(input("Enter any integer: "))
  print(integer)
except:
  print("Please enter correct integer")

#12
def div_by_zero(num1, num2):
  try:
    quotient=num1/num2
    return quotient
  except:
    return "Denominator must not be 0"

num1=int(input("Enter numerator: "))
num2=int(input("Enter denominator: "))
quotient=div_by_zero(num1,num2)
print(quotient)

#13

with open("/content/drive/MyDrive/Colab Notebooks/ftp.txt","w") as write_file:
  text="Hello, Python!\n"
  write_file.writelines(text)
  print("File written successfully")

#14
with open("/content/drive/MyDrive/Colab Notebooks/ftp.txt","r") as read_file:
  read=read_file.read()
  print(read)

#15
with open("/content/drive/MyDrive/Colab Notebooks/ftp.txt","w") as write_file:
  new_line="\nThis is new line"
  nl=text+new_line
  write_file.writelines(nl)

with open("/content/drive/MyDrive/Colab Notebooks/ftp.txt","r") as read_file:
  read=read_file.read()
  print(read)