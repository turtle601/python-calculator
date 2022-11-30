from PyQt5.QtWidgets import *

class ButtonCommand(QDialog):
    def __init__(self, props):
        super().__init__()

        self.layout = props['layout']
        self.clickOneOperator = props['clickOneOperator']

        self.commands = ['%', 'CE', 'C', '1/x', 'x²', '√']
        self.command_dict = {}
    
    def template(self):
        for command in self.commands:
            self.command_dict[command] = QPushButton(command)

    def render(self):
        self.template()

        for index, command in enumerate(self.commands):
            share, rest = divmod(index, 3)
            self.layout.addWidget(self.command_dict[command], share + 1, rest)
        
        self.setEvent()
    
    def setEvent(self):
        for command in self.commands:
            self.command_dict[command].clicked.connect(lambda state, comm = command: self.clickOneOperator(comm))