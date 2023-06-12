# Session 2 Exercises

from statistics import mean

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.

# width = 3
# height = 4
# area = width * height
# print("Rectange of width " + str(width) + " and height " + str(height) + ", has an area of " + str(area))


# 2. Write code that prints the length of the string, 'python'.

# string = "python"
# string_length = len(string)
# print(string_length)


# 3. Print out the first and third letter of the word 'python'.

# string = "python"
# print(string[0])
# print(string[2])


# 4. Ask the user to enter their name, and print out `Hello, <name>`.

# name = input("What is your name? ")

# print("Hello, " + name)


# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.

# age = int(input("What is your age? "))
# age_in_15_years = age + 15
# print("In 15 years time, you will be " + str(age_in_15_years) + " years old.")


# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.

# print("Hello " + name + ", you are currently " + str(age) + " years old. In 15 years time, you will be " + str(age_in_15_years) + " years old.")

# 7. Ask the user to enter their hometown, print it out in uppercase letters.

# hometown = input("What is your hometown? ")
# print(hometown.upper())

# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.

# fav_colour = input("What is your favourite colour? ")
# fav_colour_length = len(fav_colour)
# print(str(fav_colour_length))

# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.

# weather = input("What is the weather like? ")
# month = input("What month is it? ")

# print("It is " + month + " and it is " + weather.lower() + " today.")


# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.

# temperature_1 = int(input("Please enter a temperature from this month, in degrees Celcius: "))
# temperature_2 = int(input("Please enter a temperature from this month, in degrees Celcius: "))
# temperature_3 = int(input("Please enter a temperature from this month, in degrees Celcius: "))
# temperature_4 = int(input("Please enter a temperature from this month, in degrees Celcius: "))
# temperature_5 = int(input("Please enter a temperature from this month, in degrees Celcius: "))

# avg_temp = (temperature_1 + temperature_2 + temperature_3 + temperature_4 + temperature_5)/5

# print(str(avg_temp))

# print("It is " + month + " and the average temperature is " + str(avg_temp) + " degrees celsius.")

# 11. Print out the above sentence but make the month upper case.

# print("It is " + month.upper() + " and the average temperature is " + str(avg_temp) + " degrees celsius.")

# 12. Create a variable that holds your favourite animals and print it out. 
#    Make sure the animals are all on different lines and tabbed.

# fav_animals = "\tcats,\n\tdogs,\n\tlion"

# print(str(fav_animals))


# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.

# name = input("What is your name? ")
# number = int(input("Enter a number between 1 and the length of your name: "))
# print((name[number-1].upper()))


# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".

string = "WelcometoPython"[1:-1:2]
print(string)

# creating a variable with the string in 
str = "WelcometoPython"

# finding out the length of the string to decide which characters to exclude 
print(len(str))

# slicing the string with steps of 2, excluding the first and last character
print(str[1:14:2])