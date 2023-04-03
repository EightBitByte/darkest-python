# interface/view.py
#
# The dialog module for the interface package.
# This is where the view (i.e. the main text display) is defined.
from PySide6 import QtWidgets, QtCore

class View(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(View, self).__init__(parent)

        # Initialize the label and style it
        self.label = QtWidgets.QLabel()

        self.label.setFrameShape(QtWidgets.QFrame.Shape.Panel.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.label.setLineWidth(1)
        self.label.setMidLineWidth(2)
        self.label.setStyleSheet('background-color: #d1d1d1')

        # Add the label to the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)

        self.setLayout(layout)


__all__ = [View.__name__]