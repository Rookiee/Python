#coding: utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Only needed for access to command line arguments
import sys

'''
If you want to create a custom window, the best approach
 is to subclass QMainWindow and then include the setup for
  the window in the __init__ block. This allows the window
   behaviour to be self contained. So lets add our own subclass
    of QMainWindow — we can call it MainWindow to keep things simple.
'''

class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		self.setWindowTitle("My Awesome App")
		label = QLabel("This is Awesome")

		# The 'Qt' namespace has lots of attributes to customise
		# widgets, See: http://doc.qt.io/qt-5/qt.html
		label.setAlignment(Qt.AlignCenter)

		# Set the central widget of the Window. Widget will expand
		# to take up all the space in Window by default.
		self.setCentralWidget(label)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()


'''
Notice how we write the __init__ block with a small
bit of boilerplate to take the arguments (none currently)
and pass them up to the __init__ of the parent QMainWindow class.
'''
'''
When you subclass a Qt class you must always call the super __init__ function
 to allow Qt to set up the object.
'''