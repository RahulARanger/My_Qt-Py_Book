from PyQt5 import QtWidgets
import datetime


class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='Vertical Box Layouts')
        self.layout = QtWidgets.QVBoxLayout()
        self.window.setLayout(self.layout)
        self.widgets = [QtWidgets.QPushButton(self.window, text='At Index: {}'.format(i)) for i in range(3)]
        self.window.layout().addWidget(self.widgets[0])
        # ! non-stretchable
        self.window.layout().addSpacing(69)  # ? pady for the vbox and padx for the hbox
        self.window.layout().addWidget(self.widgets[1])
        self.window.layout().addWidget(self.widgets[2])
        self.window.show()


Test().exec()
