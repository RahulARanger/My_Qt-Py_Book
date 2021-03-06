from PyQt5 import QtWidgets, QtCore, QtGui
import csv
import os


class CSVCell(QtGui.QStandardItem):
    def __init__(self, data):
        self.__store = data
        represent = str(data)
        super().__init__(represent)
        self.setText(represent)
        self.__setup()

    def __setup(self):
        pass

    def get_data(self):
        return self.__store


class CSVModel(QtGui.QStandardItemModel):
    def __init__(self, editable):
        super().__init__()
        self.__editable=editable
        self.edit_state(editable)


    def __getattr__(self, item):
        if item == 'row':
            return self.rowCount()
        elif item == 'column':
            return self.columnCount()


    def edit_state(self, value):
        self.__edit_cells(value)
        self.__edit_headers(value)
        self.__editable = value

    def __edit_cells(self, value):

        for row in range(self.row):
            for column in range(self.column):
                self.item(row, column).setEditable(value)

    def __edit_headers(self, value):
        for column in range(self.column):
            self.horizontalHeaderItem(column).setEditable(value)

    def get_data(self, row, column):
        return self.item(row, column).get_data()

    def replace(self, file_path:str):
        self.clear()
        with open(file_path, "r") as pointer:
            csv_pointer = csv.reader(pointer)
            self.setHorizontalHeaderLabels(next(csv_pointer))
            for row in csv_pointer:
                self.__addRow(row)
            self.setColumnCount(self.column)
            self.setRowCount(self.row)

    def __addRow(self, row):
        return self.appendRow([CSVCell(cell) for cell in row])

    @QtCore.pyqtSlot()
    def clearData(self):
        for row in range(self.row):
            self.takeRow(0)

    @QtCore.pyqtSlot(int)
    def addEmptyRow(self, index):
        self.insertRow(index, [CSVCell("") for cell in range(self.column)])

    @QtCore.pyqtSlot(int)
    def removeRow(self, index):
        return super().removeRow(index, self)

    def isEditable(self):
        return self.__editable

    @QtCore.pyqtSlot(int)
    def removeColumn(self, column: int) -> bool:
        return super().removeColumn(column, self)

    def save_file(self, file_path:str):
        with open(file_path, "w", newline ='') as pointer:
            csv_pointer = csv.writer(pointer)
            csv_pointer.writerow(self.fetch_headers())
            print(self.fetch_data())
            csv_pointer.writerows(self.fetch_data())

    def fetch_headers(self):
        return [self.horizontalHeaderItem(column).text() for column in range(self.column)]

    def fetch_data(self):
        container = []
        print(self.row, self.column)
        for row in range(self.row):
            container.append(tuple([self.item(row, column).text() for column in range(self.column)]))
        return tuple(container)
    
    def fetch_actual_data(self):
        container = []
        for row in range(self.row):
            container.append(tuple([self.item(row, column).get_data() for column in range(self.column)]))
        return tuple(container)
        


class CSVView(QtWidgets.QTableView):
    open_file_signal = QtCore.pyqtSignal(str)
    save_as_file_signal = QtCore.pyqtSignal()
    def __init__(self, model, parent = None):
        super().__init__(parent)
        self.setModel(model)
        self.save_as_file_signal.connect(self.saveas)
        try:
            self.open_file_signal.connect(parent.replace)
        except:
            print("There Seem to be no replace() method for the model. which can replace the entire table")


    @QtCore.pyqtSlot()
    def saveas(self):
        ask = QtWidgets.QFileDialog.getSaveFileName(self, "Save as", QtCore.QDir.homePath(), "CSV Files (*.csv)")
        if ask[0] != "":
            return self.model().save_file(ask[0])

    @QtCore.pyqtSlot()
    def save(self):
        print("saving")
        return self.model().save_file(self.parent().file)

    @QtCore.pyqtSlot()
    def open_file(self):
        result = QtWidgets.QFileDialog.getOpenFileName(self, "Open a CSV file", QtCore.QDir.homePath(), "CSV Files (*.csv)")
        if result[0] != '':
            self.open_file_signal.emit(result[0])


    @QtCore.pyqtSlot()
    def clear_data(self):
        confirmation = QtWidgets.QMessageBox.warning(self, "Are You Sure ?",
                                                     "Do You want to erase all the contents of the table?",
                                                     QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        if confirmation == QtWidgets.QMessageBox.Ok:
            self.model().clearData()





class CSVEditor(QtWidgets.QMainWindow):
    def __init__(self, file=None, editable=True):
        super().__init__()
        self.__current_file = None
        self.__model = CSVModel(editable)
        self.__view = CSVView(self.__model, self)
        self.__viewicon, self.__editicon = QtGui.QIcon(self.__open_Resouces("preview")), QtGui.QIcon(self.__open_Resouces("edit"))
        self.__set_toolbar()
        # self.__set_statusbar()
        self.__final_setup()
        if file is not None:
            self.replace(file)
        else:
            self.__open_file.clicked.emit(False)

    def __getattr__(self, item):
        if item == 'file':
            return self.__current_file
        else:
            return self.__model.__getattr__(item)

    def check(self, file: str):
        if not os.path.exists(file):
            QtWidgets.QMessageBox.warning(self, "File Not Error", "{} file doesnt exist!!!. Please Check".format(file))
            return False
        if file[-3] + file[-2] + file[-1] != 'csv':
            QtWidgets.QMessageBox.warning(self, "File Type Error", "{} file is not a CSV file.".format(file))
            return False
        return True

    @QtCore.pyqtSlot(str)
    def replace(self, file):
        print("replacing...")
        if not self.check(file):
            return False
        print("checked...")
        self.__model.replace(file)
        self.__current_file = file

    def __open_Resouces(self, filename):
        temp_path = os.path.join(
            os.path.join(
                os.path.dirname(
                    os.path.dirname(__file__)
                ), "Resources"
            ), filename
        )
        return os.path.relpath(temp_path, __file__) if os.path.exists(os.path.relpath(temp_path, __file__)) else temp_path

    def __final_setup(self):
        self.setCentralWidget(self.__view)

    def __set_toolbar(self):
        self.__top_toolbar = QtWidgets.QToolBar(self)
        self.__top_toolbar.setMovable(False)
        self.__top_toolbar.setFloatable(False)

        self.__left_toolbar = QtWidgets.QToolBar(self)
        self.__left_toolbar.setMovable(False)
        self.__left_toolbar.setFloatable(False)

        self.__open_file = QtWidgets.QToolButton(self)
        self.__open_file.setToolTip("Open")
        self.__open_file.setIcon(QtGui.QIcon(self.__open_Resouces("open.svg")))
        self.__open_file.clicked.connect(self.__view.open_file)
        self.__top_toolbar.addWidget(self.__open_file)

        self.__save = QtWidgets.QToolButton(self)
        self.__save.setIcon(QtGui.QIcon(self.__open_Resouces("save.svg")))
        self.__save.clicked.connect(self.__view.save)
        self.__top_toolbar.addWidget(self.__save)

        self.__saveas = QtWidgets.QToolButton(self)
        self.__saveas.clicked.connect(self.__view.save_as_file_signal)
        self.__saveas.setIcon(QtGui.QIcon(self.__open_Resouces("saveas.svg")))
        self.__top_toolbar.addWidget(self.__saveas)

        self.__cell_edit = QtWidgets.QToolButton(self)
        self.__cell_edit.clicked.connect(self.__toggle_edit)
        self.__toggle_edit()
        self.__top_toolbar.addWidget(self.__cell_edit)

        self.__setupTools()

        self.addToolBar(QtCore.Qt.TopToolBarArea, self.__top_toolbar)
        self.addToolBar(QtCore.Qt.LeftToolBarArea, self.__left_toolbar)

    def __setupTools(self):
        # self.__add = QtWidgets.QToolButton(self)
        # self.__add.setIcon(self.__open_Resouces("add.svg"))
        # self.__left_toolbar.addWidget(self.__add)

        self.__delete = QtWidgets.QToolButton(self)
        self.__delete.clicked.connect(self.__view.clear_data)
        self.__delete.setIcon(QtGui.QIcon(self.__open_Resouces("delete.svg")))

        # self.__sortModel = QtWidgets.QToolButton(self)
        # self.__sortModel.setIcon(self.__open_Resouces("sort.svg"))


        self.__left_toolbar.addWidget(self.__delete)



    @QtCore.pyqtSlot(bool)
    def __toggle_edit(self, manual=True):
        if not manual:
            self.__model.edit_state(not self.__model.isEditable())
        self.__cell_edit.setIcon(self.__editicon if self.__model.isEditable() else self.__viewicon)


    def start(self):
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    a = CSVEditor(os.path.join(os.path.dirname(__file__), "example.csv"))
    a.start()
    app.exec()
