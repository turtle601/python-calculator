from PyQt5.QtWidgets import *

class ButtonInput(QDialog):
    def __init__(self, props):
        super().__init__()
        
        self.getState = props['getState']
        self.setState = props['setState']

    def render(self):
        layout = QGridLayout()
        layout.addWidget(QLineEdit(self.getState()), 0, 1)

        return layout

       

