# GUI

# libraries
import sys
from PyQt4 import QtGui, QtCore

# create window
class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,100,800,500) # window position and size
        self.setWindowTitle("Database")
        self.setWindowIcon(QtGui.QIcon("dblogo.png"))

        home(self)

def home(self):
    
    
    self.show()

# run application
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec())

run()