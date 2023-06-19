# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".
# name = input("What is your name? ")

# if name == "Bob":
#   print("Welcome " + name + "!")


# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".

# name = input("What is your name? ")

# if name != "Alice":
#   print("You're not Alice!")



# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure".

# password = input("Please enter a password: ")

# if password == "qwerty123":
#   print("You have successfully logged in")
# else:
#   print("Password failure")



# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#   print("Even")
# else:
#   print("Odd")

# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"

# number_1 = int(input("Please choose a number: "))
# number_2 = int(input("Please choose another number: "))

# if number_1 + number_2 > 21:
#   print("Bust")
# else:
#   print("Safe")


# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.

# length = int(input("Enter a length of a shape: "))
# width = int(input("Enter a width of a shape: "))

# if length == width:
#   print("The shape is a square")
# else:
#   print("The shape is not a square")

# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. 
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

# salary = int(input("Please enter your salary: £"))
# years_of_service = float(input("How many years have you worked here? "))

# if years_of_service > 3:
#   print("Your salary is £" + str(salary) + " and your bonus is £" + str(salary * 0.1))
# else:
#   print("Your salary is £" + str(salary) + " no bonus")


# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.

# number = int(input("Enter a whole number: "))

# if number > 0:
#   print(str(number ** 3))
# else:
#   print(str(number / 2))


# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", 
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".

# name = input("What is your name? ")

# if name == "Alice":
#   print("Hello, Alice")
# elif name == "Bob":
#   print("You're not Bob! I'm Bob")
# else:
#   print("You must be Charlie")


# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"

# age = int(input("Please enter your age: "))

# if age == 0:
#   print("You're not born yet!")
# elif age < 11:
#   print("You're too young to go to this school")
# elif 11 < age < 16:
#   print("You can come to this school")
# else:
#   print("You're too old for this school")

# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".

# month = input("Please enter a month: ")

# if month == "March" or month == "April" or month == "May":
#   print(month + " is in Spring")
# else:
#   print("I don't know")

# if month == "December" or month == "January" or month == "February":
#   print(month + " is in Winter")
# elif month == "March" or month == "April" or month == "May":
#   print(month + " is in Spring")
# elif month == "June" or month == "July" or month == "August":
#   print(month + " is in Summer")
# elif month == "September" or month == "October" or month == "November":
#   print(month + " is in Autumn")
# else:
#   print("I don't know")


# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.

# number_1 = int(input("Enter a number: "))
# number_2 = int(input("Enter another number: "))

# if number_1 % 2 == 0 and number_2 % 2 == 0:
#   print("Both numbers are even")
# elif number_1 % 2 != 0 and number_2 % 2 != 0:
#   print("Both numbers are odd")
# else:
#   print(str(number_1 * number_2))

# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.

# number_1 = int(input("Enter a number: "))
# number_2 = int(input("Enter another number: "))

# if number_1 > number_2:
#   print(str(number_1) + " is higher than " + str(number_2))
# else:
#   print(str(number_2) + " is higher than " + str(number_1))


# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, 
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. 
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

# salary = int(input("What is your current salary? £"))
# years_of_service = int(input("How many years have you worked here? "))

# if years_of_service > 7:
#   print("Your current salary is £" + str(salary) + ", and your bonus is £" + str(salary * 0.2))
# elif years_of_service > 5 and years_of_service <= 7:
#   print("Your current salary is £" + str(salary) + ", and your bonus is £" + str(salary * 0.15))
# elif years_of_service >= 3 and years_of_service <= 5:
#   print("Your current salary is £" + str(salary) + ", and your bonus is £" + str(salary * 0.1))
# else:
#   print("Your current salary is £" + str(salary) + ", and you do not get a bonus")


# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. 
#   If all three ages are the same, print that.

# name_1 = input("Enter a name: ")
# age_1 = int(input("How old is " + name_1 + "? "))
# name_2 = input("Enter another name: ")
# age_2 = int(input("How old is " + name_2 + "? "))
# name_3 = input("Enter another name: ")
# age_3 = int(input("How old is " + name_3 + "? "))

# if age_1 > age_2 and age_1 > age_3 and age_2 > age_3:
#   print(name_1 + " is the oldest, and " + name_3 + " is the youngest")
# elif age_1 > age_2 and age_1 > age_3 and age_3 > age_2:
#   print(name_1 + " is the oldest, and " + name_2 + " is the youngest")
# elif age_2 > age_1 and age_2 > age_3 and age_1 > age_3:
#   print(name_2 + " is the oldest, and " + name_3 + " is the youngest")
# elif age_2 > age_1 and age_2 > age_3 and age_3 > age_1:
#   print(name_2 + " is the oldest, and " + name_1 + " is the youngest")
# elif age_3 > age_1 and age_3 > age_2 and age_1 > age_2:
#   print(name_3 + " is the oldest, and " + name_2 + " is the youngest")
# elif age_3 > age_1 and age_3 > age_2 and age_2 > age_1:
#   print(name_3 + " is the oldest, and " + name_1 + " is the youngest")
# else:
#   print("They are all the same age!")


# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

lesson_1 = input("Please enter one of your lessons: ")
mark_1 = int(input("What mark did you get in " + lesson_1 + "? "))
lesson_2 = input("Please enter another one of your lessons: ")
mark_2 = int(input("What mark did you get in " + lesson_2 + "? "))
lesson_3 = input("Please enter another one of your lessons: ")
mark_3 = int(input("What mark did you get in " + lesson_3 + "? "))

if mark_1 >= 80:
  print("You got an A in " + lesson_1)
elif mark_1 < 80 and mark_1 >=60:
  print("You got a B in " + lesson_1)
elif mark_1 < 60 and mark_1 >= 50:
  print("You got a C in " + lesson_1)
elif mark_1 < 50 and mark_1 >= 45:
  print("You got a D in " + lesson_1)
elif mark_1 < 45 and mark_1 >= 25:
  print("You got a E in " + lesson_1)
else:
  print("You got an F in " + lesson_1)

if mark_2 >= 80:
  print("You got an A in " + lesson_2)
elif mark_2 < 80 and mark_2 >=60:
  print("You got a B in " + lesson_2)
elif mark_2 < 60 and mark_2 >= 50:
  print("You got a C in " + lesson_2)
elif mark_2 < 50 and mark_2 >= 45:
  print("You got a D in " + lesson_2)
elif mark_2 < 45 and mark_2 >= 25:
  print("You got a E in " + lesson_2)
else:
  print("You got an F in " + lesson_2)

if mark_3 >= 80:
  print("You got an A in " + lesson_3)
elif mark_3 < 80 and mark_3 >=60:
  print("You got a B in " + lesson_3)
elif mark_3 < 60 and mark_3 >= 50:
  print("You got a C in " + lesson_3)
elif mark_3 < 50 and mark_3 >= 45:
  print("You got a D in " + lesson_3)
elif mark_3 < 45 and mark_3 >= 25:
  print("You got a E in " + lesson_3)
else:
  print("You got an F in " + lesson_3)