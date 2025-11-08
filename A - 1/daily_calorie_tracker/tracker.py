
# Name: Lucky Pawar
# Date: November 8th, 2025
# Project title: Daily Calorie Tracker (CLI)

import datetime

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

    meal_list.append(mealName)
    calorie_list.append(mealCal)

# Calorie Calculations

totalCal = sum(calorie_list)    # Calculating the total sum of calories
totalItems = len(calorie_list)  # calculating the total number of meals (For Average)

avgCal = totalCal/totalItems # Calculating the average calories

dailyCalLimit = float(input("Enter the daily Calorie limit: ")) # taking the input of daily calorie limit

# Exceed Limit warning system

comparison_message = ""

if avgCal > dailyCalLimit:
    comparison_message = "Warning! \nYour Calorie intake is higher than your dialy Calorie limit."
else:
    comparison_message = "Your Calorie intake is normal. It is less than your daily Calorie limit."
print(comparison_message)

# Printing the table 

print("\n\nMeal Name \t Calorie")
print("--------------------------")
for i in range(mealNum):
    print(f"{meal_list[i]} \t {calorie_list[i]}")
print("---------------------------")
print(f"Total:\t{totalCal}")
print(f"Average:\t{round(avgCal,2)}")

# Bonus task (Saving data in the file)
# Ask user if they want to save the report 
user_wish = input("\nDo you want to Save this report to a file? (Y/N): ").lower().strip()

if user_wish == 'y':
    file_name = 'calorie_log.txt'
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    
    # Removed try-except block for simpler structure
    with open(file_name, 'w') as file:
        
        file.write("="*40 + "\n")
        file.write(f"Session Log - {timestamp}\n")
        file.write("="*40 + "\n\n")
        
        file.write(f"{'Meal Name':<20}{'Calories':>10}\n")
        file.write("-" * 30 + "\n")
        
        for name, calories in zip(meal_list, calorie_list):
            file.write(f"{name:<20}{calories:>10.1f}\n")
            
        file.write("\n" + "-" * 30 + "\n")
        file.write(f"{'Total:':<20}{totalCal:>10.1f}\n")
        file.write(f"{'Average:':<20}{avgCal:>10.2f}\n")
        file.write("\nDaily Calorie Limit: " + str(dailyCalLimit) + "\n")
        file.write("Status: " + comparison_message + "\n")
        file.write("="*40 + "\n")
            
    print(f"🎉 Session log successfully saved to **{file_name}**.")