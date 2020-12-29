from PyQt5 import QtWidgets,QtGui,QtCore
import string
class CalcValidator(QtGui.QValidator):
    def __init__(self):
        super().__init__()
    def validate(self,stringe,index):
        state=QtGui.QValidator.Acceptable
        if len(stringe)==0:return state,stringe,index
        if stringe[index-1] in string.ascii_letters:state=QtGui.QValidator.Invalid
        return state,stringe,index

class Calculator(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Calculator')
        self.window.setBaseSize(600,600)
        self.validator=CalcValidator()
        self.screen=QtWidgets.QLineEdit(self.window,placeholderText='0',toolTip='Calc Screen')
        self.numbers=[QtWidgets.QPushButton(self.window,text=str(i)) for i in range(10)]
        self.symbols={i:QtWidgets.QPushButton(self.window,text=i) for i  in '*+-/'}
        self.equal=QtWidgets.QPushButton(self.window,text='=')
        self.layout=QtWidgets.QVBoxLayout()
        self.window.setLayout(self.layout)
        self.adjustscreen()
        self.arrange()
        self.connectevents()
        self.window.show()
    def connectevents(self):
        for i in self.numbers:i.clicked.connect(lambda ch,text=i.text():self.screen.insert(str(text)))
        for i in self.symbols.values():i.clicked.connect(lambda ch,text=i.text():self.screen.insert(text))
        self.equal.clicked.connect(lambda ch:self.screen.setText(str(eval(self.screen.text()))))
    def adjustscreen(self):
        self.screen.setDragEnabled(True)
        self.screen.setValidator(self.validator)
        self.screen.setAlignment(QtCore.Qt.AlignRight)
    def arrange(self):        
        self.screenrow=QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.screenrow)
        self.screenrow.addWidget(self.screen)
        self.rows=[QtWidgets.QHBoxLayout() for i in '.....']
        [self.layout.addLayout(i) for i in self.rows]
        for i in range(1,10):
            self.rows[i//3 if i%3!=0 else i//3-1].addWidget(self.numbers[i])
        self.rows[3].addWidget(self.numbers[0])
        self.rows[3].addWidget(self.equal)
        for i in enumerate(self.symbols):self.rows[i[0]].addWidget(self.symbols[i[1]])
    @staticmethod
    def start():
        app=Calculator()
        app.exec()
Calculator.start()