from refer import *

test = Test()
test.insertPlainText("This are some random words. ")


def _():
    cur = test.textCursor()  # it's a local copy of original
    print(cur.movePosition(QtGui.QTextCursor.Start, QtGui.QTextCursor.MoveAnchor))
    test.setTextCursor(cur)  # set it to commit the changes


move = QtWidgets.QPushButton(test)
move.setText("begin")
move.clicked.connect(_)
move.move(100, 100)

test.show()

sample.exec_()
