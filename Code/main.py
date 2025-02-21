from athlete import Athlete
from nutrientgoal import NutrientGoal
from student import Student
from food import FoodItem
from office_worker import OfficeWorker

"""NOTE! This is the main function only for the text-based 
    nutrition tracker! It may not be functional anymore as the underlying 
    functions have been changed later in the development process. For the 
    full functionality, please see the app.py file in the Code folder."""
def main():

    #User will be asked questions and presented with their nutrition goals
    username = input("What is your name? ")
    user_gender = input("What is your passport gender (male/female)? ")
    if user_gender != "male" and user_gender != "female":
        print("Please enter 'male' or 'female'")
    user_age = int(input("How old are you? "))
    user_weight = int(input("How much do you weigh in kilograms? "))
    user_height = int(input("How tall are you in centimeters? "))
    user_archetype = input("Are you a student, an athlete or an office worker? ")
    user_validity = False
    
    food_list = []

    while not user_validity:
        if user_archetype == "student":
            student = Student(user_age, user_weight, user_height, user_gender)
            energy_need = student.calculate_calorie_goals()
            user_validity = True
        elif user_archetype == "athlete":
            athlete = Athlete(user_age, user_weight, user_height, user_gender)
            energy_need = athlete.calculate_nutrient_goals()
            user_validity = True
        elif user_archetype == "office worker":
            office_worker = OfficeWorker(user_age, user_weight, user_height, user_gender)
            energy_need = office_worker.calculate_calorie_goals()
            user_validity = True
        else:
            print("Please enter 'student' or 'athlete'")

    print(f"{username}, you need {energy_need} kcal to maintain your current weight.")
    goals = NutrientGoal(username, energy_need)
    goals.save_goals_to_file("nutrient_goals.txt")

    #Macronutrient and energy goals are presented to the user
    print("Your Macronutrient goals are:")
    print(f"Calories: {energy_need}")
    print(f"Proteins: {goals.get_protein_mass()}")
    print(f"Carbs: {goals.get_carbs_mass()}")
    print(f"Fats: {goals.get_fats_mass()}")

    print("Would you like to log some food items? (y/n)")
    user_log = input()
    if user_log == "y":
        user_log = True
    else:
        user_log = False
    while user_log:
        if user_log:
            food_name = input("What is the name of the food item? ")
            food_calories = int(input("How many calories does it contain? "))
            food_proteins = float(input("How many grams of proteins does it contain? "))
            food_carbs = float(input("How many grams of carbs does it contain? "))
            food_fats = float(input("How many grams of fats does it contain? "))
            food_item = FoodItem(food_name, food_calories, food_proteins, food_carbs, food_fats)
            food_list.append(food_item)
            goals.log_food(food_item)
        print("Would you like to log another food item? (y/n)")
        user_log = input()
        if user_log == "y":
            user_log = True
        else:
            user_log = False


main()