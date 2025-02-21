from person import Person
from nutrientgoal import NutrientGoal
class Student(Person):
    def __init__(self, age, weight, height, gender):
        super().__init__(age, weight, height, gender)
    
    def calculate_calorie_goals(self):
        # Calculate nutrient goals specific to students
        if self.gender == "male":
            energy_need = self.calculate_bmr(1.11)
        elif self.gender == "female":
            energy_need = self.calculate_bmr(1.12)
        return energy_need
    