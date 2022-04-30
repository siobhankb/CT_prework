#Question 1
#function to write "hello_USERNAME" 
def hello_name(user_name):
    uname = input("What is your name? ")
    print("Hello, " + uname + "!")
user_name = 'Siobhan'
hello_name = print("Hello, " + user_name)

#Question 2
#function to print odd numbers from 1-100
def first_odds():
    odd_numbers = list(range(1,101,2))
    print (odd_numbers)

#Question 3
#find max number in list
def max_num_in_list(a_list):

#Question 4
#tell if a given year is a leap year
def is_leap_year(a_year):
    if a_year %4 == 0 and a_year % 100 != 0 or a_year % 400 == 0:
        print(str(a_year) + " is, indeed, a leap year.\n")
    else:
        print(str(a_year) + " is NOT a leap year.\n")

year = input("\nType any year and I'll tell you if it's a LEAP year!  ")
is_leap_year(int(year))

#Question 5
#check if numbers in a list are consecutive
def is_consecutive(a_list):

#Question 6
