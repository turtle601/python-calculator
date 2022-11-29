from PyQt5.QtWidgets import *

class ButtonOperator(QDialog):
    def __init__(self, props):
        super().__init__()

        self.layout = props['layout']
        self.operators = ['BackSpace', '/', '*', '-', '+', '=']

    def render(self):
        for index, operator in enumerate(self.operators):
            self.layout.addWidget(QPushButton(operator), index, 4)
            
        

        

       

