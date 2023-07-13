"""
Hello, this is just some "fun" project of mine, I am not trully sure what i want to do with this...
For now, I am just trying some basic window sizing and some scaling in the future i hope
I am running OS linux, with gnome and some extensions (unite and other stuff)
Resolution I am able to test window scaling etc on are: 4k, 1440p (13inch) and fullhd(24 or 27 inch)
-ryuseless
"""
import sys
from PyQt5.QtWidgets import QVBoxLayout,QMainWindow,QApplication,QLabel,QWidget
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):
        label1 = QLabel(self)

        label1.setText("<font color=yellow>EPIC GUGL FROM WISH</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.red)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        self.setLayout(vbox)

        self.setWindowTitle('Gugl z wishe')

        self.resolutionHeight = QApplication.desktop().screenGeometry().height()
        self.resolutionWidth = QApplication.desktop().screenGeometry().width()

        appHeight = (int)(self.resolutionHeight * 0.5) #APPHEIGHT value
        appWidth = (int)(self.resolutionWidth * 0.5) #APPWIDTH value

        self.setGeometry(self.resolutionWidth // 2 - appWidth // 2, self.resolutionHeight // 2 - appHeight // 2, appWidth, appHeight)  #(xpos,ypos,width,height)
        self.showMaximized()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())