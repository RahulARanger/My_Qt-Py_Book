from refer import *
from frames import check


class Testing(Test):
    def __init__(self):
        super().__init__()
        for _ in range(3):
            cur = QtGui.QTextCursor(self.document().rootFrame())
            cur.clearSelection()
            print(cur.insertFrame(check()))
            cur.insertText("checking this")

        self.prev = None

    def mouseMoveEvent(self, e) -> None:
        super().mouseMoveEvent(e)

        frame = self.cursorForPosition(e.pos()).currentFrame()
        frame.setFormat(check())  # simple demo


test = Testing()
test.show()

sample.exec_()
