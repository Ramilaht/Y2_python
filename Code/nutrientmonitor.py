from food import FoodItem
from nutrientgoal import NutrientGoal
class NutrientMonitor(NutrientGoal):
    def __init__(self, name, calories, consumed):
        super().__init__(name, calories)
        self.consumed_calories = consumed[0]
        self.consumed_proteins = consumed[1]
        self.consumed_carbs = consumed[2]
        self.consumed_fats = consumed[3]
        self.food_list = []

    """Function to log food items towards user goals"""
    def log_food(self, food_item: FoodItem):
        self.consumed_calories += food_item.get_energy()
        self.consumed_proteins += food_item.get_proteins()
        self.consumed_carbs += food_item.get_carbs()
        self.consumed_fats += food_item.get_fats()

        self.food_list.append(food_item)

    def get_consumed_nutrients(self):
        return (self.consumed_calories, self.consumed_proteins, self.consumed_carbs, self.consumed_fats)


    def get_eaten_foods(self):
        formatted_food_list = ["Eaten Foods:"]
        #Store food items in a list
        for food in self.food_list:
            formatted_food_list.append(f"{food.get_name()}, E: {food.get_energy()} kcal, P: {food.get_proteins()} g, C: {food.get_carbs()} g, F: {food.get_fats()} g")
        return formatted_food_list
    
    def calculate_remaining_nutrients(self):
        remaining_calories = self.nutrient_goal.calories - self.consumed_calories
        remaining_proteins = self.nutrient_goal.proteins - self.consumed_proteins
        remaining_carbs = self.nutrient_goal.carbs - self.consumed_carbs
        remaining_fats = self.nutrient_goal.fats - self.consumed_fats
        return (remaining_calories, remaining_proteins, remaining_carbs, remaining_fats)
    
    def save_goals_to_file(self, file_path, name):
        # Save the nutrient goals to a text file
        nutrient_list = self.get_consumed_nutrients()
        c_calories = nutrient_list[0]
        c_proteins = nutrient_list[1]
        c_carbs = nutrient_list[2]
        c_fats = nutrient_list[3]

        try:
            with open(file_path, 'w') as file:
                file.write("Nutrient Goals:\n")
                file.write(f"Calories: {c_calories:.1f}/{self.calories:.1f}\n")
                file.write(f"Protein: {c_proteins:.1f}/{self.proteins_m:.1f} grams\n")
                file.write(f"Carbs: {c_carbs:.1f}/{self.carbs_m:.1f} grams\n")
                file.write(f"Fats: {c_fats:.1f}/{self.fats_m:.1f} grams\n")
        except IOError:
            pass
