from PySide2 import QtWidgets, QtCore


class Sample(QtWidgets.QTextBrowser):
    Clicks = QtCore.Signal([], [str])  # Optionally Str, Empty

    def __init__(self):
        super().__init__()
        self.count = 0

        self.Clicks.connect(self.show_count)
        self.Clicks[str].connect(self.show_msg)  # must be seperately connected

    def show_msg(self, txt):
        self.insertPlainText(txt)

    def show_count(self):
        self.count += 1
        self.Clicks[str].emit(f"Clicked {self.count}\n")

    def mousePressEvent(self, ev) -> None:
        self.Clicks[str].emit("Poked\n")
        return super().mousePressEvent(ev)


test = QtWidgets.QApplication([])

sample = Sample()
sample.show()

_ = QtWidgets.QPushButton()
_.setText("Click")

_.clicked.connect(sample.Clicks)  # signal - signal connection as long as connected ones accepts none or it matches
_.show()

test.exec_()
