import sys
import unittest
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QMessageBox
from mainwindow import MainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtTest import QTest

app = QApplication(sys.argv)

class TestMainWindow(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.form = MainWindow()

    def tearDown(self):
        self.form.close()

    def test_name_label(self):
        labels = self.form.findChildren(QLabel)
        for lbl in labels:
            if lbl.text() == 'What is your name?':
                label = lbl
                break
            else:
                label = None
        self.assertIsNotNone(label, "Label not found.")
        self.assertEqual(label.text(), 'What is your name?')
    
    def test_gender_label(self):
        labels = self.form.findChildren(QLabel)
        for lbl in labels:
            if lbl.text() == 'What is your gender? (male/female)':
                label = lbl
                break
            else:
                label = None
        self.assertEqual(label.text(), 'What is your gender? (male/female)')
    
    def test_button_event(self):
        self.form.name_input.setText("Test username")
        self.form.age_input.setText("22")
        self.form.weight_input.setText("81")
        self.form.height_input.setText("180")
        self.form.gender_input.setCurrentText("male")
        self.form.archetype_input.setCurrentText("Student")

        #Simulate button clicking event
        QTest.mouseClick(self.form.submit_button, Qt.MouseButton.LeftButton)

        #Assert validity of user input
        self.assertIsNotNone(self.form.result_window)
    
    def test_false_age_input(self):
        self.form.age_input.setText("-10")
        self.form.weight_input.setText("A")
        self.form.height_input.setText("-180")

        self.form.on_submit_clicked()

        widget = QApplication.activeModalWidget()
        self.assertIsInstance(widget, QMessageBox)

        if widget:
            self.assertEqual(widget.windowTitle(), "Error")
            self.assertEqual(widget.text(), "Please enter a valid age, weight and height.")

            widget.accept()

if __name__ == '__main__':
    unittest.main()