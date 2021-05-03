from PySide2 import QtWidgets, QtCore


class Test(QtWidgets.QTreeWidget):
    def __init__(self):
        super().__init__()
        self.directory = QtCore.QFileInfo(__file__).dir().entryInfoList()
        self.children = []
        self.setColumnCount(3)
        self.setHeaderLabels(["Name", "size", "Birth Time"])

        self.arrange()

    def arrange(self):
        for _ in self.directory:
            if _.size() == 0:
                continue
            name = _.fileName()
            time = _.birthTime().time()

            hr, min = time.hour(), time.minute()

            size = str(_.size())
            self.addTopLevelItem(QtWidgets.QTreeWidgetItem(self, [name, size, "{}:{}".format(hr, min)]))


checking = QtWidgets.QApplication([])
temp = Test()
temp.show()
checking.exec_()
