from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(476, 494)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 25 15pt \"Bahnschrift Light Condensed\";\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label.setBaseSize(QtCore.QSize(100, 10000))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit.setMaxLength(16)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 3, 2, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 3, 0, 1, 1)
        self.btn_c = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_c.sizePolicy().hasHeightForWidth())
        self.btn_c.setSizePolicy(sizePolicy)
        self.btn_c.setObjectName("btn_c")
        self.gridLayout.addWidget(self.btn_c, 0, 0, 1, 1)
        self.btn_arrow = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_arrow.sizePolicy().hasHeightForWidth())
        self.btn_arrow.setSizePolicy(sizePolicy)
        self.btn_arrow.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);")
        self.btn_arrow.setObjectName("btn_arrow")
        self.gridLayout.addWidget(self.btn_arrow, 0, 1, 1, 1)
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sign.sizePolicy().hasHeightForWidth())
        self.btn_sign.setSizePolicy(sizePolicy)
        self.btn_sign.setObjectName("btn_sign")
        self.gridLayout.addWidget(self.btn_sign, 4, 1, 1, 1)
        self.bnt_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bnt_0.sizePolicy().hasHeightForWidth())
        self.bnt_0.setSizePolicy(sizePolicy)
        self.bnt_0.setObjectName("bnt_0")
        self.gridLayout.addWidget(self.bnt_0, 4, 0, 1, 1)
        self.btn_comma = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_comma.sizePolicy().hasHeightForWidth())
        self.btn_comma.setSizePolicy(sizePolicy)
        self.btn_comma.setObjectName("btn_comma")
        self.gridLayout.addWidget(self.btn_comma, 4, 2, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)
        self.btn_plus.setObjectName("btn_plus")
        self.gridLayout.addWidget(self.btn_plus, 2, 3, 1, 1)
        self.btn_rez = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_rez.sizePolicy().hasHeightForWidth())
        self.btn_rez.setSizePolicy(sizePolicy)
        self.btn_rez.setObjectName("btn_rez")
        self.gridLayout.addWidget(self.btn_rez, 3, 3, 2, 1)
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy)
        self.btn_minus.setObjectName("btn_minus")
        self.gridLayout.addWidget(self.btn_minus, 1, 3, 1, 1)
        self.btn_del = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy)
        self.btn_del.setObjectName("btn_del")
        self.gridLayout.addWidget(self.btn_del, 0, 2, 1, 1)
        self.btn_mul = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy)
        self.btn_mul.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_mul.setObjectName("btn_mul")
        self.gridLayout.addWidget(self.btn_mul, 0, 3, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.add_functions()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_c.setText(_translate("MainWindow", "C"))
        self.btn_arrow.setText(_translate("MainWindow", "←"))
        self.btn_sign.setText(_translate("MainWindow", "+/-"))
        self.bnt_0.setText(_translate("MainWindow", "0"))
        self.btn_comma.setText(_translate("MainWindow", ","))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_rez.setText(_translate("MainWindow", "="))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_del.setText(_translate("MainWindow", "/"))
        self.btn_mul.setText(_translate("MainWindow", "*"))
        self.btn_8.setText(_translate("MainWindow", "8"))
    '''
    Добавление обработчиков кнопок.
    '''
    def add_functions(self):
        self.lineEdit.setEnabled(False)
        #Кнопки цифр
        self.bnt_0.clicked.connect(lambda: self.writeNumber(self.bnt_0.text()))
        self.btn_1.clicked.connect(lambda: self.writeNumber(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.writeNumber(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.writeNumber(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.writeNumber(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.writeNumber(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.writeNumber(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.writeNumber(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.writeNumber(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.writeNumber(self.btn_9.text()))
        #Удаление правого символа.
        self.btn_arrow.clicked.connect(self.backspace)
        #операции todo:валидация
        self.btn_plus.clicked.connect(lambda: self.operation(self.btn_plus.text()))
        self.btn_minus.clicked.connect(lambda: self.operation(self.btn_minus.text()))
        self.btn_mul.clicked.connect(lambda: self.operation(self.btn_mul.text()))
        self.btn_del.clicked.connect(lambda: self.operation(self.btn_del.text()))
        #Удаление всего
        self.btn_c.clicked.connect(self.delAll)
        #запятая
        self.btn_comma.clicked.connect(self.writeComma)
        #равно
        self.btn_rez.clicked.connect(self.rezult)
        #знак
        self.btn_sign.clicked.connect(self.sign)


    #Кнопки цифр
    def writeNumber(self,text):
        if (self.lineEdit.isEnabled()):
            self.lineEdit.setEnabled(False)
            self.lineEdit.setText('')
 
        if (self.lineEdit.text()=='0' and text =='0'):
            self.lineEdit.setText(self.lineEdit.text())
        else:
            self.lineEdit.setText(self.lineEdit.text()+ text)

    #Удаление правого символа.
    def backspace(self):
        self.lineEdit.setText(self.lineEdit.text()[0:len(self.lineEdit.text())-1])

    #Операции
    def operation(self, op):
        if len(self.lineEdit.text()) == 0 and len(self.label.text())!=0:
            if self.label.text()[-1] not in ('+','-','/','*'):
                self.label.setText(self.label.text()+op)
            
        if (len(self.lineEdit.text()) != 0):
            if (len(self.label.text()) == 0):
                self.label.setText(self.lineEdit.text()+op)
                self.lineEdit.setText('')
            else:
                self.label.setText(self.label.text()+self.lineEdit.text())
                self.lineEdit.setText(str(eval(self.label.text())))
                self.lineEdit.setEnabled(True)
                self.label.setText(self.label.text()+op)
    
    #Удаление всего
    def delAll(self):
        self.label.setText('')
        self.lineEdit.setText('')
    
    #Добавить запятую
    def writeComma(self):
        line = self.lineEdit
        if len(line.text()) !=0 and not('.' in line.text()):
            line.setText(line.text()+ '.')

    #Нажатие на равно.        
    def rezult(self):
        l=self.label.text()
        e = self.lineEdit.text()
        if len(l)==0:
            self.lineEdit.setText('')
        else:  
            if self.label.text()[-1] in ('+','-','/','*') and   len(self.lineEdit.text())==0:
                l = l[:-1]           
            self.label.setText(str(eval(l+e)))
            self.lineEdit.setText('')

    #Изменение знака
    def sign(self):
        e = self.lineEdit.text()
        if len(e)!=0:
            if e[0] == '-':
                self.lineEdit.setText(e[1:])
            else:
                self.lineEdit.setText('-'+e)
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())