#Make sure to install the following modules/packages
#py -m pip install pyqt5

#import packages and modules
from PyQt5 import QtWidgets as qt
import sys

#define window class
class myUI:
    """This is a test UI for other projects
    """
    def __init__(self):
        """This initializes our window/UI and creates some useful pieces for other operations
        """
        self.app = qt.QApplication(sys.argv)
        self.window = qt.QMainWindow()
        self.screenSize = qt.QDesktopWidget().screenGeometry(-1)
        self.window.setGeometry(self.getDims()[1]/4, self.getDims()[0]/4, self.getDims()[1]/2, self.getDims()[0]/2)

    def createApp(self):
        """This renders our window
        """
        app = self.app
        window = self.window
        window.show()
        app.exec()

    def winTitle(self, title):
        """This allows us to change the title of our window

        Args:
            title (string): This argument is what our new window title will be set to
        """
        winTitle = title
        window = self.window
        window.setWindowTitle(winTitle)

    def getDims(self):
        """This allows returns the dimensions of the user window

        Returns:
            list: the list returned contains integer values of the screen resolution height and width
        """
        size = self.screenSize
        height = int(size.height())
        width = int(size.width())
        return height, width

    def sizeWin(self, width, height):
        self.window.setGeometry(self.getDims()[1]/4, self.getDims()[1]/4, width, height)

#create object
test = myUI()

#set window title
test.winTitle("Test")

#launch the window
test.createApp()

#testing stuff
#print(test.getDims())