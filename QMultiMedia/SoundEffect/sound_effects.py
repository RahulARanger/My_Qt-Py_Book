# some files .wav (pulse code modulation or wave form files) those requires QtMultiMedia.QSoundEffect
# used for simple/ small audio files

from PyQt5 import QtMultimedia, QtCore, QtWidgets


testing = QtWidgets.QApplication([])
sample = QtWidgets.QWidget()
sample_bt = QtWidgets.QPushButton(sample)
sample_bt.setText("Play")
sample_bt.move(10, 10)
test = QtMultimedia.QSoundEffect()

print(QtCore.QUrl.fromLocalFile("the_hand.wav"))
test.setSource(QtCore.QUrl.fromLocalFile("the_hand.wav"))

sample_bt.clicked.connect(test.play)
sample.show()
testing.exec()
