import random
from refer import *

test = Test()

test.setHtml(
    """
<p> this is just a <br> random msg </p>
<p>
paragraph of text,
right?
</p>
<br>
<br>
line break

<div>
sample text</div>
"""
)

test.show()

for entity in test.document().rootFrame():
    frame: QtGui.QTextFrame = entity.currentFrame()
    block: QtGui.QTextBlock = entity.currentBlock()

    if frame:
        print("frame ? this wont be possible with tht html", frame)
        continue

    print(block)  # based on above HTML code we have three blocks
    print(block.text())

    block.setVisible(bool(random.randint(0, 1)))  # see this is how we can manipulate a block of text

    # in more scripts we can parse docs and create more blocks

# number of blocks == no of paired tags

sample.exec_()
