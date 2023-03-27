# interface/dialog.py
#
# The dialog module for the interface package.
# This is where the dialogue box is defined.
from PySide6 import QtCore, QtWidgets

class DialogBox(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(DialogBox, self).__init__(parent)

        # Editing and sending widgets
        self.edit = QtWidgets.QLineEdit()
        self.send = QtWidgets.QPushButton('Send')

        self.send.clicked.connect(self.printInfo)
        self.edit.returnPressed.connect(self.printInfo)

        # Create and set layout alignment
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setDirection(QtWidgets.QVBoxLayout.LeftToRight)

        # Add the widgets with their stretch parameters
        self.layout.addWidget(self.edit, alignment = QtCore.Qt.AlignBottom, stretch = 60)
        self.layout.addWidget(self.send, alignment = QtCore.Qt.AlignBottom, stretch = 15)
        self.layout.addStretch(stretch = 25)

        self.setLayout(self.layout)


    @QtCore.Slot()
    def printInfo(self):
        if len(self.edit.displayText()) != 0:
            print(self.edit.displayText())
            self.edit.clear()

__all__ = [DialogBox.__name__]