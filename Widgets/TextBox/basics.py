from PyQt5 import QtWidgets
class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='QTextEdit')
        self.tbox=QtWidgets.QTextEdit(self.window,toolTip='QTextEdit',
        placeholderText='Enter the text',
        acceptRichText=True,
        html='<b>Check This </b>',
        readOnly=False, # default is False
        )
        self.tbox.show()
        self.window.show()
Test().exec()