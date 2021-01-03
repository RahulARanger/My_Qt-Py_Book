from PyQt5 import QtWidgets
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Rich text for the Labels')
        self.html='''
        <h1> Fruits </h1>
        <ul>
        <li> Orange </li>
        <li> Apple </li>
        <li> Banana </li>
        </ul>
        '''
        self.lb=QtWidgets.QLabel(self.window,text=self.html)
        self.lb.move(100,100)
        self.window.show()
test().exec()