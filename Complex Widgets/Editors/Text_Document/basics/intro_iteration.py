from refer import *

demo = Test()
demo.setText(
    "checking this"
)

doc = demo.document()  # extracting document from editor widgets
frame = doc.rootFrame()
print("root frame: ", frame)  # root frame

# note: this iterates over
for child in frame:
    print("iterator", child)
    child: QtGui.QTextFrame.iterator = child

    if child.currentFrame():
        print("this is a frame", child.currentFrame())
    else:
        print("this is a block", child.currentBlock())

"""
above:
iteration

- root frame  # 1
    - child block  # 2

another example:

- root frame # 1
    - child block  # 2
    - child frame  # 3
            - child block  # 4
"""

demo.show()
sample.exec_()
