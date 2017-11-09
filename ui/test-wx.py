# TestProgramWithGUI.py
# This is a program for testing Qt GUI and PySide

#coding:utf-8
import sys

# Import Qt GUI component
from PySide.QtGui import *

# Import GUI File
from TestGUI import Ui_MainWindow

# Self Function
def PrintHello():
    print("hello")

# Make main window class
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Sample Window")
        # Connect button click event to PrintHello function
        QToolTip.setFont(QFont("Decorative", 8, QFont.Bold))
        self.setToolTip('Our Main Window')
        self.pushButton.clicked.connect(PrintHello)
        self.pushButton.setToolTip('cmd print char')
        self.closed_win.setToolTip('closed program')
    def setIcon(self):
        appIcon = QIcon("C:\pyside_test\pyside_logo.png")
        self.setWindowIcon(appIcon)
    def setIconModes(self):
        myIcon1 = QIcon('pyside_logo.png')
        myLabel1 = QLabel('sample', self)
        pixmap1 = myIcon1.pixmap(50, 50, QIcon.Active, QIcon.On)
        myLabel1.setPixmap(pixmap1)
        myLabel1.setToolTip('Active Icon')
        
        myIcon2 = QIcon('pyside_logo.png')
        myLabel2 = QLabel('sample', self)
        pixmap2 = myIcon2.pixmap(50, 50, QIcon.Disabled, QIcon.Off)
        myLabel2.setPixmap(pixmap2)
        myLabel2.move(50, 0)
        myLabel2.setToolTip('Disabled Icon')
        
        myIcon3 = QIcon('pyside_logo.png')
        myLabel3 = QLabel('sample', self)
        pixmap3 = myIcon3.pixmap(50, 50, QIcon.Selected, QIcon.On)
        myLabel3.setPixmap(pixmap3)
        myLabel3.move(100, 0)
        myLabel3.setToolTip('Selected Icon')
# End of main window class


# Main Function
if __name__=='__main__':
    Program = QApplication(sys.argv)
    Window=MainWindow()
    Window.setIcon()
    Window.setIconModes()
    Window.show()
    Program.exec_()