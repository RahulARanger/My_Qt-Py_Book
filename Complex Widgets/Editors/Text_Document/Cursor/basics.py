from refer import *

test = Test()

cur: QtGui.QTextCursor = test.textCursor()

for _ in test.document().rootFrame():
    block: QtGui.QTextBlock = _.currentBlock()
    print(block)
print(69 * "=")  # for every iteration object changes (since it changes) (so text blocks are created while iterating)

cur.insertText("testing this")  # interacts with the last active text block (cursor position)
cur.insertText("testing this")  # same as above

for _ in test.document().rootFrame():
    block: QtGui.QTextBlock = _.currentBlock()
    print(block)
print(69 * "=")


text_format = QtGui.QTextBlockFormat()
text_format.setHeadingLevel(1)

char_format = QtGui.QTextCharFormat(text_format)
char_format.setForeground(QtGui.QBrush(QtGui.QColor("orange")))
char_format.setBackground(QtGui.QBrush(QtGui.QColor("black")))

cur.insertBlock(text_format, char_format)  # inserts a block and moves the cursor to tht block
cur.insertText("Testing this again")  # inserts text to the block that the cursor is in

test.show()
sample.exec_()
