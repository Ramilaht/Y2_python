#Archetype class along with Student, SedentaryPerson and OfficeWorker classes
from person import Person
class Athlete(Person):
    def __init__(self, age, weight, height, gender):
        super().__init__(age, weight, height, gender)
    def calculate_calorie_goals(self):
        if self.gender == "male":
            energy_need = self.calculate_bmr(1.48)
        elif self.gender == "female":
            energy_need = self.calculate_bmr(1.45)
        return energy_need