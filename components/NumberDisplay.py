from PyQt5.QtWidgets import *

class NumberDisplay(QDialog):
    def __init__(self, props):
        super().__init__()
        
        self.layout = props['layout']
        self.getState = props['getState']

    def render(self):
        self.layout.addWidget(QLabel(self.getState('displayNum')), 0, 4)

       

