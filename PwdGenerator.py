import math
from PyQt6 import QtCore, QtWidgets
import string
import random


class PwdGenerator_UI(QtWidgets.QMainWindow):
    def __init__(self):
        global combo, checkboxes
        super().__init__()
        # set window size and title
        self.setMinimumSize(QtCore.QSize(500, 150))
        self.setWindowTitle('Password Generator - Settings')
        # Set Grid Layout
        widget = QtWidgets.QWidget(self)
        self.setCentralWidget(widget)
        grid = QtWidgets.QGridLayout()
        widget.setLayout(grid)
        # row 0 with descriptions
        desc_list = ['Set the length of the password to generate:', 'Password Character Options:', ' ']
        row = 0
        for desc in desc_list:
            lbl = QtWidgets.QLabel(desc)
            lbl.resize(lbl.sizeHint())
            grid.addWidget(lbl, row, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
            row += 1
        # row 1 with combobox
        for row in range(len(desc_list)):
            # create options for user
            if row == 0:
                i = 12
                combo = QtWidgets.QComboBox(self)
                while i < 50:
                    combo.addItem(str(i))
                    i += 1
                grid.addWidget(combo, row, 4, QtCore.Qt.AlignmentFlag.AlignRight)
            elif row == 2:
                # cancel
                button = QtWidgets.QPushButton('Cancel')
                button.clicked.connect(self.cancel)
                grid.addWidget(button, row, 3, QtCore.Qt.AlignmentFlag.AlignRight)

                # ok
                button = QtWidgets.QPushButton('OK')
                button.clicked.connect(self.ok)
                grid.addWidget(button, row, 4, QtCore.Qt.AlignmentFlag.AlignRight)
            else:
                options = ['upper case letters', 'numbers', 'special characters']
                c = 2
                for option in options:
                    box = QtWidgets.QCheckBox(option, self)
                    box.setChecked(True)
                    grid.addWidget(box, row, c, QtCore.Qt.AlignmentFlag.AlignCenter)
                    checkboxes += [box]
                    c += 1


    # cancel button in UI
    def cancel(self):
        app.quit()

    
    # proceed with OK button
    def ok(self):
        pwd_chars = int(combo.currentText())
        # double check length - password should not have less than 12 characters
        if pwd_chars < 12:
            QtWidgets.QMessageBox.warning(self, "Error", "Too little characters chosen for password. The password length should be at least 12 characters.")
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        number = string.digits
        special = '!"§$%&/()=?\\+*#,.-;:_<>@ €'
        # if any of the checkboxes is checked a random number of additional chars is needed
        if checkboxes[0].isChecked() or checkboxes[1].isChecked() or checkboxes[2].isChecked():
            r = random.randint(1, pwd_chars)
        else:
            r = 0
        # start with lower case letters
        pwd = random.choices(lower, k = pwd_chars-r)
        # check options
        if checkboxes[0].isChecked() and checkboxes[1].isChecked() and checkboxes[2].isChecked():
            sc = random.randint(1, math.ceil(r/2))
            i = math.floor((r-sc)/2)
        elif checkboxes[0].isChecked() and checkboxes[1].isChecked() and not checkboxes[2].isChecked():
            i = math.floor(r/2)
            sc = 0
        elif (checkboxes[0].isChecked() and checkboxes[2].isChecked()) or (checkboxes[1].isChecked() and checkboxes[2].isChecked()):
            sc = random.randint(1, r)
            i = r-sc
        elif not checkboxes[0].isChecked() and not checkboxes[1].isChecked() and checkboxes[2].isChecked():
            i = 0
            sc = random.randint(1, r)
        elif not checkboxes[2].isChecked() and (checkboxes[0].isChecked() or checkboxes[1].isChecked()):
            i = r-random.randint(1, r)
            sc = 0
        else:
            i = 0
            sc = 0
        # upper case chars
        j = 0
        if checkboxes[0].isChecked():
            while j < i:
                pwd += [upper[random.randint(0, len(upper) - 1)]]
                j += 1
        if checkboxes[1].isChecked():
        # numbers
            j = 0
            while j < i:
                pwd += [number[random.randint(0, len(number) - 1)]]
                j += 1
        if checkboxes[2].isChecked():
        # special characters
            j = 0
            while j < sc:
                pwd += [special[random.randint(0, len(special) - 1)]]
                j += 1
        # correction due to rounding down
        while len(pwd) < pwd_chars:
            pwd += [lower[random.randint(0, len(lower) - 1)]]
        # remix
        random.shuffle(pwd)
        msg = QtWidgets.QMessageBox(self)
        msg.setStyleSheet("QLabel{min-width: 300px;}")
        msg.setWindowTitle('Success!')
        msg.setText('Generated Password:')
        msg.setDetailedText(''.join(pwd))
        msg.exec()


# start application
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    combo = []
    checkboxes = []
    window = PwdGenerator_UI()
    window.show()
    app.exec()