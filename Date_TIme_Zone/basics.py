from PyQt5 import QtCore
a=QtCore.QDate.currentDate()
b=QtCore.QTime.currentTime()
c=QtCore.QDateTime.currentDateTime()

print(a,b,c)

'''date'''
print(a.toString())
print(a.addDays(3))
print(a.addMonths(69))
print(a.dayOfWeek())
print(a.dayOfYear())

'''time'''

print(b.toString())
