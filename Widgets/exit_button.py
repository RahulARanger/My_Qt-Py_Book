from PyQt5 import QtWidgets


class ExitButt(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='Exit Button')
        self.layout = QtWidgets.QVBoxLayout()
        self.window.setLayout(self.layout)
        self.Exit = QtWidgets.QPushButton(self.window, text='Exit', toolTip='Click me to Exit')
        self.layout.addWidget(self.Exit)
        self.Exit.clicked.connect(self.window.close)
        # self.Exit.clicked.connect(self.exit) will close all the Windows inside the QApplication
        self.window.show()


ExitButt().exec()
