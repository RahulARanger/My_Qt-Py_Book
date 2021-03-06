from PyQt5 import QtWidgets, QtCore, QtGui
import os
import csv


class SimpleCell(QtGui.QStandardItem):
    def __init__(self, data):
        represent = str(data)
        super().__init__(represent)
        self.store = data
        self.setText(represent)
        self.__modifications()

    def __modifications(self):
        self.setEditable(False)
        self.setToolTip("{}".format(self.text()))


class SimpleModel(QtGui.QStandardItemModel):
    def __init__(self, data=None, headers=None, icon=None):
        super().__init__()

        if data is None or headers is None:
            pass
        else:
            self.__check_contents(tuple(data), tuple(headers))

    def __getattr__(self, item):
        if item == 'width':
            return self.columnCount()
        elif item == 'height':
            return self.rowCount()
        else:
            return super().__getattr__(item)

    def check_contents(self, data: tuple, headers: tuple):
        temp_width = len(headers)
        temp_height = 0
        for row in range(len(data)):
            temp_height += 1
            if len(data[row]) != temp_width:
                return False, temp_width, len(data[row])
        return True, temp_width, temp_height

    def __check_contents(self, data: tuple, headers: tuple):
        result = self.check_contents(data, headers)
        if not result[0]:
            raise IndexError("Incorrect Data Representation")
        self.__width, self.__height = result[1], result[2]
        self.__set_contents(data, headers)

    def __set_contents(self, data, headers):
        self.setHorizontalHeaderLabels(headers)
        self.setColumnCount(self.__width)
        for row in range(self.__height):
            cells = []
            for column in range(self.__width):
                cells.append(SimpleCell(data[row][column]))
            self.appendRow(cells)

    def replace(self, data, headers):
        return self.__check_contents(tuple(data), tuple(headers))


class SimpleView(QtWidgets.QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)


class EmbeddedStaticTabularView(SimpleView):
    def __init__(self, data, headers, parent=None, vheaders: bool = True):
        super().__init__(parent)
        self.verticalHeader().setVisible(vheaders)
        self.__model = SimpleModel(data, headers)
        self.setModel(self.__model)

    def model(self):
        return self.__model

    def replace(self, data, headers):
        return self.__model.replace(data, headers)

    def csv_export(self):
        pass

    def export(self):
        result, file_name = QtWidgets.QFileDialog.getSaveFileName(self, "Save as", QtCore.QDir.homePath(),
                                                                  "CSV File (*.csv)")
        if result:
            print(file_name)


class StaticTabularView(QtWidgets.QMainWindow):
    def __init__(self, data=None, headers=None):
        super().__init__()
        self.__embedded = EmbeddedStaticTabularView(data, headers, self)
        self.__set_toolbar()
        self.__set_statusbar()
        self.__arrange()

    def __set_statusbar(self):
        self.__status_bar = self.statusBar()
        self.setStatusBar(self.__status_bar)
        self.__status_bar.setStatusTip("Welcome to Static Table View... :D")
        self.__status_bar.setSizeGripEnabled(False)

    def __set_toolbar(self):
        self.__toolbar = QtWidgets.QToolBar(self)
        self.__toolbar.setMovable(False)
        self.__toolbar.setFloatable(False)

        self.__open = QtWidgets.QToolButton(self, toolTip='Open')
        self.__open.setIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), "../Resources/open.svg")))
        self.__saveas = QtWidgets.QToolButton(self, clicked=self.export, toolTip='Save as')
        self.__saveas.setIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), "../Resources/save.svg")))
        self.__toolbar.addWidget(self.__open)
        self.__toolbar.addWidget(self.__saveas)
        self.__toolbar.setAllowedAreas(QtCore.Qt.LeftToolBarArea)
        self.addToolBar(QtCore.Qt.LeftToolBarArea, self.__toolbar)

    @QtCore.pyqtSlot()
    def export(self):
        self.__status_bar.showMessage("Exporting...")
        self.__embedded.export()
        self.__status_bar.clearMessage()

    def __arrange(self):
        self.setCentralWidget(self.__embedded)

    def start(self):
        return self.show()


if __name__ == '__main__':
    from itertools import product

    app = QtWidgets.QApplication([])
    a = StaticTabularView(data=product([True, False], repeat=2), headers=("a", "b"))
    a.start()
    app.exec()
