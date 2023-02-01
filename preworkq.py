def hello_name(user_name):
 #print(f'hello_{user_name}!') #f-string
 print(f'hello_' + user_name + '!')

#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
  for num in range(1,101):
   if num % 2 == 1:
    print(num)
#or num=1
while num <= 100
num

first_odd
 

 
 
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
 def max_num_in_list(a_list):
curr_max =a_list[0]

for num in a_list:
 if num > curr_max:
  curr_max = num

  return curr_max
 

 Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

    def is_leap_year(a_year):
     if a_year % 400:
      return True