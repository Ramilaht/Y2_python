from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsTextItem, QInputDialog, QHBoxLayout, QFileDialog, QMessageBox
from PyQt6.QtCore import QRectF
from PyQt6.QtGui import QColor, QBrush
from nutrientmonitor import NutrientMonitor
from food import FoodItem

class ResultWindow(QWidget):
    def __init__(self, name, goals, consumed):
        super().__init__()
        self.name = name
        self.goals = goals
        self.consumed = consumed
        self.nutrient_monitor = NutrientMonitor(self.name, self.goals[0], consumed)
        self.initUI(goals)
        
    
    def initUI(self, goals: list):
        self.setWindowTitle(f'Hi {self.name}! Here are your Nutrition Goals')
        self.resize(1000, 750)
        layout = QVBoxLayout()
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.balance_text = QTextEdit()
        self.balance_text.setReadOnly(True)
        self.food_list_area = QTextEdit()
        self.food_list_area.setReadOnly(True)

        self.update_goals_display()

        #Create a text layout
        text_layout = QHBoxLayout()
        text_layout.addWidget(self.result_text)
        text_layout.addWidget(self.balance_text)
        text_layout.addWidget(self.food_list_area)

        layout.addLayout(text_layout)
        
        #Create a Graphics layout
        graphics_layout = QHBoxLayout()

        #Create a Graphicsscene and GraphicsView
        self.scene = QGraphicsScene()
        self.scene2 = QGraphicsScene()
        view = QGraphicsView(self.scene)
        view2 = QGraphicsView(self.scene2)
        graphics_layout.addWidget(view)
        graphics_layout.addWidget(view2)
        
        layout.addLayout(graphics_layout)

        #Add ellipse and make portions of ellipse visible to user. The portions are the goals.
        #Ellipse sections will be the balanced macronutrients that the user needs to meet their goals
        ellipse_dim = QRectF(0, 0, 300, 300)
        


        total_goals = goals[1] + goals[2] + goals[3]
        start_angle = 0

        section_angles = {'Proteins': 360*goals[1]/total_goals, 'Carbs': 360*goals[2]/total_goals, 'Fats': 360*goals[3]/total_goals}

        colours = {'Proteins': QColor(255, 0, 0), 'Carbs': QColor(0, 0, 255), 'Fats': QColor(255, 255, 0)}
        named_colours = {'Proteins': 'Red', 'Carbs': 'Blue', 'Fats': 'Yellow'}

        #Draw ellipse according to parameters
        for goal, section_angle in section_angles.items():
            ellipse = QGraphicsEllipseItem(ellipse_dim)
            ellipse.setStartAngle(int(start_angle*16))

            ellipse.setSpanAngle(int(section_angle)*16)

            ellipse.setBrush(QBrush(colours[goal]))
            self.scene.addItem(ellipse)

            #Add text to ellipse
            text_item = QGraphicsTextItem(f"{goal}: {named_colours[goal]}")
            text_item.setPos(ellipse_dim.x() + ellipse_dim.width() + 10, ellipse_dim.y() + start_angle/360*ellipse_dim.height())
            self.scene.addItem(text_item)
            start_angle += section_angle
        #Adding a title to the ellipse
        text = QGraphicsTextItem("Goal Macronutrients visualised")
        text.setPos(ellipse_dim.x() + ellipse_dim.width()/2 - text.boundingRect().width()/2, ellipse_dim.y() - text.boundingRect().height())
        self.scene.addItem(text)
        
        #Creating a layout for buttons
        self.button_layout = QHBoxLayout()
        self.log_food_button = QPushButton("Log Food", self)
        self.log_food_button.clicked.connect(self.log_food_clicked)
        self.export_goals_button = QPushButton("Export Goals", self)
        self.export_goals_button.clicked.connect(self.export_goals_clicked)
        
        self.button_layout.addWidget(self.log_food_button)
        self.button_layout.addWidget(self.export_goals_button)
        layout.addLayout(self.button_layout)


        #Add a placeholder for monitoring ellipse
        self.consumed_ellipse = None
        if self.consumed[1] + self.consumed[2] + self.consumed[3] != 0:
            self.draw_consumed_nutrients_ellipse()

        self.update_food_list_display()
        self.setLayout(layout)
        self.show()

    def update_goals_display(self):
        consumed = self.nutrient_monitor.get_consumed_nutrients()
        self.result_text.setText(f"""
            Current intake:
            Calories: {consumed[0]} kcal / {int(self.goals[0])} kcal
            Protein: {consumed[1]} g / {int(self.goals[1])} g
            Carbs: {consumed[2]} g / {int(self.goals[2])} g
            Fats: {consumed[3]} g / {int(self.goals[3])} g
        """)
        total = int(consumed[1] + consumed[2] + consumed[3])
        if total != 0:
            self.balance_text.setText(f"""
                Your consumed macronutrient percentages are:
                Protein: {int(consumed[1]/total*100)}%
                Carbs: {int(consumed[2]/total*100)}%
                Fats: {int(consumed[3]/total*100)}%
            """)
        else:
            self.balance_text.setText("No data yet, input something!")
    
    def update_food_list_display(self):
        #Get list of eaten foods and display it
        food_items = self.nutrient_monitor.get_eaten_foods()
        self.food_list_area.setText("\n".join(food_items))

    def draw_consumed_nutrients_ellipse(self):
        #Remove the previous ellipse if it exists
        if self.consumed_ellipse:
            self.scene.removeItem(self.consumed_ellipse)

        self.consumed_ellipse_dim = QRectF(0, 0, 300, 300)
        consumed_proteins = self.nutrient_monitor.get_consumed_nutrients()[1]
        consumed_carbs = self.nutrient_monitor.get_consumed_nutrients()[2]
        consumed_fats = self.nutrient_monitor.get_consumed_nutrients()[3]
        consumed_total = consumed_proteins + consumed_carbs + consumed_fats

        #Draw new ellipse according to parameters
        if consumed_total > 0:
            consumed_section_angles = {'Proteins': 360*consumed_proteins/consumed_total, 'Carbs': 360*consumed_carbs/consumed_total, 'Fats': 360*consumed_fats/consumed_total}


            colours = {'Proteins': QColor(255, 0, 0), 'Carbs': QColor(0, 0, 255), 'Fats': QColor(255, 255, 0)}
            start_angle = 0
            for nutrient, section_angle in consumed_section_angles.items():
                self.consumed_ellipse = QGraphicsEllipseItem(self.consumed_ellipse_dim)
                self.consumed_ellipse.setStartAngle(int(start_angle*16))

                self.consumed_ellipse.setSpanAngle(int(section_angle)*16)
                
                self.consumed_ellipse.setBrush(QBrush(colours[nutrient]))
                self.scene2.addItem(self.consumed_ellipse)
                start_angle += section_angle
        text = QGraphicsTextItem("Consumed Macronutrients visualised")
        text.setPos(self.consumed_ellipse_dim.x() + self.consumed_ellipse_dim.width()/2 - text.boundingRect().width()/2, self.consumed_ellipse_dim.y() - text.boundingRect().height())
        self.scene2.addItem(text)
    
    def log_food_clicked(self):
        food_item_name = QInputDialog.getText(self, "Food Item", "Enter the meal's name:")[0]
        food_item_proteins = QInputDialog.getInt(self, "Food Item", "Enter the meal's protein in grams:")[0]
        food_item_carbs = QInputDialog.getInt(self, "Food Item", "Enter the meal's carbs in grams:")[0]
        food_item_fats = QInputDialog.getInt(self, "Food Item", "Enter the meal's fats in grams:")[0]

        if food_item_proteins < 0 or food_item_carbs < 0 or food_item_fats < 0:
            QMessageBox.warning(self, "Error", "Invalid input. Please enter positive values.")
            return

        #Utilise the functions above to update the display, this function works as a master function of sorts
        food_item = FoodItem(food_item_name, food_item_proteins, food_item_carbs, food_item_fats)
        self.nutrient_monitor.log_food(food_item)
        self.draw_consumed_nutrients_ellipse()
        self.update_goals_display()
        self.update_food_list_display()

    def export_goals_clicked(self):
        # This will prompt the user to choose where to save the file
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Goals", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            self.nutrient_monitor.save_goals_to_file(file_path, self.name)
        else:
            # Handle the situation where the user cancels the save operation
            pass




