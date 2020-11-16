# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(485, 408)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 621, 431))
        self.tabs.setObjectName("tabs")
        self.uniform = QtWidgets.QWidget()
        self.uniform.setObjectName("uniform")
        self.label = QtWidgets.QLabel(self.uniform)
        self.label.setGeometry(QtCore.QRect(20, 10, 101, 16))
        self.label.setObjectName("label")
        self.a_even = QtWidgets.QLineEdit(self.uniform)
        self.a_even.setGeometry(QtCore.QRect(20, 30, 31, 20))
        self.a_even.setObjectName("a_even")
        self.b_even = QtWidgets.QLineEdit(self.uniform)
        self.b_even.setGeometry(QtCore.QRect(80, 30, 31, 20))
        self.b_even.setObjectName("b_even")
        self.label_2 = QtWidgets.QLabel(self.uniform)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 101, 16))
        self.label_2.setObjectName("label_2")
        self.number_count_even = QtWidgets.QLineEdit(self.uniform)
        self.number_count_even.setGeometry(QtCore.QRect(20, 80, 113, 20))
        self.number_count_even.setObjectName("number_count_even")
        self.run_even = QtWidgets.QPushButton(self.uniform)
        self.run_even.setGeometry(QtCore.QRect(20, 160, 101, 23))
        self.run_even.setObjectName("run_even")
        self.label_3 = QtWidgets.QLabel(self.uniform)
        self.label_3.setGeometry(QtCore.QRect(190, 220, 21, 21))
        self.label_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.uniform)
        self.label_4.setGeometry(QtCore.QRect(210, 230, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.uniform)
        self.label_5.setGeometry(QtCore.QRect(190, 250, 21, 21))
        self.label_5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.uniform)
        self.label_6.setGeometry(QtCore.QRect(210, 260, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.uniform)
        self.label_7.setGeometry(QtCore.QRect(190, 280, 21, 21))
        self.label_7.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.m_theor = QtWidgets.QLabel(self.uniform)
        self.m_theor.setGeometry(QtCore.QRect(250, 220, 47, 21))
        self.m_theor.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.m_theor.setObjectName("m_theor")
        self.m_pract = QtWidgets.QLabel(self.uniform)
        self.m_pract.setGeometry(QtCore.QRect(250, 250, 47, 21))
        self.m_pract.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.m_pract.setObjectName("m_pract")
        self.dispertion = QtWidgets.QLabel(self.uniform)
        self.dispertion.setGeometry(QtCore.QRect(250, 280, 47, 21))
        self.dispertion.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.dispertion.setObjectName("dispertion")
        self.accurancy_even = QtWidgets.QLineEdit(self.uniform)
        self.accurancy_even.setGeometry(QtCore.QRect(20, 130, 113, 20))
        self.accurancy_even.setObjectName("accurancy_even")
        self.label_13 = QtWidgets.QLabel(self.uniform)
        self.label_13.setGeometry(QtCore.QRect(20, 110, 101, 16))
        self.label_13.setObjectName("label_13")
        self.save_to_file = QtWidgets.QPushButton(self.uniform)
        self.save_to_file.setGeometry(QtCore.QRect(370, 210, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_to_file.setFont(font)
        self.save_to_file.setObjectName("save_to_file")
        self.even_list = QtWidgets.QTextEdit(self.uniform)
        self.even_list.setEnabled(True)
        self.even_list.setGeometry(QtCore.QRect(200, 20, 241, 171))
        self.even_list.setObjectName("even_list")
        self.tabs.addTab(self.uniform, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Range"))
        self.a_even.setText(_translate("MainWindow", "0.6"))
        self.b_even.setText(_translate("MainWindow", "1.2"))
        self.label_2.setText(_translate("MainWindow", "Number count"))
        self.number_count_even.setText(_translate("MainWindow", "1000"))
        self.run_even.setText(_translate("MainWindow", "Form"))
        self.label_3.setText(_translate("MainWindow", "М"))
        self.label_4.setText(_translate("MainWindow", "теор"))
        self.label_5.setText(_translate("MainWindow", "М"))
        self.label_6.setText(_translate("MainWindow", "практ"))
        self.label_7.setText(_translate("MainWindow", "D"))
        self.m_theor.setText(_translate("MainWindow", "0.0"))
        self.m_pract.setText(_translate("MainWindow", "0.0"))
        self.dispertion.setText(_translate("MainWindow", "0.0"))
        self.accurancy_even.setText(_translate("MainWindow", "0.04"))
        self.label_13.setText(_translate("MainWindow", "Accuracy"))
        self.save_to_file.setText(_translate("MainWindow", "Save to file"))
        self.tabs.setTabText(self.tabs.indexOf(self.uniform), _translate("MainWindow", "Even"))
