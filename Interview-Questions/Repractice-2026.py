# # # Input a year and find whether it is a leap year or not.
# year = int(input('input the year: '))
# if year % 400==0 or year % 4==0 and year % 100!=0:
#     print(f'{year} is a leap year')
# else:
#     print(f'{year} is not a leap year')
#
# # # Take two numbers and print the sum of both.
# num1 = int(input('input the number: '))
# num2 = int(input('input the number: '))
# print(f'Sum is {num1+num2}')
#
#
# # #  Take a number as input and print the multiplication table for it.
# number= int(input('Enter the number: '))
# i = 1
# while i<=20:
#     print(f'{i}*{number}={i*number}')
#     i+=1
#
# # #  Keep taking numbers as inputs till the user enters ‘x’, after that print sum of all.
# outnumbers=0
# number = input('Enter a number: ')
# while number !='x':
#     outnumbers += int(number)
#     number = input('Enter a number: ')
# print(outnumbers)
#
# # # Take 2 numbers as inputs and find their HCF and LCM.
# number_one = int(input("Enter First Number"))
# number_second = int(input("Enter Second Number"))
# remainder = 1
#
# if number_one <= number_second:
#     number_one, number_second = number_second, number_one
#
# while number_second != 0:
#     remainder   =   number_one % number_second
#     print(f"{remainder} is the remainder")
#     number_one = number_second
#     number_second=remainder
