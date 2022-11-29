from PyQt5.QtWidgets import *

class ButtonCommand(QDialog):
    def __init__(self, props):
        super().__init__()

        self.layout = props['layout']
        self.command = ['%', 'CE', 'C', '1/x', 'x²', '√']

    def render(self):
        for index, command in enumerate(self.command):
            share, rest = divmod(index, 3)
            self.layout.addWidget(QPushButton(command), share, rest)