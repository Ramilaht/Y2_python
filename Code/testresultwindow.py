import unittest
from PyQt6.QtWidgets import QWidget, QApplication
from result_window import ResultWindow
from nutrientmonitor import NutrientMonitor
import sys


class TestResultWindow(unittest.TestCase):

    def setUp(self):
        self.result_window = QApplication(sys.argv)
    def test_init(self):
        self.name = 'Test Name'
        self.goals = [1000, 100, 100, 100]

        result_window = ResultWindow(self.name, self.goals)

        self.assertEqual(result_window.goals, self.goals)
        self.assertEqual(result_window.name, self.name)

    
    def test_nutrient_monitor(self):
        self.name = 'Test Name'
        self.goals = [1000, 100, 100, 100]

        result_window = ResultWindow(self.name, self.goals)
        self.assertIsInstance(result_window.nutrient_monitor, NutrientMonitor)

        self.assertEqual(result_window.nutrient_monitor.Name, self.name)
        self.assertEqual(result_window.nutrient_monitor.calories, self.goals[0])

if __name__ == '__main__':
    unittest.main()
    