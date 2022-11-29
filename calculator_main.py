import sys
from PyQt5.QtWidgets import *

from buttons.ButtonInput import ButtonInput
 

class Main(QDialog):
    def __init__(self):
        super().__init__()

        self.state = { "cal_num" : "0" }
        self.init_ui()

    def init_ui(self):
        self.makeComponent([
            ButtonInput({
                'getState': self.getState,
                'setState': self.setState
            }),
        ])
            
        self.show()

    def makeComponent(self, componentInstanceArr): 
        for instance in componentInstanceArr:
            self.setLayout(instance.render())
    
    def getState(self):
        return self.state['cal_num']; 

    def setState(self, newData):
        self.state["cal_num"] = newData
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())