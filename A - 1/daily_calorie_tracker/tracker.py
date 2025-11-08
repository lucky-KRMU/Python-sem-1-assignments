
# Name: Lucky Pawar
# Date: November 8th, 2025
# Project title: Daily Calorie Tracker (CLI)

# Creating a welcome string
welcome_str = ''' 
#===============================#
#             WELCOME           #
#-------------------------------#
#*******************************#
#   Daily Calorie Tracker(CLI)  #
#*******************************#

> Why use this tool?  :- )
=> This is the tool that can be 
used to calculate and keep a track
of your daily calorie intake.

**********************************
#================================#
# Thanks for using our tool! :-D #
#================================#
'''

print(welcome_str)  # printing the welcome string

# Input and Data Collection

# Defining the required list
meal_list = [] # defining the meal list
calorie_list = [] # defining the calorie list

#Taking the inputs

mealNum = int(input("Enter the number of Meals you want to enter: ")) # taking input of the total number of meals

# Using for loop as the number of iterations is predefined.
for i in range(mealNum):
    mealName = input("Enter the Meal: ") # Taking the input of the name
    mealCal = float(input("Enter the Calorie of the Meal: ")) # Taking the input of the calorie of that meal


