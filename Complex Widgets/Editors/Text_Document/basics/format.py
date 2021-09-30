from refer import *

normal = QtGui.QTextCharFormat()
normal.setBackground(QtGui.QBrush(QtGui.QColor("yellow")))
hover = QtGui.QTextCharFormat()
hover.setBackground(QtGui.QBrush(QtGui.QColor("orange")))

test = Test()

cur = test.textCursor()
cur.setBlockCharFormat(normal)

block = cur.block()

cur.insertText("checking this", cur.blockCharFormat())
block.setRevision(False)

test.setTextCursor(cur)
print(test.pieceTable)
test.show()
cur = test.textCursor()
for _ in cur.block():
    _: QtGui.QTextFragment = _.fragment()
    print(_.charFormat(), _.charFormat())


sample.exec_()
