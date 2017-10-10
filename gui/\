import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSlot
app = QApplication(sys.argv)
w = QWidget()
w.resize(320, 240)
w.setWindowTitle("Hello World!")
button = QPushButton("Hello World", w)
button.setToolTip("Click to Quit!")
btn = QPushButton("Not your ordinary Hello World!", w)
#button.clicked.connect(exit)
#button.resize(button.sizeHint())
button.move(100, 80)

@pyqtSlot()
def on_click():
	print('clicked')

button.clicked.connect(on_click)

w.show()

newWidget = QWidget()
result = QMessageBox.question(w, "Message", "Do you like Python?", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)

if result == QMessageBox.Yes:
	print "Yes"
else:
	print "No"

sys.exit(app.exec_())
