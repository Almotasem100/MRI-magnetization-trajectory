from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, QMessageBox, QLabel)
from PyQt5.QtGui import QIcon, QPixmap
import pyqtgraph as pg
from pyqtgraph import ImageView, PlotWidget
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
import sys
import cv2 as cv
import numpy as np
import random

from Task2 import Ui_MainWindow
from imageModel import ImageModel


class ApplicationWindow(QtWidgets.QMainWindow):
    
           
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Image.triggered.connect(lambda: self.uploadimage())
        self.ui.comboBox.currentTextChanged.connect(lambda: self.inputcombobox())
        self.ui.pushButton.clicked.connect(self.random)
        self.ui.graph2.clicked.connect(self.freq)
        self.hidebuttons = [self.ui.widget, self.ui.widget_1]
        for j in range(len(self.hidebuttons)):
            self.hidebuttons[j].ui.histogram.hide()
            self.hidebuttons[j].ui.roiBtn.hide()
            self.hidebuttons[j].ui.menuBtn.hide()
            self.hidebuttons[j].ui.roiPlot.hide()

        self.field =[1.5 for i in range(150)] 
        self.flag=False


    def uploadimage(self):
        self.image = QtWidgets.QFileDialog.getOpenFileName(None, 'Open',
                                                           'D:/BIOMEDICAL ENGINEERING/3rd/2nd semester/MRI',
                                                           "images(*.jpg *.png)")
        self.image1 = ImageModel(imgPath=self.image[0])
        self.ui.widget.show()
        self.ui.widget.setImage(self.image1.imgByte.T)

    def inputcombobox(self):
        self.ui.widget_1.clear()
        self.ui.widget_1.show()
        if (str(self.ui.comboBox.currentText())) == 'Phase':
            self.ui.widget_1.setImage(self.image1.phase.T)
        elif (str(self.ui.comboBox.currentText())) == 'Magnitude':
            self.ui.widget_1.setImage(20 * np.log(np.fft.fftshift(self.image1.magnitude) + 1).T)
        elif (str(self.ui.comboBox.currentText())) == 'Real':
            self.ui.widget_1.setImage(20 * np.log(self.image1.real + 1).T)
        elif (str(self.ui.comboBox.currentText())) == 'Imaginary':
            self.ui.widget_1.setImage(20 * np.log(self.image1.imaginary + 1).T)

    def random(self):
        self.flag=True
        for i in range(150):
            randomVal = random.uniform(-0.15, 0.15)
            self.field[i]=randomVal+1.5
        self.length = np.arange(0, 150, 1)  # centimeter
        self.ui.widget_2.showGrid(x=True, y=True)
        self.ui.widget_2.setXRange(0, 150, padding=0)
        self.ui.widget_2.setLabel('left', 'Magnet', color='white', size=30)
        self.ui.widget_2.setLabel('bottom', 'Z-axis', color='white', size=30)
        self.pen = pg.mkPen(color=(204, 0, 204))
        self.ui.widget_2.clear()
        self.ui.widget_2.plot(self.length,self.field, pen=self.pen)

    def freq(self):
     if self.flag:   
        gamma = 4.258
        larmorfreq =np.multiply(gamma,self.field)
        freq_diff=[0 for i in range(150)]
        for i in range(149):
          freq_diff[i]=larmorfreq[i+1]-larmorfreq[i]  
        self.ui.widget_3.showGrid(x=True, y=True)
        # self.ui.widget_3.setXRange(0, 150, padding=0)
        self.ui.widget_3.setLabel('left', 'freq', color='white', size=30)
        self.ui.widget_3.setLabel('bottom', 'field', color='white', size=30)
        self.ui.widget_3.clear()
        self.ui.widget_3.plot(self.field,larmorfreq, pen=self.pen)


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    # Now use a palette to switch to dark colors:
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
