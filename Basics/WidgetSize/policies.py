from PyQt5 import QtWidgets, QtCore


class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='Size Policy')
        self.layout = QtWidgets.QVBoxLayout()
        self.window.setLayout(self.layout)
        self.fixed = QtCore.QSize(300, 10)
        self.expand = QtCore.QSize(400, 10)
        self.entry1 = QtWidgets.QLineEdit(self.window, toolTip='Normal', clearButtonEnabled=True)
        self.entry2 = QtWidgets.QLineEdit(self.window, toolTip='Fixed', clearButtonEnabled=True)
        self.entry3 = QtWidgets.QLineEdit(self.window, toolTip='Entry', clearButtonEnabled=True)
        self.layout.addWidget(self.entry1)
        self.layout.addWidget(self.entry2)
        self.layout.addWidget(self.entry3)
        self.entry1.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        # ? QtWidgets.QSizePolicy.Preferred is the default size policy for the widgets (may nt be for all the widgets
        # for instance linedit has fixed policy for its height) * Widgets.setSizePolicy(policy for width,policy for
        # the height)
        self.entry2.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.entry2.sizeHint = lambda: self.fixed
        # tries to be hintsize but expands and shrinks if resized through window
        self.entry3.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.entry3.sizeHint = lambda: self.expand
        self.window.show()


Test().exec()
