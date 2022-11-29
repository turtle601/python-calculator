import sys
from PyQt5.QtWidgets import *

from components.NumberDisplay import NumberDisplay
from buttons.ButtonOperator import ButtonOperator
from buttons.ButtonNumberPad import ButtonNumberPad
from buttons.ButtonCommand import ButtonCommand
 

class Main(QDialog):
    def __init__(self):
        super().__init__()

        self.state = { "cal_num" : "0" }
        
        self.layout = QGridLayout()    
        
        self.init_ui()

    def init_ui(self):
        self.makeComponent([
            NumberDisplay({
                'layout': self.layout,
                'getState': self.getState,
                'setState': self.setState
            }),

            ButtonNumberPad({
                'layout': self.layout
            }),    

            ButtonOperator({
                'layout': self.layout
            }),

            ButtonCommand({
               'layout': self.layout 
            })
        ])

        self.setLayout(self.layout)
        self.show()

    def makeComponent(self, componentInstanceArr): 
        for instance in componentInstanceArr:
            instance.render()
    
    def getState(self):
        return self.state['cal_num']; 

    def setState(self, newData):
        self.state["cal_num"] = newData
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())