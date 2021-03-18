from PyQt5 import QtWidgets
# * Refer https://doc.qt.io/qtforpython/PySide6/QtWidgets/QListWidgetItem.html#PySide6.QtWidgets.PySide6.QtWidgets.QListWidgetItem for QListWidgetItem
# * Refer https://doc.qt.io/qtforpython/PySide6/QtWidgets/QListWidget.html#more for QListWidget()
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='QListWidget')
        self.layout=QtWidgets.QVBoxLayout()
        self.lstbox=QtWidgets.QListWidget(self.window)
        self.row1=QtWidgets.QListWidgetItem('Testing1',self.lstbox)
        # QListWidgetItem allows more customization and helps us keep track  of items easily
        self.lstbox.addItem('Testing3')
        self.lstbox.insertItem(1,'Testing2') # pos starts from 0
        self.window.setLayout(self.layout)
        self.layout.addWidget(self.lstbox)
        self.window.show()
test().exec()