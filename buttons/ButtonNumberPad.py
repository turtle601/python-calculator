from PyQt5.QtWidgets import *

class ButtonNumberPad(QDialog):
    def __init__(self, props):
        super().__init__()

        self.layout = props['layout']
        self.getState = props['getState']
        self.setState = props['setState']
        self.rerender = props['rerender']
        
        self.number_button_dict = {}

    def template(self):
        for number in range(0, 10):
            self.number_button_dict[number] = QPushButton(str(number))

        self.dotBtn = QPushButton('.')
        self.doubleZeroBtn = QPushButton('00')

    def numPadOverZero(self, number, button):
        share, rest = divmod(number - 1, 3)
        self.layout.addWidget(button, share + 3, rest)

    def numPadZero(self, button):
        self.layout.addWidget(button, 6, 1)
    
    def numPadDot(self):
        self.layout.addWidget(self.dotBtn, 6, 2)
    
    def numPadDoubleZero(self):
        self.layout.addWidget(self.doubleZeroBtn, 6, 0)

    def render(self):
        self.template()

        for number, button in self.number_button_dict.items():
            self.numPadOverZero(number, button) if number > 0 else self.numPadZero(button)

        self.numPadDot()
        self.numPadDoubleZero()

        self.setEvent()

    def setEvent(self):
        for number in range(0, 10):
            self.number_button_dict[number].clicked.connect(lambda state, num = number: self.clickNumPad(num))

        self.dotBtn.clicked.connect(lambda: self.clickNumPad('.'))
        self.doubleZeroBtn.clicked.connect(lambda: self.clickNumPad('00'))
    

    def clickNumPad(self, number):
        newData = self.getState() + str(number)

        self.setState(newData)
        self.rerender()