import datetime
from PyQt5.QtWidgets import *
from entry import *
from warning import *
import csv

class Controller(QMainWindow, Ui_JournalEntry, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        
        #connect the button to their functions
        self.submit_button.clicked.connect(lambda: self.submit())
        self.clear_button.clicked.connect(lambda: self.warning())

        
    def submit(self):
        '''
        Takes the values entered and writes them to the records.csv file if the data entered are valid.
        Raises and displays an error if the workout, study, or game values are non-numeric or if an entry already exists for the current date in records.csv
        '''
        try:
            #Gets the values from the GUI fields
            rating = self.rating_input.currentText()
            workout = float(self.workout_input.text())
            study = float(self.study_input.text())
            pray = self.pray_input.currentText()
            game = float(self.games_input.text())
            date = datetime.datetime.now()
            comments = self.comments_input.toPlainText()
            total_input = [date.strftime("%x"), rating, workout, study, pray, game, comments]

            #Checks if an entry for the current date already exists
            with open("records.csv", "r") as file:
                content = csv.DictReader(file)
                for line in content:
                    if line['Date'] == date.strftime("%x"):
                        raise KeyError

            #writes date to the records file
            with open("records.csv", "a") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(total_input)

            self.success()

        except ValueError:
            self.error_messege.setText("The answers to the workout, \nstudy, and gaming questions \nneeds to be numberic!")

        except KeyError:
            self.error_messege.setText("An entry for today \nhas already been recorded!")

    
    def success(self):
        '''
        Runs after a submission to the records.csv file. 
        Clears all the GUI fields and displays a success messege to the user.
        '''
        self.workout_input.clear()
        self.study_input.clear()
        self.games_input.clear()
        self.comments_input.clear()
        self.error_messege.setText("Submission Successful!")

    def warning(self):
        '''
        Brings up the warning messege box to confirm the user wants to delete the current date's entry
        '''
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
