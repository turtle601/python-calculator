import sys
from PyQt5.QtWidgets import *

from components.NumberDisplay import NumberDisplay
from buttons.ButtonOperator import ButtonOperator
from buttons.ButtonNumberPad import ButtonNumberPad
from buttons.ButtonCommand import ButtonCommand
 

class Main(QDialog):
    def __init__(self):
        super().__init__()

        self.state = { "displayNum" : "", "operation": [] }
        
        self.layout = QGridLayout()    
        
        self.init_ui()

    def init_ui(self):
        self.display = NumberDisplay({
            'layout': self.layout,
            'getState': self.getState,
        })

        self.numberPad = ButtonNumberPad({ 
            'layout': self.layout,
            'clickNumPad': self.clickNumPad
        })   

        self.operator = ButtonOperator({ 'layout': self.layout })   
        self.command = ButtonCommand({ 'layout': self.layout })   

        self.mounted([
           self.display, 
           self.numberPad, 
           self.operator, 
           self.command
        ])

        self.setLayout(self.layout)
        self.show()

    def mounted(self, componentInstanceArr): 
        for instance in componentInstanceArr:
            instance.render()
    
    def getState(self, stateKey):
        return self.state.get(stateKey); 

    def setState(self, newData, stateKey):
        self.state[stateKey] = newData
    
    def rerender(self):
        self.display.render()

    def clickNumPad(self, number): 
        newData = self.getState('displayNum') + str(number)

        self.setState(newData, 'displayNum')
        self.rerender()
    
    def clickBackSpace(self):
        newData = self.getState('displayNum')[:-1]
        
        self.setState(newData, 'displayNum')
        self.rerender()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())