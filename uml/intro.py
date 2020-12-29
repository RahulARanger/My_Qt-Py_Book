# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uml\intro.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(349, 130)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.welcome = QtWidgets.QLabel(Form)
        self.welcome.setScaledContents(False)
        self.welcome.setObjectName("welcome")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.welcome)
        self.usernamelabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.usernamelabel.setFont(font)
        self.usernamelabel.setObjectName("usernamelabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.usernamelabel)
        self.username = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.username.setFont(font)
        self.username.setText("")
        self.username.setFrame(True)
        self.username.setObjectName("username")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.username)
        self.passwordlabel = QtWidgets.QLabel(Form)
        self.passwordlabel.setObjectName("passwordlabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.passwordlabel)
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.password.setPlaceholderText("")
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("password")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.password)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.usernamelabel.raise_()
        self.passwordlabel.raise_()
        self.password.raise_()
        self.welcome.raise_()
        self.pushButton_2.raise_()
        self.username.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.username, self.password)
        Form.setTabOrder(self.password, self.pushButton_2)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.welcome.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#ff557f;\">Greetings</span></p></body></html>"))
        self.welcome.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#ffaa00;\">WELCOME TO THE LOGIN PAGE</span></p></body></html>"))
        self.usernamelabel.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">UserName</span><span style=\" font-size:10pt;\">:</span></p></body></html>"))
        self.username.setWhatsThis(_translate("Form", "<html><head/><body><p>Enter Your UserName:</p><p><br/></p></body></html>"))
        self.passwordlabel.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Password</span>:</p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
