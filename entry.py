# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entry.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JournalEntry(object):
    def setupUi(self, JournalEntry):
        JournalEntry.setObjectName("JournalEntry")
        JournalEntry.resize(450, 600)
        JournalEntry.setMinimumSize(QtCore.QSize(450, 600))
        JournalEntry.setMaximumSize(QtCore.QSize(450, 600))
        self.centralwidget = QtWidgets.QWidget(JournalEntry)
        self.centralwidget.setObjectName("centralwidget")
        self.rating_input = QtWidgets.QComboBox(self.centralwidget)
        self.rating_input.setGeometry(QtCore.QRect(310, 50, 73, 21))
        self.rating_input.setMaxCount(2147483646)
        self.rating_input.setObjectName("rating_input")
        self.rating_input.addItem("")
        self.rating_input.addItem("")
        self.rating_input.addItem("")
        self.rating_input.addItem("")
        self.rating_input.addItem("")
        self.rating_input.addItem("")
        self.rating_input.addItem("")
        self.rating_input.addItem("")
        self.rating_input.addItem("")
        self.rating_input.addItem("")
        self.rating_label = QtWidgets.QLabel(self.centralwidget)
        self.rating_label.setGeometry(QtCore.QRect(30, 40, 161, 31))
        self.rating_label.setObjectName("rating_label")
        self.workout_label = QtWidgets.QLabel(self.centralwidget)
        self.workout_label.setGeometry(QtCore.QRect(30, 100, 221, 31))
        self.workout_label.setObjectName("workout_label")
        self.study_label = QtWidgets.QLabel(self.centralwidget)
        self.study_label.setGeometry(QtCore.QRect(30, 160, 271, 21))
        self.study_label.setObjectName("study_label")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(350, 510, 93, 28))
        self.submit_button.setObjectName("submit_button")
        self.workout_input = QtWidgets.QLineEdit(self.centralwidget)
        self.workout_input.setGeometry(QtCore.QRect(310, 100, 71, 22))
        self.workout_input.setObjectName("workout_input")
        self.study_input = QtWidgets.QLineEdit(self.centralwidget)
        self.study_input.setGeometry(QtCore.QRect(310, 160, 71, 22))
        self.study_input.setObjectName("study_input")
        self.pray_label = QtWidgets.QLabel(self.centralwidget)
        self.pray_label.setGeometry(QtCore.QRect(30, 215, 211, 31))
        self.pray_label.setObjectName("pray_label")
        self.pray_input = QtWidgets.QComboBox(self.centralwidget)
        self.pray_input.setGeometry(QtCore.QRect(310, 220, 73, 22))
        self.pray_input.setMaxVisibleItems(2)
        self.pray_input.setObjectName("pray_input")
        self.pray_input.addItem("")
        self.pray_input.addItem("")
        self.games_label = QtWidgets.QLabel(self.centralwidget)
        self.games_label.setGeometry(QtCore.QRect(30, 290, 281, 16))
        self.games_label.setObjectName("games_label")
        self.games_input = QtWidgets.QLineEdit(self.centralwidget)
        self.games_input.setGeometry(QtCore.QRect(310, 290, 71, 22))
        self.games_input.setObjectName("games_input")
        self.comments_label = QtWidgets.QLabel(self.centralwidget)
        self.comments_label.setGeometry(QtCore.QRect(30, 350, 211, 16))
        self.comments_label.setObjectName("comments_label")
        self.comments_input = QtWidgets.QTextEdit(self.centralwidget)
        self.comments_input.setGeometry(QtCore.QRect(30, 390, 341, 87))
        self.comments_input.setObjectName("comments_input")
        self.error_messege = QtWidgets.QLabel(self.centralwidget)
        self.error_messege.setGeometry(QtCore.QRect(130, 490, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.error_messege.setFont(font)
        self.error_messege.setText("")
        self.error_messege.setObjectName("error_messege")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(0, 510, 121, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        JournalEntry.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JournalEntry)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 26))
        self.menubar.setObjectName("menubar")
        JournalEntry.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JournalEntry)
        self.statusbar.setObjectName("statusbar")
        JournalEntry.setStatusBar(self.statusbar)

        self.retranslateUi(JournalEntry)
        self.pray_input.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(JournalEntry)

    def retranslateUi(self, JournalEntry):
        _translate = QtCore.QCoreApplication.translate
        JournalEntry.setWindowTitle(_translate("JournalEntry", "Journal Entry"))
        self.rating_input.setItemText(0, _translate("JournalEntry", "1"))
        self.rating_input.setItemText(1, _translate("JournalEntry", "2"))
        self.rating_input.setItemText(2, _translate("JournalEntry", "3"))
        self.rating_input.setItemText(3, _translate("JournalEntry", "4"))
        self.rating_input.setItemText(4, _translate("JournalEntry", "5"))
        self.rating_input.setItemText(5, _translate("JournalEntry", "6"))
        self.rating_input.setItemText(6, _translate("JournalEntry", "7"))
        self.rating_input.setItemText(7, _translate("JournalEntry", "8"))
        self.rating_input.setItemText(8, _translate("JournalEntry", "9"))
        self.rating_input.setItemText(9, _translate("JournalEntry", "10"))
        self.rating_label.setText(_translate("JournalEntry", "How would you rate today?"))
        self.workout_label.setText(_translate("JournalEntry", "How long did you workout (in hours)?"))
        self.study_label.setText(_translate("JournalEntry", "How long did you study/read today (in hours)?"))
        self.submit_button.setText(_translate("JournalEntry", "Submit"))
        self.pray_label.setText(_translate("JournalEntry", "Did you go to church/pray today?"))
        self.pray_input.setItemText(0, _translate("JournalEntry", "No"))
        self.pray_input.setItemText(1, _translate("JournalEntry", "Yes"))
        self.games_label.setText(_translate("JournalEntry", "How long did you play video games (in hours)?"))
        self.comments_label.setText(_translate("JournalEntry", "Write a bit about the day:"))
        self.clear_button.setText(_translate("JournalEntry", "Clear Today\'s Entry"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JournalEntry = QtWidgets.QMainWindow()
    ui = Ui_JournalEntry()
    ui.setupUi(JournalEntry)
    JournalEntry.show()
    sys.exit(app.exec_())
