from PySide6 import QtUiTools,QtCore,QtWidgets,QtGui    
from .texteditor import Editor
editorclass,editorwidgetclass=QtUiTools.loadUiType('QtRWidgets\\CMD\\editor.ui')
class CMDEditor(editorwidgetclass,editorclass):
    def __init__(self,parent=None):
        super().__init__(parent)
        
        self.setupUi(self)
        #!  MODIFICATION BEGINS FROM HERE
        self.EDITOR=Editor(self)
        self.arrange()
        self.setnames()
        self.setevents()        
    def arrange(self):
        self.tab1layout.addWidget(self.EDITOR)
    def setnames(self):
        pass
    def setevents(self):
        pass
    
# TODO: use pathfinder()
if __name__=='__main__':
    app=QtWidgets.QApplication([])
    store=CMDEditor()
    app.exec_()