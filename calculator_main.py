import sys
from PyQt5.QtWidgets import *

from components.NumberDisplay import NumberDisplay
from components.buttons.ButtonOperator import ButtonOperator
from components.buttons.ButtonNumberPad import ButtonNumberPad
from components.buttons.ButtonCommand import ButtonCommand

from utils.fourArithmetic import plus, minus, multiply, divide, getRest
 

class Main(QDialog):
    def __init__(self):
        super().__init__()

        self.state = { "displayNum" : "", "operation": [], "operator": "" }
        
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

        self.operator = ButtonOperator({ 
            'layout': self.layout,
            'clickTwoOperator': self.clickTwoOperator 
        })
           
        self.command = ButtonCommand({ 
            'layout': self.layout,
            'clickOneOperator': self.clickOneOperator 
        })   

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

    def setState(self, stateKey, newData):
        self.state[stateKey] = newData
    
    def rerender(self):
        self.display.render()

    def clickNumPad(self, number): 
        newData = str(self.getState('displayNum')) + str(number)

        self.setState('displayNum', newData)
        self.rerender()
    
    def clickBackSpace(self):
        newData = str(self.getState('displayNum'))[:-1]

        self.setState('displayNum', newData)
        self.rerender()

    def clickEqual(self):
        operation = self.getState('operation')[:]
        inputNum = self.getState('displayNum')

        if (inputNum != ""): operation.append(float(inputNum))

        if len(operation) == 1:             
            self.setState('operation', operation)
            self.setState('displayNum', "")
            
        if len(operation) == 2:
            old_operator = self.getState('operator')
            
            if (len(old_operator) > 0): 
                result = plus(operation, old_operator) or minus(operation, old_operator) or multiply(operation, old_operator) or divide(operation, old_operator) or getRest(operation, old_operator)
                self.setState('operation', [result])                
                self.setState('displayNum', str(result))

        self.rerender()

    def clickTwoOperator(self, operator):
        if operator == "BackSpace": self.clickBackSpace()
        elif operator == "=": self.clickEqual()
        else:
            self.clickEqual()
            self.setState('operator', operator)
    
    def clickReset(self):
        self.setState('displayNum', "")
        self.setState('operation', [])
        self.setState('operator', "")
        self.rerender()

    def clickReciprocal(self):
        try:
            self.setState('displayNum', str(round(1 / float(self.getState('displayNum')), 10)))
        except ZeroDivisionError:
            self.clickReset()
            self.setState('displayNum', "0?????? ?????? ??? ????????????")
            
        self.rerender()

    def clickSquare(self):
        self.setState('displayNum', str(pow(float(self.getState('displayNum')), 2)))
        self.rerender()
            
    def clickSquareRoot(self):
        self.setState('displayNum', str(pow(float(self.getState('displayNum')), 1/2)))
        self.rerender()
    
    def clickOneOperator(self, operator):
        if operator == 'C' or operator == 'CE': self.clickReset()
        if operator == '%': self.clickTwoOperator(operator)
        if operator == '1/x': self.clickReciprocal()
        if operator == 'x??': self.clickSquare()
        if operator == '???': self.clickSquareRoot()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())