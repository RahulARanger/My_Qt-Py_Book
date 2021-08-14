from PySide2 import QtWidgets, QtCore


# Acc. to my observation, Signal will emit values from any thread to a main thread or a thread where QApplication is
# running

class Sample(QtWidgets.QTextBrowser):
    def __init__(self):
        super().__init__()
        self.setOpenLinks(False)
        self.anchorClicked.connect(self.check)  # this are some in build signals
        # it releases values of the same type and it's type matters

        self.setHtml(
            """
<a href="https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QTextBrowser.html"> check </a>
"""
        )

    # here url must be QUrl or it's derivatives
    def check(self, url: QtCore.QUrl):
        print(url, str(url.url()))


test = QtWidgets.QApplication([])

sample = Sample()
sample.show()

test.exec_()
