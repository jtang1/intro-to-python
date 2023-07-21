# Session 6 Exercises

## Section A
# 1. Create the following dictionary for an apple: Type = "Bramley", Price = 0.39, Colour = "Green".

# apple = {
#   "type": "Bramley",
#   "price": "0.39",
#   "colour": "green"
# }

# 2. Add the best before date to the dictionary - print the dictionary.

# apple["best_before"] = "22nd July 2023"

# print(apple)

# 3. Change the price to 0.41 - print the dictionary.

# apple["price"] = "0.41"

# print(apple)

# 4. Set the apple to be on offer using a Boolean - print the dictionary.

# apple["on_offer"] = True

# print(apple)

# 5. The offer has now expired, remove the key/value from the dictionary - print the dictionary.

# del(apple["on_offer"])

# print(apple)

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask the user to enter a persons name, if they enter a name, ask for the persons age. Store this information in a dictionary inside a list. 
#   Continue to ask for names until no name is given. Then print out all of the names and ages collected.

# names = []
# name = None
# age = None

# while name != "":
#   name = input("Enter a name: ")
  
#   if name != "":
#       age = input("How old are they? ")
#       names.append({
#         "name": name,
#         "age": age
#       })

# print(names)
      

# 2. Create a restaurants menu with 5 items. Store this information in a dictionary inside a list. 
#   Each item in the menu should have the name of the item, the price and if it's vegetarian friendly (make at least one vegetarian friendly dish). 
#   Print out the entire menu. Print out the name of the vegetarian option(s).

# menu = [
#   {"name": "Pasta", "price": "10", "vegetarian": False},
#   {"name": "Pizza", "price": "11", "vegetarian": False},
#   {"name": "Chips", "price": "5", "vegetarian": True},
#   {"name": "Bread", "price": "2", "vegetarian": True},
#   {"name": "Lasagne", "price": "12", "vegetarian": False},
# ]

# # print(menu)

# for item in menu:
#   if item["vegetarian"]:
#     print(item["name"])

# 3. The beetle game is a dice game where depending on what you roll is how much of the beetle you can draw.
#   If you roll a 6, you can draw the body
#   If you roll a 5, you can draw the head
#   If you roll a 4, you can draw the legs (but remember, you cannot draw legs without a body)
#   If you roll a 3, you can draw the antenna (but remember, you cannot draw antenna without a head)
#   If you roll a 2, you can draw the eyes (but remember, you cannot draw eyes without a head)
#   If you roll a 1, you can draw the mouth (but remember, you cannot draw a mouth without a head)
#   You need 6 legs, 2 antenna, 2 eyes, 1 mouth.
#   The player to complete the beetle in the fewest rolls of the dice wins. Create the beetle game.

import random

dice_roll = random.randint(1,6)

beetle = [
  {"body_part": "body", "dice_roll": "6", "number_required": "1", "number_aquired": "0"}
  {"body_part": "head", "dice_roll": "6", "number_required": "1", "number_aquired": "0"}
  {"body_part": "legs", "dice_roll": "6", "number_required": "6", "number_aquired": "0"}
  {"body_part": "antenna", "dice_roll": "6", "number_required": "2", "number_aquired": "0"}
  {"body_part": "eyes", "dice_roll": "6", "number_required": "2", "number_aquired": "0"}
  {"body_part": "mouth", "dice_roll": "6", "number_required": "1", "number_aquired": "0"}
]


print(dice_roll)