# Session 5 Exercises

## Section A
# 1. Print 10 random numbers.

# import random
# x = 0
# while x < 9:
#   print(random.randint(0, 100))
#   x += 1


# 2. Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!".
#     - Rewrite so that the number being guessed is a random value from 1 to 10 instead of number 7 .

# number = None

# while number != 7:
#   number = int(input("Enter a number: "))

# print("Wow, lucky number 7!")

# 3. The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre. 
#   E.g. 240cm x 80cm = 19200cm2 = 2m2.
# import math
# width = int(input("Enter a width in cm: "))
# length = int(input("Enter a height in cm: "))
# area_cm = width * length
# area_m = math.floor(area_cm/10000)

# print("The area is " +  str(area_m) + "m^2")


# 4. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure" and then ask them to enter it again. 
#   Only allow them to enter the password wrong 3 times before printing "System Locked!".

# password = None
# attempts = 0

# while attempts < 3:
#   if password != "qwerty123":
#     password = input("Please enter your password: ")
#     print("Password failure")
#     attempts += 1
#   else:
#     print("You have successfully logged in")
#     break

  
# if attempts == 3:
#   print("You have entered your password incorrectly 3 times.")
#   print("System Locked!")


# password = input("Please enter your password: ")
# correct_password = "qwerty123"
# attempts = 0

# while attempts <2:
#   if password == correct_password:
#     print("You have successfully logged in.")
#     break
#   else:
#     print("Password failure")
#     attempts += 1
#     password = input("Please enter your password: ")

# if attempts == 2:
#   print("System failure - you have entered your password incorrectly 3 times.")
    

# 5. Add up all the numbers from 1 to 500 and print the answer.

# number = 0
# sum = 0

# while number < 501:
#   sum = sum + number
#   number += 1

# print(sum)


# 6. Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list. 
#   Find the index at which the user entered the number 99.

# list = []

# index = 0

# while len(list) < 10:
#   user_input = list.append(int(input("Enter 10 numbers, one of which should be 99: ")))

# for each_number in list:
#   if each_number != 99:
#     index += 1
#   else:
#     print("99 is at index number " + str(index))
    
# 7. Print a multiplication table for the number 18 up to 15. E.g.
#     1 x 18 = 18
#     2 x 18 = 36


# for each_number in range(1, 16):
#   print(str(each_number) + " x 18 = " + str(each_number*18))

# i = 0

# while i < 15:
#   print(str(i) + " x 18 = " + str(i * 18))
#   i += 1

# 8. Print the numbers 1 to 100 (including the number 100) using a while loop.

# i = 0

# while i < 101:
#   print(i)
#   i += 1

# 9. Rewrite question B8 from session 3 using a while loop
#     - A school has following rules for their grading system:
#         a.	Above 80 – A
#         b.	60 to 80 – B
#         c.	50 to 60 – C
#         d.	45 to 50 – D
#         e.	25 to 45 – E
#         f.	Below 25 - F
#     Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

# lesson = None

# print("REPORT CARD:")

# while lesson != "":
#     lesson = input("Input your lesson:\n")
#     mark = int(input("Input your mark:\n"))
#     if mark > 80:
#         print(lesson + " - A grade")
#     elif mark <= 80 and mark > 60:
#         print(lesson + " - B grade")
#     elif mark <= 60 and mark > 50:
#         print(lesson + " - C grade")
#     elif mark <= 50 and mark> 45:
#         print(lesson + " - D grade")
#     elif mark <= 45 and mark > 25:
#         print(lesson + " - E grade")
#     elif mark < 25:
#         print(lesson + " - F grade")
#     else:
#         print("Go to see your teacher")


# 10. Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name

# import random

# list_of_names = []

# user_input = None

# while user_input != "":
#   user_input = input("Enter the name of someone who entered a prize draw: ")
#   list_of_names.append(user_input)

# # print(list_of_names)
# # print(len(list_of_names))
# del(list_of_names[len(list_of_names) - 1])
# # print(list_of_names)
# print("The winner is " + random.choice(list_of_names))



# 11. Create a rock, paper, scissors game which is run against computer. 
#    This is a game where you select either rock/paper/scissors and you compare it to your opponents choice. 
#    Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again.
#       + Expand this so that its best of 3 games

import random

user_wins = 0
computer_wins = 0
options = ["Rock", "Paper", "Scissors"]

while user_wins < 2 and computer_wins < 2:
  user_input = input("Choose from Rock, Paper, or Scissors: ")
  computer_input = random.choice(options)
  print("Computer chose " + computer_input)
  if user_input == "Rock" and computer_input == "Paper":
    print("Computer wins!")
    computer_wins += 1
  elif user_input == "Rock" and computer_input == "Scissors":
    print("User wins!")
    user_wins += 1
  elif user_input == "Paper" and computer_input == "Scissors":
    print("Computer wins!")
    computer_wins += 1
  elif user_input == "Paper" and computer_input == "Rock":
    print("User wins!")
    user_wins += 1
  elif user_input == "Scissors" and computer_input == "Rock":
    print("Computer wins!")
    computer_wins += 1
  elif user_input == "Scissors" and computer_input == "Paper":
    print("User wins!")
    user_wins += 1
  else:
    print("It's a draw! Play again")
  print("User wins: " + str(user_wins))
  print("Computer wins: " + str(computer_wins))
  
    
  