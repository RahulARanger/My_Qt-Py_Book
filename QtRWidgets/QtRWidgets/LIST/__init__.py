from PyQt5 import QtGui, QtWidgets, QtCore
from typing import Union, Sequence, Any, NoReturn
import os
import json

__all__ = [
    "CellModel",
    "DisplayModel",
    "DisplayView",
    "ListView"
]


# According to the Model-View Programming

class CellModel(QtGui.QStandardItem):
    def __init__(self, item: Any, index: bool = False):
        super().__init__()
        self.setText(str(item))
        self.secert = None if index else item
        self.__state = index
        self.__setup()

    def __setup(self):
        self.setEditable(False)
        self.setToolTip("Index" if self.__state else "Data")
        self.setStatusTip("{}: {}".format("Index" if self.__state else "Data", self.text()))

    def manipulate(self, data: Any) -> None:
        self.secert = None if self.__state else data
        self.setText(str(data))

    def reload(self) -> None:
        return self.setText(str(self.secert) if not self.__state else self.text())

    @QtCore.pyqtSlot()
    def print_data(self):
        return print(self.text())


class DisplayModel(QtGui.QStandardItemModel):
    # cant modify this
    """
     ! Model for the ListView.

     * Contains 2 Columns (index, value)
     * N - Number of the rows
    """

    def __init__(self, container: Sequence[Any] = []):
        super().__init__()
        self.__lastindex = 0
        self.ds = 'List'
        self.__indexerror = QtWidgets.QMessageBox()
        self.__setMessagebox()
        self.__settingDimensions()
        self.replace(container)

    def __setMessagebox(self) -> NoReturn:
        self.__indexerror.setWindowTitle("IndexError")
        self.__indexerror.setIcon(QtWidgets.QMessageBox.Critical)
        self.__indexerror.setStandardButtons(QtWidgets.QMessageBox.Ok)

    def __settingDimensions(self) -> NoReturn:
        self.setColumnCount(2)  # Index, Data
        self.setHorizontalHeaderLabels(["Index", "Data"])

    def __getattr__(self, value: str):
        if value == 'length':
            return self.rowCount()
        elif value == 'tuple':
            return self.toTuple()
        else:
            return None

    def __len__(self) -> int:
        return self.length

    def __setitem__(self, item: int, value: Any, index: bool = False):
        _ = self.__getactualitem(item, rly=index)
        if _ != "":
            return _.manipulate(value)
        return _

    def __getactualitem(self, index: int, rly: bool = False) -> Any:
        if index < 0:
            index = self.length + index
        store = self.item(index, 1 if not rly else 0)
        if store is None:
            self.__indexerror.setText("IndexError: Index: {} is out of the {}'s range".format(self.ds, index))
            self.__indexerror.exec()
            return ""
        return store

    def __getitem__(self, index: int):
        _ = self.__getactualitem(index)
        if _ != "":
            return _.secert
        return _

    def __iter__(self) -> "ListView":
        self.count = 0
        return self

    def __next__(self):
        if self.count < self.length:
            store = self[self.count]
            self.count += 1
            return store
        else:
            raise StopIteration

    def __delitem__(self, key: int) -> NoReturn:
        """ List Related"""
        if len(self.takeRow(key)) == 0:
            self.__indexerror.setText("IndexError: Index {} is out of {}'s range".format(key, self.ds))
            self.__indexerror.exec()
            return ""
        self.refresh()

    def insert(self, pos, item):
        """ List Related"""
        self.insertRow(pos, [CellModel(pos, index=True), CellModel(item)])
        self.refresh()

    def append(self, item) -> NoReturn:
        self.appendRow([CellModel(self.__lastindex, index=True), CellModel(item)])
        self.__lastindex += 1

    def pop(self) -> Any:
        if self.length == 0:
            self.__indexerror.setText("IndexError: pop() on the Empty {}()".format(self.ds))
            self.__indexerror.exec()
            return ""
        store = self.takeRow(self.length - 1)
        self.__lastindex -= 1
        return store[1].secert

    def leave(self):
        if self.length == 0:
            self.__indexerror.setText("IndexError: leave() on Empty {}()".format(self.ds))
            self.__indexerror.exec()
            return ""
        store = self.takeRow(0)
        return store[1].secert

    def refresh(self):
        for _ in range(self.length):
            self.__setitem__(_, _, index=True)
        self.__lastindex = self.length

    def clear(self) -> list:
        """ Overriding it in to avoid removal of the horizontal headers"""
        return [self.pop() for _ in range(self.length)]

    def reload(self, index):
        """ ! Not Tested"""
        if index is None:
            [[__.reload() for __ in self[_]] for _ in range(self.length)]

    def toTuple(self):
        return tuple([self[_] for _ in range(self.length)])

    def replace(self, lst):
        self.clear()
        self.extend(lst)

    def extend(self, lst, front=False):
        print(lst)
        if front:
            store = self.tuple
            self.replace(lst)
            self.extend(store)
        else:
            [self.append(_) for _ in lst]


class DisplayView(QtWidgets.QTableView):
    """
    * Table View for the ListView()

    Lol tho Table but its list since index col is not meant for the modification
    """

    def __init__(self, parent, *args):
        super().__init__(parent, *args)
        self.verticalHeader().setVisible(False)  # removes the custom index column for  the dsapy.Queues.Queue()


class ListView(DisplayView):
    """
    one of the GUI reper.used in dsapy

    In dsapy.DS.Stacks.Stack() and dspay.DS.Queues.Queue()

    is this a JOJO ref.?

    => yes
    """

    def __init__(self, container=[], parent=None, *args):
        super().__init__(parent, *args)
        self.__model = DisplayModel(container)
        self.setModel(self.__model)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.__arrange()

    def __arrange(self):
        pass

    def __getattr__(self, value):
        result = self.__model.__getattr__(value)
        if result is not None:
            pass
        return result

    def __getitem__(self, item):
        return self.__model.__getitem__(item)

    def __setitem__(self, key, value):
        return self.__model.__setitem__(key, value)

    def __delitem__(self, key):
        return self.__model.__delitem__(key)

    def __repr__(self):
        return 'ListView({})'.format(self.tuple)

    def __str__(self):
        return str(self.tuple)

    def __del__(self):
        if self.cultured:
            print('Caese{}'.format('r' * 69))

    def __len__(self):
        return self.__model.__len__()

    def __iter__(self):
        return self.__model.__iter__()

    def __next__(self):
        return self.__model.__next__()

    def model(self):
        return self.__model

    def console_print(self):
        """! Not Tested"""
        return print(self.tuple)

    def append(self, item):
        self.__model.append(item)

    def go(self, item):
        return self.append(item)

    def push(self, item):
        return self.append(item)

    def pop(self):
        return self.__model.pop()

    def clear(self):
        self.__model.clear()

    def leave(self):
        return self.__model.leave()

    def flush(self):
        return self.clear()

    def refresh(self):
        return self.__model.refresh()

    def reload(self, index=None):
        """ ! Not Tested"""
        return self.__model.reload(index)

    def replace(self, lst):
        return self.__model.replace(lst)

    def extend(self, lst, front=False):
        return self.__model.extend(lst, front)

    def merge(self, lst, front=False):
        return self.extend(lst, front)

    def insert(self, pos, item):
        return self.__model.insert(pos, item)

    @staticmethod
    def start():
        nigerundayo = ListView()
        nigerundayo.show()

    def seno(self):
        """ alias for the show()"""
        self.show()


if __name__ == '__main__':
    class MiniConsole(QtWidgets.QWidget):
        def __init__(self):
            super().__init__()
            self.line = QtWidgets.QLineEdit(self, placeholderText='Enter a line of code', returnPressed=self.execute)
            self.line.move(100, 100)
            self.show()

        def execute(self):
            exec(self.line.text())
            self.line.clear()


    app = QtWidgets.QApplication([])
    store = ListView([1, 2, 3])
    store.seno()
    console = MiniConsole()
    app.exec()
