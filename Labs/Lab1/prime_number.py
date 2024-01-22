# Lab1: This Python script returns True if it is a prime number and False if it is not a prime number

# Author: Anders Grahn
# Date: 2024-01-21

# Returns true if it is a prime number
def check_if_prime_number(number):
  
  # Only numbers higher than 1 can be prime numbers
  if number < 2:
    return False
  
  # 2 is the only even prime number so just return True if the user inputs 2
  if number == 2:
    return True

  # Here we check if it is an even number (even numbers cannot be prime numbers)
  if (number % 2) == 0:
    return False

  # Here we create a range of numbers to be tested
  numbers_to_test = range(2, round(number)) # Since we start on zero the last number is not included, and we round our float (divided value) so it becomes an int

  # Here we keep track of all odd numbers to divide with the user input
  my_odd_numbers = []

  # Here we go through the range, and keep track of all odd numbers
  for i in numbers_to_test:
    # And we only keep odd numbers to test with
    if (i % 2) == 1:
      my_odd_numbers.append(i)

  # Here we take half of the user input value and test against the remaning odd numbers
  for i in my_odd_numbers:
    #print(number)
    #print(i)
    divided_number = number / i
    #print("divided:{0}".format(divided_number))
    #Here we check if the result is without decimals (int)
    if divided_number.is_integer():
      return False

  # All the tests passed so this is a prime number
  return True