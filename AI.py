# Name: AI.py 
# Language(s): Python (100%)
# Lines: 86
# Words: 340
# Characters: 2,524
# Variables/Categories: 5 

# SUMMARY (FORM & PROFILE): Basically a form that uses the inputs/responses/answers as a variable input and prints them in a single profile, you can change the form if you want. #
# SUMMARY (CREATING & LOADING SIMULATION): The creating and loading simulations are, well, simulations, and can be removed or changed, just like the form. #

import time
import sys

# Type your name (real or user, although I recommend only your username) here, this will be used later as a variable input #
print(" ")
print("AI: Hello there. I'm AI. What's your name?")
name = input("You: ")
print(" ")

# Type your home country/country you live in here, this will be used later as a variable input #
print("AI: Okay then... what country are you from?")
country = input("You: ")
print(" ")

# Type your birth year here, this will be used later as a variable input #
print("AI: In what year were you born?")
birthyear = input("You: ")
print(" ")

# Type favorite food(s) here, this will be used later as a variable input #
print("AI: I'm hungry. What's (What are) your favorite food(s)?")
food = input("You: ")
print(" ")

# Type your hobby(s) here, this will be used later as a variable input #
print("AI: And finally... what is/are your hobby(s)?")
hobby = input("You: ")
print(" ")

# Simulates creating your profile, you can remove/change this code if you want, only a simulation #
print("Wait for your profile to be done...")
print(" ")
time.sleep(2)
print(".")
time.sleep(0)
print("..")
time.sleep(1)
print("...")
time.sleep(2)
print("....")
time.sleep(3)
print(".....")
time.sleep(4)

print(" ")
print("AI: Your profile is done! Loading your profile...")
print(" ")

# Simulates loading your profile, again, this is a simulation, you can delete/change this if you want #
time.sleep(1)
print("Loading results...")
time.sleep(3)
print("Loading: var 'name'")
print("Loading: var 'country'")
print("Loading: var 'birthyear'")
time.sleep(1)
print("Loading: var 'food'")
time.sleep(1)
print("Loading: var 'hobby'")
time.sleep(2)
print("Localizing results...")
time.sleep(2)
print(" ")
print("Done!")
time.sleep(1)

# Your profile #
# This compiles the inputs/answers/responses you wrote into a single profile by using the variable inputs of your responses and printing them #
print(" ")
print("// YOUR PROFILE //")
print(" ")
print("Name: {}" .format(name))
print("Country: {}" .format(country))
print("Birthyear: {}" .format(birthyear))
print("Favorite Food: {}" .format(food))
print("Hobby: {}" .format(hobby))