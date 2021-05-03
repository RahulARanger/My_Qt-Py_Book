from PyQt5 import QtWidgets, QtCore
import datetime


class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='QDateTimeEdit')
        self.select = QtWidgets.QDateTimeEdit(self.window, toolTip='QDateTimeEdit',
                                              date=QtCore.QDate.currentDate(),
                                              # datetime.date.today() this one also works
                                              time=QtCore.QTime(10, 0),  # datetime.time(10,0) this one also works
                                              displayFormat='HH:mm dd-MM-yyyy',
                                              # 'H' for hours and 'm' for min and 'd,M,Y' for date month and year
                                              maximumDate=datetime.date.today(),
                                              minimumDate=datetime.date(2020, 1, 1),
                                              minimumTime=datetime.time(2, 3),
                                              calendarPopup=True)  # if calendPopup=False then it's same as Spinbox so with True it's totally cool
        self.select.show()
        self.window.show()


test().exec()
# * refer this for more displayFormat styles: https://doc.qt.io/qt-5/qdatetime.html
# ! QtCore has a module for handling date and time but it isnt necessary to use tht always. So we can also use datetime module
