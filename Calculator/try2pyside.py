from PySide6 import QtUiTools,QtWidgets,QtGui
# ! loadui() is used for analyzing and modifying ui files through python (not just for reading that ui files)
# way to load the UI file in Pyside6
class1,class2=QtUiTools.loadUiType('Calculator\\try2.ui')
print('{}: type: {} and {} and type: {}'.format(class1,type(class1),class2,type(class2)))

# Refer: https://github.com/RahulARanger/My_PyQt5_Book/blob/master/Calculator/try2.py this for another way through loadUiType()
# modified class (that inherites the class from the UI)
import string
class CalcVald(QtGui.QValidator):
    def __init__(self):
        super().__init__()
    def dotht(self,string_):
        return str(string_).replace('^','**')
    def validate(self,string_,index):
        state=QtGui.QValidator.Acceptable
        if index-1<0:return state,string_,index
        whatisit='n' if string_[index-1] in string.digits else '?'
        if whatisit=='?':
            state=QtGui.QValidator.Invalid
            whatisit='s' if string_[index-1] in '+.-*/^' else '?'
            if whatisit=='s':
                if  index-2<0 and string[index-1]=='.' :state=QtGui.QValidator.Acceptable
                else: 
                    if string_[index-2] not in '+-/*.^':state=QtGui.QValidator.Acceptable
        return state,string_,index
class Calcu(class2,class1):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.validator=CalcVald()
        self.display.setValidator(self.validator)
        self.numbers=[self.zero,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine]
        self.symbols=[self.plus,self.minus,self.division,self.multiply,self.dot,self.power]
        self.connect()
        self.start()
    def connect(self):
        [_.clicked.connect(lambda x=True,y=_.text():self.display.insert(y)) for _ in self.numbers+self.symbols]
        self.clear.clicked.connect(self.display.clear)
        self.backspace.clicked.connect(self.display.backspace)
        print()
        self.equal.clicked.connect(self.addLog)
    def addLog(self):
        # dump logs for now
        self.display.setText(self.validator.dotht(eval((self.display.text()))))
        self.listWidget.addItem(str(self.display.text()))
    def start(self):
        self.show()
# extra code for execution
app=QtWidgets.QApplication([])
a=Calcu()
app.exec_()
