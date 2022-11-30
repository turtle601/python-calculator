from PyQt5.QtWidgets import *

class NumberDisplay(QDialog):
    def __init__(self, props):
        super().__init__()
        
        self.layout = props['layout']
        self.getState = props['getState']
    
    def template(self):
        self.display = QLineEdit('')

    def render(self):
        self.template()
        self.display.setText(str(self.getState('displayNum')))

        self.layout.addWidget(self.display, 0, 4)

       

