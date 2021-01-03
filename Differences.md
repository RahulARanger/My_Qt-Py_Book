# Intro

Pyside6 and PyQt5 is very similar and they don't differ much.

But they posses some significant differences. and it is important between anyone out of them. Since the size of each module >100mb.


# Pyside6 vs PyQt5

* They also differ in method for loading the UI file using the module (refer: [PyQt5](https://github.com/RahulARanger/My_PyQt5_Book/blob/master/Calculator/try2.py) and [PySide6](https://github.com/RahulARanger/My_PyQt5_Book/blob/master/Calculator/try2.py))

*  for executing QApplication `exec_()` only works for the `PySide.QtWidgets.QApplication()` but for the PyQt5 it is `exec()`.

* For Constructing own signals we use `PySide6.QtCore.Signal()` but in PyQt5 we use `PyQt5.QtCore.pyqtSignal()`  and for slot we use `PySide6.QtCore.Slot()` but for PyQt5 we use `PyQt5.QtCore.pyqtSlot()`

* Key Bindings are listed in `QtCore.Qt` for PyQt5 but for PySide it's `QtGui.Qt`


