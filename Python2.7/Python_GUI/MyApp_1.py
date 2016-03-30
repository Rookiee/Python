#coding: utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per applicaiton
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
# app = QApplication(sys.argv)

'''
we create an instance of QApplication, passing in sys.arg (which contains 
command line arguments). This allows us to pass command line arguments to
our application. If you know you won’t be accepting command line arguments 
you can pass in an empty list instead, e.g.
'''
app = QApplication([])

# Start the event loop
app.exec_()
'''
The underscore is there because exec is a reserved word in Python and 
can’t be used as a function name. PyQt5 handles this by appending an 
underscore to the name used in the C++ library. You’ll also see it for .print_().
'''

# Your application won't reach here untile you exit and the event
# loop has stopped.

'''
The application should run without errors, yet there will be no indication
of anything happening, aside from perhaps a busy indicator. This is completely
 normal — we haven’t told Qt to create a window yet!
'''