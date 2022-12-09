# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 150)
        MainWindow.setMinimumSize(QtCore.QSize(375, 150))
        MainWindow.setMaximumSize(QtCore.QSize(375, 150))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.warning_label = QtWidgets.QLabel(self.centralwidget)
        self.warning_label.setGeometry(QtCore.QRect(30, 10, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setKerning(True)
        self.warning_label.setFont(font)
        self.warning_label.setObjectName("warning_label")
        self.yes_button = QtWidgets.QPushButton(self.centralwidget)
        self.yes_button.setGeometry(QtCore.QRect(50, 70, 93, 28))
        self.yes_button.setObjectName("yes_button")
        self.no_button = QtWidgets.QPushButton(self.centralwidget)
        self.no_button.setGeometry(QtCore.QRect(220, 70, 90, 30))
        self.no_button.setMinimumSize(QtCore.QSize(0, 0))
        self.no_button.setMaximumSize(QtCore.QSize(90, 30))
        self.no_button.setObjectName("no_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 375, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Are You Sure?"))
        self.warning_label.setText(_translate("MainWindow", "Are you sure you want to delete today\'s entry?"))
        self.yes_button.setText(_translate("MainWindow", "Yes"))
        self.no_button.setText(_translate("MainWindow", "No"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())