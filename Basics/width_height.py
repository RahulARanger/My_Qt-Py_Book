from PyQt5 import QtWidgets

a = QtWidgets.QApplication([])


class Test(QtWidgets.QWidget):
    def __init__(self):
        super().__init__(windowTitle='window with dimensions',
                         width=600, height=600, minimumWidth=300, minimumHeight=200,
                         maximumHeight=800, maximumWidth=1000)  # implicit way
        self.setMinimumHeight(500)  # explicit way
        self.setMinimumWidth(500)  # explicit way
        self.setMaximumHeight(700)  # explicit way
        self.setMaximumWidth(700)  # explicit  way
        self.setBaseSize(700, 700)  # explicit way
        self.show()
        # ? it is what it is 


b = Test()
a.exec()
