from PyQt5 import QtWidgets,QtCore,QtGui
from typing import Any, Iterator,NoReturn
import sys

class Element(QtWidgets.QTableWidgetItem):
    def __init__(self,*args,element=None):
        super().__init__(*args)
        self.element=element
        self.setIcon(QtGui.QIcon('QtRWidgets\\LIST\\point.png'))
        self.setFlags(QtCore.Qt.ItemIsEnabled)
    
    def swap(self,other):
        self.element,other.element=other.element,self.element
        store=self.text()
        self.setText(other.text())
        other.setText(store)

class Container(QtWidgets.QTableWidget):
    ''' Container is used for displaying iterables '''
    def __init__(self,parent=None,name='Container'):
        super().__init__(parent)
        self.setColumnCount(1)
        self.setRowCount(0)
        self.__name=name
        self.setHorizontalHeaderLabels(['Elements'])
    
    def __repr__(self) -> str:return '{}({})'.format(self.name,self.tuple)

    def __str__(self) -> str:return str(self.tuple)

    def __add__(self,other:Iterator) -> tuple:
        return self.tuple+tuple(other)
    
    def __mul__(self,other:int) -> tuple:
        return self.tuple*other


    def __getattr__(self,index) -> Any:
        if index=='tuple':return self.__represent()
        elif index=='name':return self.__name
        elif index=='head' or index=='front' or index=='top':return self[0]
        elif index=='tail' or index=='back':return self[self.length-1]
        elif index=='length':return self.rowCount()
        else: raise AttributeError('{}() has no attribute named {}'.format(self.__name,index))
        
    def __len__(self) -> int: return self.length

    def __iter__(self) -> QtWidgets.QTableWidgetItem:
        self.count=0
        return self

    def __next__(self):
        if self.count<self.length:
            store=self[self.count]
            self.count+=1
            return store
        else:raise StopIteration
    
    def __getitem__(self,index) -> Any:
        return self.item(index,0).element

    def __setitem__(self,index,value) -> NoReturn:
        item=Element(str(value),element=value)
        self.setItem(index,0,item)
    
    def __getTrueItem(self,index) -> "Element":
        return self.item(index,0)
    
    def __represent(self) -> tuple:
        mini=[]
        for i in self:
            mini.append(i)
        return tuple(mini)

    def setObjectName(self,name:str) -> NoReturn: 
        try:self.__name:str=str(name)
        except:raise TypeError('Name Must be of String Type')

    def push(self,element) -> NoReturn:
        try:
            store=str(element)
            self.insertRow(self.length)
            temp=Element(store,element=element)
            self.setItem(self.length-1,0,temp)
        except:raise TypeError('str() failed for the given {}'.format(element))

    def pop(self) -> QtWidgets.QTableWidgetItem:
        return self.removeRow(self.length-1)

    def go(self,element) -> NoReturn:
        self.push(element)

    def leave(self):
        return self.removeRow(0)
    
    def clear(self) -> NoReturn:
        '''OverRiding Super class method'''
        self.flush()

    def flush(self) -> NoReturn:
        for i in range(self.length):self.pop()
    
    def properties(self) -> dict:
        return {
            'size':self.length,
            'tuple':self.tuple,
            'nbytes':sys.getsizeof(self.tuple),
            'id':id(self)
        }
        
    def reverse(self) -> NoReturn :
        templength=self.length
        for i in range(templength//2):
            temp1,temp2=self.__getTrueItem(i),self.__getTrueItem(templength-i-1)
            temp1.swap(temp2)

if __name__=='__main__':
    c=QtWidgets.QApplication([])
    test=QtWidgets.QWidget()
    main=Container(test)
    a=[1,2,3]
    edit=QtWidgets.QLineEdit(test)
    def testing():
        exec(edit.text())
        edit.clear()
    bt=QtWidgets.QPushButton(test,text='evalute',clicked=testing)
    edit.move(100,500)
    bt.move(100,600)
    test.show()
    c.exec()
    
    
