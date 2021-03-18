from PyQt5 import QtWidgets
import sys
class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.window=QtWidgets.QWidget(windowTitle='Rich Text Label')
        # ? Rich text is like the HTML Syntax
        self.label=QtWidgets.QLabel(self.window,text='<a href="www.google.com" > Link </a>',indent=100,margin=50,toolTip='Google Link')
        self.label.show()
        self.window.show()
        
a=Test()
a.exec()