from PyQt5 import QtWidgets, QtGui


class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='Buttons with Icons')
        self.icon_button = QtWidgets.QPushButton(self.window, text='Received')
        self.icon_button.setIcon(QtGui.QIcon(
            'ic_call_received_36pt_2x.png'))  # left will be the icon and right to it will be the text (normal UI
        # format)
        self.icon_button.move(100, 100)
        self.window.show()


test().exec()
