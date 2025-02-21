

class NutrientGoal:
    def __init__(self, Name, calories):
        self.Name = Name
        self.calories = calories
        self.proteins_e = self.calories * 0.3
        self.carbs_e = self.calories * 0.45
        self.fats_e = self.calories * 0.25

        self.proteins_m = self.proteins_e/4
        self.carbs_m = self.carbs_e/4
        self.fats_m = self.fats_e/9

    def get_name(self):
        return self.Name
    def get_calories(self):
        return self.calories
    def get_protein_energy(self):
        return self.proteins_e
    def get_carbs_energy(self):
        return self.carbs_e 
    
    def get_fats_energy(self):
        return self.fats_e
    def get_protein_mass(self):
        return self.proteins_m 
    
    def get_carbs_mass(self):
        return self.carbs_m 
    def get_fats_mass(self):
        return self.fats_m
    
    def load_from_file(self, file_path):
        goals =self.load_goals_from_file(file_path)
        consumed = self.load_consumed_from_file(file_path)

        return [goals, consumed]

    def load_goals_from_file(self, file_path):
        # Load the nutrient goals from a text file
        try:
            with open(file_path, 'r') as file:
                stream = file.readlines()

            if len(stream) != 5:
                raise ValueError(f"Invalid data in file: {file_path}")
            
            try:
                #Reads first member of the tuple
                self.goal_calories = float(stream[1].split(": ")[1].split("/")[0])
                self.proteins_m = float(stream[2].split(": ")[1].split("/")[0])
                self.carbs_m = float(stream[3].split(": ")[1].split("/")[0])
                self.fats_m = float(stream[4].split(": ")[1].split("/")[0])
                if self.goal_calories < 0 or self.proteins_m < 0 or self.carbs_m < 0 or self.fats_m < 0:
                    raise ValueError(f"Invalid data in file: {file_path}")

                return [self.goal_calories, self.proteins_m, self.carbs_m, self.fats_m]
            except ValueError:
                raise ValueError(f"Invalid data in file: {file_path}")
            


        except IOError:
            raise IOError(f"File not found: {file_path}")
        
        finally:
            file.close()
    
    def load_consumed_from_file(self, file_path):
        try: 
            with open(file_path, 'r') as file:
                stream = file.readlines()
            
            if len(stream) != 5:
                raise ValueError(f"Invalid data in file: {file_path}")
            try:
                #Reads second member of the tuple
                self.consumed_calories = float(stream[1].split(": ")[1].split("/")[1])
                self.consumed_proteins = float(stream[2].split(": ")[1].split("/")[1].rstrip(' grams\n'))
                self.consumed_carbs = float(stream[3].split(": ")[1].split("/")[1].rstrip(' grams\n'))
                self.consumed_fats = float(stream[4].split(": ")[1].split("/")[1].rstrip(' grams\n'))

                if self.consumed_calories < 0 or self.consumed_proteins < 0 or self.consumed_carbs < 0 or self.consumed_fats < 0:
                    raise ValueError(f"Invalid data in file: {file_path}")

                return [self.consumed_calories, self.consumed_proteins, self.consumed_carbs, self.consumed_fats]
            except ValueError:
                raise ValueError(f"Invalid data in file: {file_path}")
            
        except IOError:
            raise IOError(f"File not found: {file_path}")
        
        finally:
            file.close()

