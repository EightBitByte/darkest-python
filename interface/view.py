# interface/view.py
#
# The dialog module for the interface package.
# This is where the view (i.e. the main text display) is defined.
from PySide6 import QtWidgets, QtCore

class View(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(View, self).__init__(parent)

        # Initialize the label and style it
        label = QtWidgets.QLabel()

        label.setFrameShape(QtWidgets.QFrame.Shape.Panel.WinPanel)
        label.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        label.setLineWidth(1)
        label.setMidLineWidth(2)
        label.setStyleSheet('background-color: #d1d1d1')

        # Add the label to the layout
        layout = QtWidgets.QVBoxLayout()
        layout.setDirection(QtWidgets.QVBoxLayout.LeftToRight)
        layout.addWidget(label, stretch = 75)
        layout.addStretch(stretch = 25)

        self.setLayout(layout)


__all__ = [View.__name__]