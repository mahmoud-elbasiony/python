# 1-​ Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them.
def get_name():
    first_name=input("\n\nEnter first name\n")
    last_name=input("\n\nEnter last name\n")
    print(last_name+" "+first_name)

get_name()
print("=============================================")

# 2- Write a Python program that accepts an integer (n) and computes the value of
# n+nn+nnn.


def value_of_nnn():
    n=int(input("\n\nEnter number\n"))
    print("n+nn+nnn\n")
    print(n+n*n+n*n*n)

value_of_nnn()
print("=============================================")

# 3- Write a Python program to print the following here document.
# Sample string ​ :

def print_multi_line_string():
    multi_line_string="""\na string that you "don't" have to escape
    This
    is a ....... multi-line
    heredoc string --------> example"""

    print(multi_line_string)

print_multi_line_string()
print("=============================================")

# 4- Write a Python program to get the volume of a sphere with radius 6.
import math

def sphere_volume(radius=6):
    volume=(4/3)*math.pi*pow(radius,3)
    print(f"sphere_volume ={volume}")

sphere_volume()
print("=============================================")

# 5- Write a Python program that will accept the base and height of a triangle and compute
# the area.

def triangle_area(base=1,height=1):
    area=.5*base*height
    print(area)

triangle_area()
print("=============================================")

# 6- Write a Python program to construct the following pattern, using a nested for loop.
# Search about method

def print_shape(n=10):
    for i in range(1,n):
        if i<n/2+1:
            print("* "*i)
        else:
            print("* "*(n-i))

print_shape(10)
print("=============================================")

# 7- Write a Python program that accepts a word from the user and reverse it.

def reverse_word():
    word=input("\n\nEnter Word\n")
    print(word[::-1])

reverse_word()
print("=============================================")


# 8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

def print_nums():
    for i in range(1,7):
        if i==3 or i==6:
            continue
        print(f"{i}, ")

print_nums()
print("=============================================")
# 9-Write a Python program to get the Fibonacci series between 0 to 50

def Fibonacci(n=50):
    prev=0
    next=1
    print(prev)
    while next<50:
        print(next)
        temp=next
        next=prev+next
        prev=temp

Fibonacci()
print("=============================================")

# 10- Write a Python program that accepts a string and calculate the number of digits and
# letters.

def count(text):
    digits=0
    chars=0
    for i in range(len(text)):
        if text[i].isdigit():
            digits+=1
        elif text[i].isalpha():
            chars+=1
    
    print(f"digits count= {digits}, chars count = {chars}")

count("akdha$65")
print("=============================================")

