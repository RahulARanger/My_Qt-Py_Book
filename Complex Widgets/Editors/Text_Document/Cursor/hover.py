from refer import *

test = Test()

cur = test.textCursor()
_ = QtGui.QTextCharFormat(), QtGui.QTextCharFormat()
_[0].setBackground(QtGui.QBrush(QtGui.QColor("orange")))
_[1].setBackground(QtGui.QBrush(QtGui.QColor("blue")))

cur.insertText("hello there, ", _[0])
cur.insertText("checking again", _[1])
test.setTextCursor(cur)


test.show()

for block in test.document().rootFrame():
    print(block.currentBlock())

    for frag in block.currentBlock():
        print(frag.fragment().text(), frag.fragment().charFormatIndex())

cur = test.textCursor()
cur.setCharFormat(_[1])
test.setTextCursor(cur)

sample.exec_()
