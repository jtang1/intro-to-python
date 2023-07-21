# Session 4 Exercises

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.

# fruits = ["Apple", "Cherry", "Pear", "Pineapple", "Peach", "Mango"]

# print(fruits)


# 2. Add "Grapes" to the list and print the list.

# fruits.append("Grapes")
# print(fruits)


# 3. Change "Pears" to "Strawberries" and print the list.
# fruits[2] = "Strawberry"
# print(fruits)


# 4. Remove "Apples" from the list and print the list.

# del(fruits[0])
# print(fruits)

# 5. Print out the current length of the list.

# print(len(fruits))

# 6. Order the list alphabetically.

# fruits.sort()


# 7. Print out the list again.

# print(fruits)


# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.

# for fruit in fruits:
  # print(fruit)

# 2. Print the numbers 1 to 100 (including the number 100).

# for i in range(1,101):
#   print(i)


# 3. Print all odd numbers from 1 to 100.

# for i in range(1,101,2):
#   print(i)

# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).

# for i in range(1896,2023,4):
#   if i == 1916 or i == 1940 or i == 1944 or i == 2020:
#     print("The Olympics were not held in " + str(i))
#   else:
#     print(i)

# not_held = [1916, 1940, 1944, 2020]

# for olympic_year in range(1896, 2022, 4):
#     if olympic_year not in not_held:
#         print(olympic_year)

# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.


# randomlist = ["11", "21", "15", "47", "78", "27", "52", "13", "9", "98"]
# even = []
# odd = []

# for i in randomlist:
#   if int(i) % 2 == 0:
#     even.append("i")
#   else:
#     odd.append("i")

# print(len(even))
# print(len(odd))
  


# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.

# names = ["Alice", "Bob", "Charlie", "Dave", "Eric"]

# for i in names:
#   print("Hello " + i)

# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".

# word = "supercalifragilisticexpialidocious"

# for each_letter in word:
#   print(each_letter)


# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.

# numbers = [1, 15, 3, 11, 34]
# square_of_numbers = []

# for each_number in numbers:
#   square_of_numbers.append(each_number ** 2)

# print(square_of_numbers)

# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.

# names = ["Alice", "Bob", "Charlie", "Dave", "Eric"]

# dr = []

# for each_name in names:
#   dr.append("Dr. " + each_name)

# print(dr)

# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#    For numbers which are multiples of both three and five, print "FizzBuzz".

# for each_number in range(1,101):
#   if each_number % 5 == 0 and each_number % 3 == 0:
#     print("FizzBuzz")  
#   elif each_number % 3 == 0:
#     print("Fizz")
#   elif each_number % 5 == 0:
#     print("Buzz")
#   else:
#     print(each_number)

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```
