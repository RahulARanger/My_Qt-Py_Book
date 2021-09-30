from refer import *
import random

_ = QtGui.QTextCharFormat(), QtGui.QTextCharFormat()
_[0].setBackground(QtGui.QBrush(QtGui.QColor("orange")))
_[1].setBackground(QtGui.QBrush(QtGui.QColor("yellow")))


class Test2(Test):
    def __init__(self):
        super().__init__()

    def enterEvent(self, event):
        super().enterEvent(event)

        sur = self.textCursor()
        sur.clearSelection()

        sur.select(QtGui.QTextCursor.LineUnderCursor)
        sur.setCharFormat(_[random.randint(0, 1)])

        sur.clearSelection()

        self.setTextCursor(sur)
        self.repaint()


print([__.background() for __ in _])

___ = Test2()
___.show()

h = ___.textCursor()
h.insertText("checking this, ", _[0])
h.insertText("fragment of text", _[0])
h.insertText("\nanother fragment of text", _[1])

# for block in ___.document().rootFrame():
#     print(block.currentBlock())
#
#     for frag in block.currentBlock():
#         print(frag.fragment().text(), frag.fragment().charFormatIndex())


sample.exec_()
