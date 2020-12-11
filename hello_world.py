from PyQt5 import QtWidgets
# ! note that PyQt5 follows camel case (first letter of func are small and latter are caps but the all first letter of the words in class must be in caps)
class HelloWorld(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([]) # ? we can pass the command line arguments 
        self.window=QtWidgets.QWidget(windowTitle='Hello World')
        # ? can also be replaced by
        '''
        self.window=QtWidgets.QtWidget()
        self.window.setWindowTitle('Hello World')
        '''
        print('The Title for the QWidget is : {}'.format(self.window.windowTitle()))
        self.window.show()
store=HelloWorld()
store.exec()

# * Summary 
# TODO: for creating the basic Qt Window
# * create the QtWidgets.QApplication before creating a QWidget 
# * create the QWidgets.QWidget() which is responsible for the window
# * use show() for showing the current window
# ! QtWidgets.QtApplications.exec() creates the loop (so must be at end of the program)