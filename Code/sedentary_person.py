from person import Person

class SedentaryPerson(Person):
    def __init__(self, age, weight, height, gender):
        super().__init__(age, weight, height, gender)

    def calculate_calorie_goals(self):
        if self.gender == "male":
            energy_need = self.calculate_bmr(1)
        elif self.gender == "female":
            energy_need = self.calculate_bmr(1)
        return energy_need