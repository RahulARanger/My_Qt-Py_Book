from .quickview import QuickImageView
from .morewindow import More
import os
from PyQt5 import QtWidgets,QtCore,QtGui

class MainImageViewer(QtWidgets.QMainWindow):
    def __init__(self,filepath=None,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.__WINDOWS=[]
        self.settings=QtCore.QSettings('QtRWidgets','ImageViewer')
        self.setWindowTitle("Image Viewer")
        self.__QUICKVIEW=self.settings.value('quickview',type=bool)                
        self.__setMainWindow()
        self.__setMenuBar()
        self.__setToolBar()
        self.__setStatusBar()
        self.__filepath=filepath

    def __getattr__(self,index):
        if index=='mode':return self.__QUICKVIEW
        elif index=='filepath':return self.__filepath

    def __setMainWindow(self):
        self.__MainWindow=QtWidgets.QWidget(self)
        self.__Home=QuickImageView(self.filepath)
        self.__Settings=More(self.__Home.details,self)
        self.__MainWindow.setLayout(QtWidgets.QStackedLayout())
        self.__MainWindow.layout().addWidget(self.__Home) 
        self.__MainWindow.layout().addWidget(self.__Settings)
        self.setStatusTip('Welcome to ImageViewer')
        self.__switchpage()
        self.setCentralWidget(self.__MainWindow)

    def __setMenuBar(self):
        self.__menubar=self.menuBar()
        self.__setMenuActions()

    def __setMenuActions(self):
        self.__help=QtWidgets.QAction("Help",self)
        self.__file=QtWidgets.QMenu("File",self)
        self.__reload=QtWidgets.QAction("Refresh",self)
        self.__addnew=QtWidgets.QAction("New Window",self)
        self.__exit=QtWidgets.QAction("Exit",self)

        self.__addnew.setShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL+QtCore.Qt.Key_N))
        self.__addnew.triggered.connect(self.__createWindow)
        self.__exit.triggered.connect(self.close)
        self.__exit.setShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL+QtCore.Qt.Key_X))
        self.__reload.triggered.connect(self.__refresh)

        self.__menubar.addMenu(self.__file)
        
        self.__file.addAction(self.__addnew)
        self.__file.addAction(self.__reload)
        self.__file.addSeparator()
        self.__file.addAction(self.__exit)
        self.__menubar.addAction(self.__help)

    def __setToolBar(self):
        self.__toolbar=QtWidgets.QToolBar("File")
        self.__setActions()
        ''' customization '''
        self.__toolbar.setMovable(False)
        self.__toolbar.setFloatable(False)
        self.addToolBar(QtCore.Qt.LeftToolBarArea,self.__toolbar)

        ''' adding actions '''
        self.__toolbar.addAction(self.__quick)
        self.__toolbar.addAction(self.__home)
        self.__toolbar.addAction(self.__upload)

    def __setActions(self):
        self.__quickbutton=QtWidgets.QToolButton(text='Home',clicked= lambda x=True: self.__switchpage(0))
        self.__homebutton=QtWidgets.QToolButton(text='Settings',clicked= lambda x=True: self.__switchpage(1))
        self.__home=self.__toolbar.addWidget(self.__homebutton)
        self.__quick=self.__toolbar.addWidget(self.__quickbutton)
        self.__upload=QtWidgets.QAction('Upload',self)
        self.__quickbutton.setCheckable(True)
        self.__homebutton.setCheckable(True)
        self.__quickbutton.setChecked(self.__QUICKVIEW)
        self.__homebutton.setChecked(not self.__QUICKVIEW)
        self.__upload.triggered.connect(self.__uploading)

    

    def __switchpage(self,mode=None):
        if mode is not None:self.__QUICKVIEW=False if mode==1 else True
        if self.mode:
            self.__MainWindow.layout().setCurrentIndex(0)
            if mode is not None:
                self.__homebutton.setChecked(False)
                self.__quickbutton.setChecked(True)
        else:
            self.__MainWindow.layout().setCurrentIndex(1)
            if mode is not None:    
                self.__quickbutton.setChecked(False)
                self.__homebutton.setChecked(True)

    def __uploading(self):
        result=QtWidgets.QFileDialog.getOpenFileName(self,"Open Any Image",
        QtCore.QDir.homePath(),
        "JPG Files (*.jpg) ;; JPEG files (*.jpeg)")
        if result[-1]:
            self.__Home.refresh(result[0])
        return self.__refresh()


    def __refresh(self):
        self.repaint()
        self.adjustSize()
        self.adjustSize()
        self.repaint()

    def __setStatusBar(self):
        pass

    def __createWindow(self):
        self.__WINDOWS.append(MainImageViewer(None))
        self.__WINDOWS[-1].show()

    def closeEvent(self,event):
        # TODO: think of some closing event
        return super().closeEvent(event)

class ImageViewer(QtWidgets.QApplication):
    def __init__(self,filepath=None,*args):
        super().__init__([])
        self.__mainwindow=MainImageViewer(filepath)
        self.__mainwindow.show()
        self.exec()



