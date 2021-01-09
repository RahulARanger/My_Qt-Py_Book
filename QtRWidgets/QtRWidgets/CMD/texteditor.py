from PySide6 import QtCore,QtWidgets,QtGui    
import code,sys

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
        #self.setup()
        self.cursor=self.textCursor()
        self.blocks=[]
        print(self.lineWrapMode())
        

    def customize(self):
        self.setCursorWidth(8)
        self.setUndoRedoEnabled(False)

    ''' Events'''

    def keyPressEvent(self,event):
        if event.key()==QtCore.Qt.Key_Up:pass
        else:super().keyPressEvent(event)

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
        return "print('Hello There)"

    def fakesetup(self):
        self.insertPlainText('Welcome To Python Console \n\n')
    def setup(self):
        self.pipes=(sys.stdin,sys.stdout,sys.stderr)
        sys.stdin,sys.stdout,sys.stderr=self,self,self
        self.compiler=code.InteractiveConsole(locals=locals(),filename='<Console>')
        self.compiler.interact()
        sys.stdin,sys.stdout,sys.stderr=self.pipes
    def flush(self):
        pass

    def clean(self):
        
        self.fakesetup()

    def addlog(self,string):
        pass

    def write(self,string):
        self.insertPlainText(string)
    
    def replacecurrentline(self):
        pass


    def detectcurrentline(self):
        pass
    ''' code related methods ends here '''

if __name__=='__main__':
    a=QtWidgets.QApplication([])
    b=QtWidgets.QWidget()
    c=Editor(b)
    b.show()
    c.show()
    a.exec_()