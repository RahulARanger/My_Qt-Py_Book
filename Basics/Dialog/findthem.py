from PyQt5 import QtWidgets,QtCore

class FindThem(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super().__init__()
        self.arrange()
    def arrange(self):
        self.setSizeGripEnabled(False)
        self.setWindowModality(QtCore.Qt.NonModal)

if __name__=='__main__':
    app=QtWidgets.QApplication([])
    c=QtWidgets.QWidget()
    c.setMinimumSize(QtCore.QSize(600,600))
    d=QtWidgets.QLineEdit(c)
    d.show()
    c.show()
    b=FindThem(c)
    b.show()
    app.exec()