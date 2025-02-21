
class FoodItem:
    def __init__(self, name, proteins, carbs, fats):
        self.name = name
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats
        
    
    def get_energy(self):
        return self.proteins * 4 + self.carbs * 4 + self.fats * 9
    
    def get_name(self):
        return self.name
    
    def get_proteins(self):
        return self.proteins
    
    def get_carbs(self):
        return self.carbs
    
    def get_fats(self):
        return self.fats
    
