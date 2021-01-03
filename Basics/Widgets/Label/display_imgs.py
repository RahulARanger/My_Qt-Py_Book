from PyQt5 import QtWidgets,QtCore,QtGui
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Display Images')
        self.select=QtWidgets.QPushButton(self.window,text='Select Image',toolTip='Select Any Image',clicked=self.openImage)
        self.layout=QtWidgets.QVBoxLayout()
        self.window.setLayout(self.layout)
        self.layout.addWidget(self.select)
        self.box=QtWidgets.QGroupBox(self.window,title='Image:',toolTip='Selected Image')
        self.layout.addWidget(self.box)
        
        self.display=QtWidgets.QLabel(self.box,text='Select Any Image')
        self.display.move(100,100) # places at the x and y coordinates
        self.window.show()
    def openImage(self):
        result=QtWidgets.QFileDialog.getOpenFileName(self.window,
        'Select any File',
        QtCore.QDir.homePath()
        #options=(QtWidgets.QFileDialog.DontUseNativeDialog )  Same for the OS but primitive in terms of the design
        )
        if not result[-1]:return None
        self.image=QtGui.QPixmap(result[0])
        self.display.setPixmap(self.image)
        self.display.repaint() # ? for refreshing the label 
        self.display.resize(self.image.width(),self.image.height()) # ? for resizing the label
test().exec()