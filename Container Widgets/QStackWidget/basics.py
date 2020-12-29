from PyQt5 import QtWidgets
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='QStackWidgets')
        self.layout=QtWidgets.QVBoxLayout()
        self.window.setLayout(self.layout)
        self.container=QtWidgets.QStackedWidget(self.window)
        self.layout.addWidget(self.container)
        self.container.addWidget(QtWidgets.QPushButton(self.window,text='Testing1'))
        self.container.addWidget(QtWidgets.QPushButton(self.window,text='Testing2'))
        
        self.window.show()
test().exec()