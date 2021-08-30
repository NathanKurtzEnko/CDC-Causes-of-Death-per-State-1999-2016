#import packages and modules
from PyQt5 import QtWidgets as qt


#define window class
class myUI:
    """This is a test UI for other projects
    """
    def __init__(self):
        self.app = qt.QApplication([])
        self.label = qt.QLabel('Hello world')
        self.window = qt.QWidget()

    def createApp(self):
        app = self.app
        window = self.window
        window.show()
        app.exec()

    def winTitle(self, title):
        winTitle = title
        window = self.window
        window.setWindowTitle(winTitle)



#create object
test = myUI()

#set window title
test.winTitle("Test")

#launch the window
test.createApp()