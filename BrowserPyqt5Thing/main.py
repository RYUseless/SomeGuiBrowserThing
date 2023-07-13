"""
Hello, this is just some "fun" project of mine, I am not trully sure what i want to do with this...
For now, I am just trying some basic window sizing and some scaling in the future i hope
I am running OS linux, with gnome and some extensions (unite and other stuff)
Resolution I am able to test window scaling etc on are: 4k, 1440p (13inch) and fullhd(24 or 27 inch)
-ryuseless
"""
from PyQt5.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.resolutionHeight = QApplication.desktop().screenGeometry().height()
        self.resolutionWidth = QApplication.desktop().screenGeometry().width()
        appWidth = (int)(self.resolutionWidth*0.5)
        appHeight = (int)(self.resolutionHeight*0.5)
        self.setGeometry((int)(self.resolutionWidth/2-appWidth/2), (int)(self.resolutionHeight/2-appHeight/2),appWidth,appHeight)  # (xpos,ypos,width,height)
        self.showMaximized()

        print("Fullass monitor:",self.resolutionWidth,"x",self.resolutionHeight,"\nPolovina monitoru:",(int)(self.resolutionWidth/2),"x",(int)(self.resolutionHeight/2))
        #geometry is there for when the window is not in fulscreen, so the resolution is not like 30x30, dont know what it will do with scaling etc



app = QApplication(sys.argv)
QApplication.setApplicationName("Gugl z wishe")
window = MainWindow()
app.exec_()