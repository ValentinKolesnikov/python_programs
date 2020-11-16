# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Plot(object):
    def setupUi(self, Plot):
        Plot.setObjectName("Plot")
        Plot.resize(588, 413)
        self.centralwidget = QtWidgets.QWidget(Plot)
        self.centralwidget.setObjectName("centralwidget")
        Plot.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Plot)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 21))
        self.menubar.setObjectName("menubar")
        Plot.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Plot)
        self.statusbar.setObjectName("statusbar")
        Plot.setStatusBar(self.statusbar)

        self.retranslateUi(Plot)
        QtCore.QMetaObject.connectSlotsByName(Plot)

    def retranslateUi(self, Plot):
        _translate = QtCore.QCoreApplication.translate
        Plot.setWindowTitle(_translate("Plot", "График функции"))
