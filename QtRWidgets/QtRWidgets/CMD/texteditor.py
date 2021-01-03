from PySide6 import QtCore,QtWidgets,QtGui    
import code,sys,threading

# *  right click to paste
# * disabled the context menu
# TODO: prevent accessing the upper lines
# TODO: Set limit to the max lines

class Editor(QtWidgets.QPlainTextEdit):
    def __init__(self,parent):
        super().__init__(parent)
        self.started=True
        self.connected=0
        self.customize()
        self.fakesetup()
        self.cursor=self.textCursor()
        self.installEventFilter(self)
        self.blocks=[]
        print(self.lineWrapMode())
        

    def customize(self):
        self.setCursorWidth(8)
        self.setUndoRedoEnabled(False)

    ''' Events'''

    def cursorForPosition(self, pos):
        print(pos)
        return super().cursorForPosition(pos)

    def contextMenuEvent(self, event):
        # ? disables the context menu
        return True
    ''' Events Closed'''
    def test(self,*args):
        print('$',args)
        return True

    '''Code related methods'''
    def readline(self):
        pass

    def fakesetup(self):
        self.insertPlainText('Welcome To Python Console \n\n')
    def setup(self):
        self.compiler=code.InteractiveConsole(locals=locals(),filename='<Console>')
        self.compiler.interact()
        
    def flush(self):
        pass

    def clean(self):
        
        self.fakesetup()

    def addlog(self,string):
        pass

    def write(self,string):
        pass
    
    def replacecurrentline(self):
        pass


    def detectcurrentline(self):
        pass
    ''' code related methods ends here '''

    def eventFilter(self,object_,event):
        if event.type()==QtCore.QEvent.KeyPress:self.checkkeyevents(event)
        elif event.type()==QtCore.QEvent.MouseButtonPress:self.checkmouseevents(event)
        return super().eventFilter(object_,event) 
    
    def checkkeyevents(self,event):
        if event.key()==QtGui.Qt.Key_Up:
            self.cursor.movePosition(QtGui.QTextCursor.Down,QtGui.QTextCursor.MoveAnchor)
        if event.key()==QtGui.Qt.Key_Return:
            print(self.cursor.position())
    def checkmouseevents(self,event):
        if event.button()==QtGui.Qt.RightButton:self.paste()
        

if __name__=='__main__':
    a=QtWidgets.QApplication([])
    b=QtWidgets.QWidget()
    c=Editor(b)
    b.show()
    c.show()
    a.exec_()