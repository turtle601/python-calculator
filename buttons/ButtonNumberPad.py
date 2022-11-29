from PyQt5.QtWidgets import *

class ButtonNumberPad(QDialog):
    def __init__(self, props):
        super().__init__()

        self.layout = props['layout']
        self.number_button_dict = {}

    def template(self):
        for number in range(0, 10):
            self.number_button_dict[number] = QPushButton(str(number))

    def numPadOverZero(self, number, button):
        share, rest = divmod(number - 1, 3)
        self.layout.addWidget(button, share, rest)

    def numPadZero(self, button):
        self.layout.addWidget(button, 3, 1)
    
    def numPadDot(self):
        self.layout.addWidget(QPushButton('.'), 3, 2)
    
    def numPadDoubleZero(self):
        self.layout.addWidget(QPushButton('00'), 3, 0)

    def render(self):
        self.template()

        for number, button in self.number_button_dict.items():
            self.numPadOverZero(number, button) if number > 0 else self.numPadZero(button)

        self.numPadDot()
        self.numPadDoubleZero()