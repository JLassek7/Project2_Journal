from warning import *
from PyQt5.QtWidgets import *
import csv
import datetime

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        #connect buttons to functions, connects the no button to the close function to close out the window
        self.no_button.clicked.connect(lambda: self.close())
        self.yes_button.clicked.connect(lambda: self.yes())

    def yes(self):
        '''
        This method looks for an entry in the records.csv file with the current date and sets all the fields associated with it to blank strings, effectively erasing it.
        '''
        date = datetime.datetime.now()
        with open("records.csv", "a") as file:
            content = csv.DictReader(file)
            for line in content:
                if line['Date'] == date.strftime("%x"):
                    line['Date'] = ""
                    line['Rating'] = ""
                    line['Workout'] = ""
                    line['Study'] = ""
                    line['Pray'] = ""
                    line['Game'] = ""
                    line['Comments'] = ""
        self.close()

