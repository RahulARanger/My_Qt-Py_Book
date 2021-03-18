from PyQt5 import QtWidgets,QtCore
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Check This Bug')
        # ! TRY TO DELETE THE PLACEHOLDER TEXT. so dont use this combo(align right + clear button for line edit)
        self.entry=QtWidgets.QLineEdit(self.window,placeholderText='0',clearButtonEnabled=True)
        self.entry.setAlignment(QtCore.Qt.AlignRight)
        self.entry.show()
        self.window.show()
test().exec()