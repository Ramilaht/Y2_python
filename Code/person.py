#Parent class for Student, Athlete, OfficeWorker and SedentaryPerson
class Person:
    def __init__(self, age, weight, height, gender):
        self.age = age
        self.weight = weight
        self.height = height/100
        self.gender = gender

    def calculate_bmr(self, physical_activity_level):
        # Calculate Basal Metabolic Rate (BMR)
        if self.gender == "male":
            bmr = 662 - (9.53 * self.age) + physical_activity_level*((15.91 * self.weight) + (539.6 * self.height))
        elif self.gender == "female":
            bmr = 354 - (6.91 * self.age) + physical_activity_level*((9.36 * self.weight) + (726.6 * self.height))
        return bmr
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_weight(self):
        return self.weight
    
    def get_height(self):
        return self.height
    
    def get_gender(self):
        return self.gender