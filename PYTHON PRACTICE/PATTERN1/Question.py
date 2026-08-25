# Question 1 — Fitness Activities
# Problem Description
# A fitness application stores information about different fitness activities. Each activity contains its name, category, duration, and calories burned.
# The program should allow the user to add activity details and then retrieve activities based on their category and minimum duration.
# 1. Add Activity Details
# Function Name: add_data
# Parameters:
# name
# category
# duration
# calories

# The function should:
# Create a tuple containing the activity name, category, duration, and calories.
# Add the tuple to the list of activities.
# Return the updated list.
# For example:
# Input:
# Name = Running
# Category = Cardio
# Duration = 30
# Calories = 300
# Stored tuple:
# ("Running", "Cardio", 30, 300)

# 2. Get Activity Details
# Function Name: get_data
# Parameters:
# category
# min_duration

# The function should:
# Find all activities belonging to the given category.
# Category comparison should be case-insensitive.
# Find only activities whose duration is greater than or equal to the given minimum duration.
# Store all matching activities in a separate result list.
# Return the result list.
# If no activity matches the given conditions, return an empty list.

list = []
def add_data(name,category,duration,calories):
    tup = (name, category, duration, calories)
    list.append(tup)
    return list

def get_data(category,minimum_duration):
    result = []
    for tup in list:
        if category.lower() == tup[1].lower() and tup[2] >= minimum_duration:
            result.append(tup)
    return result
    
def main():
    n = int(input("Enter number of activities: "))

    for i in range(n):
        name = input("Enter activity name: ")
        category = input("Enter category: ")
        duration = int(input("Enter duration: "))
        calories = int(input("Enter calories burned: "))

        add_data(name, category, duration, calories)

    print("Activities:")

    category = input("Enter category: ")
    min_duration = int(input("Enter minimum duration: "))

    result = get_data(category, min_duration)

    for activity in result:
        print(activity)


if __name__ == "__main__":
    main()