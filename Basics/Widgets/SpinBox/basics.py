from PyQt5 import QtWidgets
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Spinbox')
        self.sbox=QtWidgets.QSpinBox(self.window,toolTip='SpinBox',
        value=6,
        prefix='Hello',wrapping=True, # wrapping asks whether to rotate after reaching either ends
        minimum=0,maximum=1000, # sets the maximum and minimum value for the spin box (setMaximum() and setMinimum() are their methods)
        singleStep=3,# single step defines the step value for the up and down arrow button
        suffix='There') # suffix and prefix are the text that appear after and before of the value (setPrefix() and setSuffix() are some explicit methods)
        self.sbox.show()
        self.window.show()
test().exec()