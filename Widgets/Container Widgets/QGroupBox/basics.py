from PyQt5 import QtWidgets


# Refer thivs Website: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QGroupBox.html#more
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='QGroupBox')
        self.mainl = QtWidgets.QVBoxLayout()
        self.grouped = QtWidgets.QGroupBox('Group: 1',
                                           self.window,
                                           checkable=True,  # with checkbox to view it or not
                                           flat=False)  # whether the relief is Flat or frame)
        # title and then parent
        # ! there's alignment parameter for the groupbox refer the side
        self.window.setLayout(self.mainl)
        self.mainl.addWidget(self.grouped)
        self.layout = QtWidgets.QVBoxLayout()
        self.grouped.setLayout(self.layout)
        self.layout.addWidget(QtWidgets.QDateTimeEdit(self.grouped, toolTip='Select Date and Time', calendarPopup=True))
        self.window.show()


test().exec()
