from PyQt5 import QtWidgets,QtCore,QtGui
# * Refer for layout structure of the QMainWindow https://github.com/RahulARanger/My_PyQt5_Book/blob/master/Main_Window/mainwindowlayout.png
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='MainWindow')
        self.labl=QtWidgets.QLabel(self.window,text='Hello There')
        self.mainwindow=QtWidgets.QMainWindow()
        self.mainwindow.setCentralWidget(self.window) # this is the way to set the central widget
        self.mainwindow.show()
test().exec()