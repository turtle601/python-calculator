from PyQt5.QtWidgets import *

class ButtonOperator(QDialog):
    def __init__(self, props):
        super().__init__()

        self.layout = props['layout']
        self.clickOperator = props['clickOperator']
        
        self.operators = ['BackSpace', '/', '*', '-', '+', '=']
        self.operator_dict= {}

    def template(self):
        for operator in self.operators:
            self.operator_dict[operator] = QPushButton(operator)

    def render(self):
        self.template()

        for index, operator in enumerate(self.operators):
            self.layout.addWidget(self.operator_dict[operator], index + 1, 4)

        self.setEvent()
            
    def setEvent(self):
        for operator in self.operators:
            self.operator_dict[operator].clicked.connect(lambda state, op = operator: self.clickOperator(op))

        

       

