from PyQt5 import QtCore, QtWidgets
# TODO: This is the second method for creating the messsagebox (this is the more customizable than the first one)
# * Docs: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMessageBox.html#id2
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='QMessageBox with the constructor Method')
        self.window=QtWidgets.QWidget(windowTitle='QMessageBox')
        self.layout=QtWidgets.QHBoxLayout()
        self.window.setLayout(self.layout)
        self.createMessageBoxes()
        store=[None for i in '....']
        f1=lambda x=True:print(self.info.exec_())
        f2=lambda x=True:print(self.que.exec_()) # prints the code for the predefined buttons in the messagebox 
        f3=lambda x=True:print(self.war.exec_()) # they can also be checked using QtWidgets.QMessageBox.type_of_button
        f4=lambda x=True:print(self.cri.exec_()) # example QtWidgets.QMessageBox.Cancel
        self.information=QtWidgets.QPushButton(self.window,text='Information',clicked=f1)
        self.question=QtWidgets.QPushButton(self.window,text='Question',clicked=f2)
        self.warning=QtWidgets.QPushButton(self.window,text='Warning',clicked=f3)
        self.critical=QtWidgets.QPushButton(self.window,text='Critical',clicked=f4)
        self.layout.addWidget(self.information)
        self.layout.addWidget(self.question)
        self.layout.addWidget(self.warning)
        self.layout.addWidget(self.critical)
        self.window.show()
    def createMessageBoxes(self):
        self.info,self.war,self.cri,self.que=[QtWidgets.QMessageBox(self.window) for i in '....']
        self.info.setText('This is a Information Message Box')
        self.war.setText('This is the Warning Message Box')
        self.cri.setText('This is the Critical Message Box')
        self.que.setText('This is the Question Message Box')
        
        self.info.setWindowTitle('Information')
        self.war.setWindowTitle('Warning')
        self.cri.setWindowTitle('Critical')
        self.que.setWindowTitle('Question')

        self.info.setIcon(QtWidgets.QMessageBox.Information)
        self.war.setIcon(QtWidgets.QMessageBox.Warning)
        self.que.setIcon(QtWidgets.QMessageBox.Question) # This is will set icon and as well as the warning sound
        self.cri.setIcon(QtWidgets.QMessageBox.Critical) # ? also included with the critical sound

        self.info.setDetailedText('Hello There this is the Information box')
        self.war.setDetailedText('Hello There this is the warning Box')
        self.que.setDetailedText('Hello There this is the question Box')
        self.cri.setDetailedText('Hello There this is the Critical Message Box')
        self.cri.setInformativeText('This is more informative text')    
            
        self.que.setWindowModality(QtCore.Qt.WindowModal)
        self.info.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Help) # we use pipes to add more than one buttons
        self.war.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Help | QtWidgets.QMessageBox.RestoreDefaults)
        # ? This is how the standard Buttons are added to the Message Box
test().exec()
