from PyQt5 import QtWidgets,QtCore,QtGui
import random
from typing import NoReturn, Optional,Tuple
import os

class QuickImageView(QtWidgets.QWidget):
    """
    QtWidget with Label and a Frame to display the image quickely.
    For  More Settings refer the Press the Home Button

    TODO: add dropevent to upload the files

    Raises:
        if filename is invalid then refers the default files or previously selected files
        but before that it show critical message.

    Methods:
        refresh(filename: Optional)
    """
    
    def __init__(self,filename=None,parent=None,**kwargs):
        super().__init__(parent)
        self.__mainlayout=QtWidgets.QVBoxLayout()
        self.__mainframe=QtWidgets.QFrame(self)
        self.__DEFAULTMODE=True
        self.__mainlabel=QtWidgets.QLabel(self.__mainframe,text='Not Uploaded Yet...')        
        self.defaultfiles=[
            os.path.join(
                os.path.join(
                    os.path.join(
                        os.path.dirname(__file__),
                        'Resources'),
                        'Images'),
    'rem{}.jpeg'.format(i))
    for i in range(1,7)]
        self.filepath=random.choice(self.defaultfiles)
        self.__IMAGE=QtGui.QPixmap(self.filepath)
        self.__settings=QtCore.QSettings('QtRWidgets','ImageViewer')
        self.__arrange()
        self.__parseImage(filename)

    def __getattr__(self,item):
        if item=='default':return self.__DEFAULTMODE
        elif item=='settings':return self.__parseSettings()

    def __arrange(self):
        self.setLayout(self.__mainlayout)
        self.__mainlayout.addWidget(self.__mainframe)
        self.__mainframe.setLayout(QtWidgets.QVBoxLayout())
        self.__mainframe.layout().addWidget(self.__mainlabel)

    def __parseSettings(self) -> Tuple[str,float]:
        return self.__settings.value('mode',type=str),self.__settings.value('value',type=float)

    def __parseImage(self,filename):
        ''' Internal Parsing of the Image to the Label  using the pixmap'''
        self.mode,self.value=self.__parseSettings()
        try:
            test=QtGui.QPixmap(filename)
            if test.width()==0 or test.height()==0:raise Exception
            self.__IMAGE.swap(test)
            self.filepath=filename
            self.__DEFAULTMODE=False
        except Exception:
            self.__DEFAULTMODE=True
            self.__displayerror('File Related Issue',"Image Can't be Displayed",str("""
ErrorName: Chunchunmaru (69) 
Desc:   Either Image File is not of proper format or the filepath is incorrect.
        For Now: Loading one of the Default Files we have. 
        So don't worry please try next time. ALL THE BEST. and please enjoy our defaults""")).exec()
        self.__adjustImage()        
        self.__mainlabel.setPixmap(self.__IMAGE)
        self.__reload()

    def __reload(self):
        self.__mainlabel.resize(self.__IMAGE.width(),self.__IMAGE.height())
        self.__mainlabel.repaint()
        self.__mainframe.repaint()
        self.repaint()

    def refresh(self,filename:Optional[str]=None) -> NoReturn:
        '''refreshes the current image with the given filename else just normally refreshes the label '''
        if filename is None:filename=self.filepath
        return self.__parseImage(filename)

    def __adjustImage(self) -> None:
        ''' adjusts the size of the image of the label according to the settings'''
        mode,value=self.__parseSettings()
        if mode=='default':pass
        elif mode=='percentage':
            self.__IMAGE.swap(
                self.__IMAGE.scaled(
                    QtCore.QSize(int(self.__IMAGE.width()*(value/100)),int(self.__IMAGE.height()*(value/100))),
                    transformMode=QtCore.Qt.SmoothTransformation
                )
            )
        

    def __displayerror(self,title='Error',msg_to_display="Image can't be loaded. So loading the Default Ones...",details='Please try to select another file'):
        '''returns the messagebox (critical mode)'''
        errorbox=QtWidgets.QMessageBox()
        errorbox.setIcon(QtWidgets.QMessageBox.Critical)
        errorbox.setWindowTitle(title)
        errorbox.setText(msg_to_display)
        errorbox.setDetailedText(details)
        return errorbox


if __name__=='__main__':
    app=QtWidgets.QApplication([])
    window=QuickImageView()
    window.show()
    app.exec()
