from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox, QInputDialog
from nutrientgoal import NutrientGoal
from PyQt6.QtWidgets import QWidget
import sys
from result_window import ResultWindow
from student import Student
from athlete import Athlete
from office_worker import OfficeWorker
from sedentary_person import SedentaryPerson

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.result_window = None

    def initUI(self):
        self.setWindowTitle('Nutrition Tracker')
        
        layout = QVBoxLayout()
        
        #Creating the labels
        self.name_label = QLabel("What is your name?", self)
        self.name_input = QLineEdit(self)

        self.gender_label = QLabel("What is your gender? (male/female)", self)
        self.gender_input = QComboBox(self)
        self.gender_input.addItem("male")
        self.gender_input.addItem("female")

        self.age_label = QLabel("How old are you?", self)
        self.age_input = QLineEdit(self)

        self.weight_label = QLabel("How much do you weigh in kilograms?", self)
        self.weight_input = QLineEdit(self)

        self.height_label = QLabel("How tall are you in centimeters?", self)
        self.height_input = QLineEdit(self)

        self.archetype_label = QLabel("What type of person are you?", self)
        self.archetype_input = QComboBox(self)
        self.archetype_input.addItem("Student")
        self.archetype_input.addItem("Athlete")
        self.archetype_input.addItem("Office worker")
        self.archetype_input.addItem("Sedentary person")

        #Creating the buttons
        self.load_goals_button = QPushButton("Load Goals from file", self)
        self.load_goals_button.clicked.connect(self.on_load_goals_clicked)
        
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.on_submit_clicked) # Connect the button to the on_submit_clicked function (submit)

    

        # Add widgets to layout
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.gender_label)
        layout.addWidget(self.gender_input)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        layout.addWidget(self.archetype_label)
        layout.addWidget(self.archetype_input)
        layout.addWidget(self.submit_button)

        layout.addWidget(self.load_goals_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        #Set title
        self.setWindowTitle('Nutrient calculator')
        self.show()

    def on_submit_clicked(self):
        name = self.name_input.text()
        gender = self.gender_input.currentText()
        archetype = self.archetype_input.currentText()


        #validate inputs   
        try:
            age = int(self.age_input.text())
            weight = int(self.weight_input.text())
            height = int(self.height_input.text())

            if age < 0 or weight < 0 or height < 0:
                raise ValueError("Age, weight and height must be positive numbers")
        except ValueError:
            QMessageBox.critical(self,"Input Error","Please enter valid age, weight and height")
            return

        if archetype == "Sedentary person":
            user = SedentaryPerson(age, weight, height, gender)
            user_type = "Sedentary"

        elif archetype == "Student":
            user = Student(age, weight, height, gender)
            user_type = "Student"

        elif archetype == "Athlete":
            user = Athlete(age, weight, height, gender)
            user_type = "Athlete"


        elif archetype == "Office worker":
            user = OfficeWorker(age, weight, height, gender)
            user_type = "Office worker"

        else:
            QMessageBox.critical(self,"Input Error","Please enter valid archetype")
            return
        
        calories = user.calculate_calorie_goals()

        #Obtain nutrient goals for the user
        nutrient_goal = NutrientGoal(name, calories)
        calories = nutrient_goal.get_calories()
        proteins = nutrient_goal.get_protein_mass()
        carbs = nutrient_goal.get_carbs_mass()
        fats = nutrient_goal.get_fats_mass()
        
        goals = [calories, proteins, carbs, fats]
        consumed = [0, 0, 0, 0]

        #Open result window
        #Close existing result window if it exists
        if self.result_window is not None:
            self.result_window.close()
        
        self.result_window = ResultWindow(name, goals, consumed)
        self.result_window.show()

    def on_load_goals_clicked(self):

        username, ok = QInputDialog.getText(self, 'Enter Username', 'Username:')
        if not ok or not username:
            return

        file_path, ok = QInputDialog.getText(self, 'Load Goals from File', 'Enter file path:')
        if not ok or not file_path:
            return
        
        print(f"Loading goals from file: {file_path}")
        
        #Load goals from file
        file_read = NutrientGoal(username, 0)
        try:
            nutrients = file_read.load_goals_from_file(file_path)
            consumed_nutrients = file_read.load_consumed_from_file(file_path)
            
            calories = nutrients[0]
            proteins = nutrients[1]
            carbs = nutrients[2]
            fats = nutrients[3]

            consumed_calories = consumed_nutrients[0]
            consumed_proteins = consumed_nutrients[1]
            consumed_carbs = consumed_nutrients[2]
            consumed_fats = consumed_nutrients[3]

            goals = [calories, proteins, carbs, fats]   
            consumed = [consumed_calories, consumed_proteins, consumed_carbs, consumed_fats]


            #Create a ResultWindow
            if self.result_window is not None:
                self.result_window.close()
            self.result_window = ResultWindow(username, consumed, goals)
            self.result_window.show()

        except ValueError as e:
            QMessageBox.warning(self, 'Invalid data in file', str(e))
        except IOError as e:
            QMessageBox.warning(self, 'Error', str(e))
        
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())