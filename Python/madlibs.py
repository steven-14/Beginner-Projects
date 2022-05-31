# This is my beginner project,  code along with Kylie Ying.
# youtube video: 12 Beginner Python Projects - Coding Course - FreeCodeCamp.org
# To run this, save it to desktop and navigate there using the command line interpreter.
# It's practice for string concatenation (aka how to put strings together).
# suppose we want to create a string that says "subscribe to ______"
# using a variable for the string: youtuber = "" # some string variable
# 3 ways to print that
# print("subscribe to" + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

# Assign adj as an input variable. Then assign madlib variable = an f string.

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous_person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time \
because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)

# kylie ying's madlibs are here: C:\Users\toshiba\Desktop\A Projects\kylie ying's madlibs code for beginner my beginner madlibs project\beginner-projects-master
