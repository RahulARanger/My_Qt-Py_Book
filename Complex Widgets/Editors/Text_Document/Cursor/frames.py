from refer import *
import random

test = Test()

_ = QtGui.QTextFormat(QtGui.QTextFormat.FrameFormat)


def check():
    __ = QtGui.QTextFrameFormat(
        _
    )

    __.setBackground(
        QtGui.QBrush(
            QtGui.QColor(
                random.choice(["orange", "blue", "green", "yellow"])
            )
        )
    )

    return __


if __name__ == "__main__":
    print("root", test.document().rootFrame())

    for ___ in range(3):
        cur = QtGui.QTextCursor(test.document().rootFrame())

        frame = cur.insertFrame(check())
        print("@", frame, frame.parentFrame())
        cur.insertText("checking this: " + str(___))

        test.setTextCursor(cur)

    for frame in test.document().rootFrame():
        print(frame.currentFrame())

    test.show()
    sample.exec_()
