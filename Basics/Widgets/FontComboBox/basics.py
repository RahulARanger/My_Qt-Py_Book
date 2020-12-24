from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Font Combo Box')
        self.window.show()
        self.fcox=QtWidgets.QFontComboBox(self.window,toolTip='Font Combo Box',
        
        )
        self.fcox.setFontFilters(QtWidgets.QFontComboBox.ScalableFonts)
        self.fcox.show()
        print(self.fcox.currentFont())
Test().exec()
# NOTE: refer this https://doc.qt.io/qtforpython/PySide6/QtWidgets/QFontComboBox.html#qfontcombobox