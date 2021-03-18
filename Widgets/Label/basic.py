from PyQt5 import QtWidgets
import sys
a=QtWidgets.QApplication(sys.argv)
class Test(QtWidgets.QWidget):
    def __init__(self):
        super().__init__(windowTitle='window with basic Label')
        self.label=QtWidgets.QLabel(self,text='Hello There!',margin=10) 
        self.setMinimumHeight(300)
        self.setMinimumWidth(300)
        # ! This below ones becomes a top level
        # TODO: self.label=QtWidgets.QLabel(text='Hello There!')
        # TODO: for extracting label details
        self.extractData()
        # TODO: for making some changes later
        self.modify()
        self.label.show()
        self.show()
        text='this is a long ass paragraph which needs some wod wapping else it will be messed up'
        wrapthis=QtWidgets.QLabel(self,text=text,wordWrap=True,margin=100)
        wrapthis.show()
    def modify(self):
        self.label.setText('Hello There!!!')
        self.label.setMargin(20)
    def extractData(self):
        print(self.label.text()) # ? text inside the label
b=Test()
a.exec()