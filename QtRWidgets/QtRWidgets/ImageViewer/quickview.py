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
        if filepath is invalid then refers the default files or previously selected files
        but before that it show critical message.

    Methods:
        refresh(filepath: Optional)
    """
    
    def __init__(self,filepath=None,parent=None,**kwargs):
        super().__init__(parent)
        self.__mainlayout=QtWidgets.QVBoxLayout()
        self.__mainframe=QtWidgets.QFrame(self)
        # TODO:self.setAcceptDrops(True)
        self.__DEFAULTMODE=True
        self.__mainlabel=QtWidgets.QLabel(self.__mainframe,text='Not Uploaded Yet...')        
        self.defaultfiles=[
            os.path.join(
                os.path.join(
                    os.path.join(
                        os.path.dirname(__file__)
                        ,'Resources')
                    ,'Images')
                    ,_) for _ in os.listdir(
                        os.path.join(
                            os.path.join(
                                os.path.dirname(__file__)
                                ,'Resources')
                            ,'Images')
                        )
        ]
        self.__filepath=random.choice(self.defaultfiles) if filepath is None else filepath
        self.__IMAGE=QtGui.QPixmap(self.__filepath)
        self.__settings=QtCore.QSettings('QtRWidgets','ImageViewer')
        self.__details={
            'filepath':None,
            'extension':None,
            'width':None,
            'Height':None,
            'Colored':None
        }
        self.__arrange()
        self.__parseImage(filepath)

    def __getattr__(self,item):
        if item=='default':return self.__DEFAULTMODE
        elif item=='settings':return self.__parseSettings()
        elif item=='details':return self.__details.copy()
        elif item=='filepath':return self.__filepath
        else: raise AttributeError("{} Attribute doesn't exist in {}".format(item,self.__class__))

    def __arrange(self):
        self.setLayout(self.__mainlayout)
        self.__mainlayout.addWidget(self.__mainframe)
        self.__mainframe.setLayout(QtWidgets.QVBoxLayout())
        self.__mainframe.layout().addWidget(self.__mainlabel)

    def __parseSettings(self) -> Tuple[str,float]:
        return self.__settings.value('mode',type=str),self.__settings.value('value',type=float)

    def __parseImage(self,filepath:str) -> dict:
        print(self.__IMAGE.width(),self.__IMAGE.height())
        ''' Internal Parsing of the Image to the Label  using the pixmap'''
        try:
            test=QtGui.QPixmap(filepath)
            if test.width()==0 or test.height()==0:raise Exception
            self.__IMAGE.swap(test)
            self.__filepath=filepath
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
        self.__note()
        return self.__details.copy()
    
    def __reload(self):
        print(self.__IMAGE.width(),self.__IMAGE.height())
        self.__mainlabel.resize(self.__IMAGE.width(),self.__IMAGE.height())
        self.__mainlabel.repaint()
        self.__mainframe.repaint()
        self.repaint()

    def __note(self):
        self.__details["width"],self.__details["height"]=self.__IMAGE.width(),self.__IMAGE.height()
        self.__details["filepath"],self.__details["extension"]=self.__filepath[:-4],self.__filepath[-3:]
        
    def refresh(self,filepath:Optional[str]=None) -> NoReturn:
        '''refreshes the current image with the given filepath else just normally refreshes the label '''
        if filepath is None:filepath=self.__filepath
        return self.__parseImage(filepath)

    def realrefresh(self):
        self.__adjustImage()
        self.__reload()

    def openDefault(self):
        ''' opens one of the default files '''
        return self.refresh(random.choice(self.defaultfiles))

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
