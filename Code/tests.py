import unittest
from nutrientgoal import NutrientGoal
from result_window import ResultWindow
from mainwindow import MainWindow
from student import Student
from athlete import Athlete
from office_worker import OfficeWorker
from sedentary_person import SedentaryPerson
from nutrientmonitor import NutrientMonitor
from food import FoodItem

class Tests(unittest.TestCase):
    def test_proteins_energy(self):
        goal = NutrientGoal("Test Goal", 2000)
        self.assertEqual(goal.get_protein_energy(), 600)
    
    def test_carbs_energy(self):
        goal = NutrientGoal("Test Goal", 2000)
        self.assertEqual(goal.get_carbs_energy(), 900)
    
    def test_fats_energy(self):
        goal = NutrientGoal("Test Goal", 2000)
        self.assertEqual(goal.get_fats_energy(), 500)

    def test_proteins_mass(self):
        goal = NutrientGoal("Test Goal", 2000)
        self.assertEqual(goal.get_protein_mass(), 150)
    
    def test_carbs_mass(self):
        goal = NutrientGoal("Test Goal", 2000)
        self.assertEqual(goal.get_carbs_mass(), 225)
    
    def test_fats_mass(self):
        goal = NutrientGoal("Test Goal", 2000)
        self.assertEqual(goal.get_fats_mass(), 55.555555555555555555)

    def test_log_food(self):
        monitor = NutrientMonitor("Test", 2000)
        food = FoodItem("Test", 10, 20, 5)

        monitor.log_food(food)

        self.assertEqual(monitor.get_consumed_nutrients(), (165, 10, 20, 5))

if __name__ == '__main__':
    unittest.main()



        