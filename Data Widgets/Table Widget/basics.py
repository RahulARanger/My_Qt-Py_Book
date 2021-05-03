from PyQt5 import QtWidgets, QtCore, QtGui


class test(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.sample_widgets = [
            QtWidgets.QLabel(text=f"Works: {_}") for _ in range(9)
        ]
        self.test_on = QtWidgets.QTableWidget(3, 3, self)
        # self.test_on.setRowCount(3)
        # self.test_on.setColumnCount(3)

        print(f"Number of rows: {self.test_on.rowCount()}, Number of Columns: {self.test_on.columnCount()}")
        self.setLayout(QtWidgets.QHBoxLayout())
        self.arrange_table()
        self.layout().addWidget(self.test_on)

    def arrange_table(self):
        count = 0
        for _ in range(self.test_on.rowCount()):
            for __ in range(self.test_on.columnCount()):
                self.test_on.setCellWidget(_, __, self.sample_widgets[count])
                count += 1


testing = QtWidgets.QApplication([])
sample = test()
sample.show()
testing.exec()
