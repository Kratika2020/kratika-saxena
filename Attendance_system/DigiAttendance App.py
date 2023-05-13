5# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 13:35:37 2021

@author: Kratika
"""

import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from welcome import Ui_Form1
from gui_attend import Ui_Form


counter = 0

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

      
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form1()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.show()
       
    def progress(self):

        global counter
        self.ui.progressBar.setValue(counter)

        if counter > 100:
           
            self.timer.stop()

            self.main = MainWindow()
            self.main.show()

            self.close()

       
        counter += 1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())