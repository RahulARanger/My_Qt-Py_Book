from PyQt5 import QtCore, QtWidgets, QtGui
import resources


# This is best for icons/ images/ gifs not suitable for videos and audios

# we don't need to use qrc file again and the resources

class Test(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout())
        layer = QtWidgets.QHBoxLayout()
        self.layout().addLayout(layer)

        self.display = QtWidgets.QLabel(self)

        self.bye, self.image, self.gif = [QtWidgets.QPushButton(self) for _ in range(3)]
        self.image.setIcon(QtGui.QIcon(":/media/image"))
        self.gif.setIcon(QtGui.QIcon(":/media/gif"))
        self.bye.setIcon(QtGui.QIcon(":/media/close"))

        self.image.clicked.connect(lambda x=False: self.do(False))
        self.gif.clicked.connect(lambda x=True: self.do(True))
        self.bye.clicked.connect(self.close)

        layer.addWidget(self.gif)
        layer.addWidget(self.image)
        layer.addWidget(self.bye)

        self.layout().addWidget(self.display)

    def do(self, what):
        self.display.clear()
        if what:
            self.display.setMovie(QtGui.QMovie(":/media/pat_rem"))
            self.display.movie().start()
        else:
            self.display.setPixmap(QtGui.QPixmap(":/media/rem"))
            self.adjustSize()  # for adjusting the size


Check = QtWidgets.QApplication([])
run_this = Test()
run_this.show()
Check.exec()
