from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtUiTools import *
import math

class Calc(QMainWindow):
    def __init__(self):
        super().__init__()


        loader = QUiLoader()
        self.ui = loader.load("design.ui")
        self.ui.show()
        self.txt=""
        self.operator = ""

        self.ui.BtnNum0.clicked.connect(self.btn0)
        self.ui.BtnNum1.clicked.connect(self.btn1)
        self.ui.BtnNum2.clicked.connect(self.btn2)
        self.ui.BtnNum3.clicked.connect(self.btn3)
        self.ui.BtnNum4.clicked.connect(self.btn4)
        self.ui.BtnNum5.clicked.connect(self.btn5)
        self.ui.BtnNum6.clicked.connect(self.btn6)
        self.ui.BtnNum7.clicked.connect(self.btn7)
        self.ui.BtnNum8.clicked.connect(self.btn8)
        self.ui.BtnNum9.clicked.connect(self.btn9)
        self.ui.BtnDot.clicked.connect(self.dot)
        self.ui.BtnClear.clicked.connect(self.clear)
        

        self.ui.BtnPlus.clicked.connect(self.plus)
        self.ui.BtnMinus.clicked.connect(self.minus)
        self.ui.BtnMul.clicked.connect(self.mul)
        self.ui.BtnDiv.clicked.connect(self.div)
        self.ui.BtnRoot.clicked.connect(self.root)
        self.ui.BtnLog.clicked.connect(self.log)
        self.ui.BtnPower.clicked.connect(self.power)
        self.ui.BtnMod.clicked.connect(self.mod)
        self.ui.BtnCos.clicked.connect(self.cos)
        self.ui.BtnSin.clicked.connect(self.sin)
        self.ui.BtnTan.clicked.connect(self.tan)
        self.ui.BtnCot.clicked.connect(self.cot)

        self.ui.BtnEqual.clicked.connect(self.equal)


    def setBgColorWhite(self): 
        self.ui.BtnPlus.setStyleSheet("background-color: #ffffff")
        self.ui.BtnMinus.setStyleSheet("background-color: #ffffff")
        self.ui.BtnMul.setStyleSheet("background-color: #ffffff")
        self.ui.BtnDiv.setStyleSheet("background-color: #ffffff")
        self.ui.BtnEqual.setStyleSheet("background-color: #ffffff")
        self.ui.BtnLog.setStyleSheet("background-color: #ffffff")
        self.ui.BtnCos.setStyleSheet("background-color: #ffffff")
        self.ui.BtnSin.setStyleSheet("background-color: #ffffff")
        self.ui.BtnTan.setStyleSheet("background-color: #ffffff")
        self.ui.BtnCot.setStyleSheet("background-color: #ffffff")
        self.ui.BtnMod.setStyleSheet("background-color: #ffffff")
        self.ui.BtnRoot.setStyleSheet("background-color: #ffffff")
        self.ui.BtnPower.setStyleSheet("background-color: #ffffff")


    def btn0(self) :
        self.txt += "0"
        self.ui.TextBox.setText(self.txt)

    def btn1(self) :
        self.txt += "1"
        self.ui.TextBox.setText(self.txt)

    def btn2(self) :
        self.txt += "2"
        self.ui.TextBox.setText(self.txt)

    def btn3(self) :
        self.txt += "3"
        self.ui.TextBox.setText(self.txt)

    def btn4(self) :
        self.txt += "4"
        self.ui.TextBox.setText(self.txt)

    def btn5(self) :
        self.txt += "5"
        self.ui.TextBox.setText(self.txt)

    def btn6(self) :
        self.txt += "6"
        self.ui.TextBox.setText(self.txt)

    def btn7(self) :
        self.txt += "7"
        self.ui.TextBox.setText(self.txt)

    def btn8(self) :
        self.txt += "8"
        self.ui.TextBox.setText(self.txt)

    def btn9(self) :
        self.txt += "9"
        self.ui.TextBox.setText(self.txt)

    def dot(self) :
        if "." not in self.txt :
            self.txt += "."
        self.ui.TextBox.setText(self.txt)

    def clear(self) :
        self.txt = ""
        self.ui.TextBox.setText(self.txt)
        self.setBgColorWhite()





    def plus(self) :
        if self.operator != "+" and self.txt!="" :
            self.operator = "+"
            self.setBgColorWhite()
            self.ui.BtnPlus.setStyleSheet("background-color: #F9ED69")
            self.num1 = float(self.txt)
            self.txt = ""
            self.ui.TextBox.setText(self.txt)
            
    def minus(self) :
        if self.operator!="-" and self.txt != "":
            self.operator = "-"
            self.setBgColorWhite()
            self.ui.BtnMinus.setStyleSheet("background-color: #F9ED69 ")
            self.num1 = float(self.txt)
            self.txt = ""
            self.ui.TextBox.setText(self.txt)

    def mul(self) :
        if self.operator != "x" and self.txt != "":
            self.operator = "x"
            self.setBgColorWhite()
            self.ui.BtnMul.setStyleSheet("background-color: #F9ED69 ")
            self.num1 = float(self.txt)
            self.txt = ""
            self.ui.TextBox.setText(self.txt)

    def div(self) :
        if self.operator != "/" and self.txt != "":
            self.operator = "/"
            self.setBgColorWhite()
            self.ui.BtnDiv.setStyleSheet("background-color: #F9ED69 ")
            self.num1 = float(self.txt)
            self.txt = ""
            self.ui.TextBox.setText(self.txt)

    def power(self) :
        if self.operator != "^" and self.txt != "":
            self.operator = "^"
            self.setBgColorWhite()
            self.ui.BtnPower.setStyleSheet("background-color: #F9ED69 ")
            self.num1 = float(self.txt)
            self.txt = ""
            self.ui.TextBox.setText(self.txt)

    def mod(self) :
        if self.operator != "%" and self.txt != "":
            self.operator = "%"
            self.setBgColorWhite()
            self.ui.BtnMod.setStyleSheet("background-color: #F9ED69 ")
            self.num1 = float(self.txt)
            self.txt = ""
            self.ui.TextBox.setText(self.txt)

    def root(self) :
        if self.operator != "√" and self.txt != "":
            self.operator = "√"
            self.setBgColorWhite()
            self.ui.BtnRoot.setStyleSheet("background-color: #F9ED69 ")
            self.num1 = float(self.txt)
            self.txt = str(math.pow(self.num1,0.5))
            self.ui.TextBox.setText(self.txt)

    def log(self) :
        if self.operator != "log" and self.txt != "":
            self.operator = "log"
            self.setBgColorWhite()
            self.ui.BtnLog.setStyleSheet("background-color: #F9ED69 ")
            self.num1 = float(self.txt)
            self.txt = str(math.log2(self.num1))
            self.ui.TextBox.setText(self.txt)

    def sin(self) :
        if self.operator != "sin" and self.txt != "":
            self.operator = "sin"
            self.setBgColorWhite()
            self.ui.BtnSin.setStyleSheet("background-color: #F9ED69 ")
            self.num1 = float(self.txt)
            self.txt = str(math.sinh(self.num1))
            self.ui.TextBox.setText(self.txt)

    def cos(self) :
        if self.operator != "cos" and self.txt != "":
            self.operator = "cos"
            self.setBgColorWhite()
            self.ui.BtnCos.setStyleSheet("background-color: #F9ED69 ")
            self.num1 = float(self.txt)
            self.txt = str(math.cosh(self.num1))
            self.ui.TextBox.setText(self.txt)

    def tan(self) :
        if self.operator != "tan" and self.txt != "":
            self.operator = "cos"
            self.setBgColorWhite()
            self.ui.BtnTan.setStyleSheet("background-color: #F9ED69 ")
            self.num1 = float(self.txt)
            self.txt = str(math.tanh(self.num1))
            self.ui.TextBox.setText(self.txt)

    def cot(self) :
        if self.operator != "cot" and self.txt != "":
            self.operator = "cot"
            self.setBgColorWhite()
            self.ui.BtnCot.setStyleSheet("background-color: #F9ED69 ")
            self.num1 = float(self.txt)
            self.txt = str(1/(math.tan(self.num1)))
            self.ui.TextBox.setText(self.txt)





    def equal(self):
        self.num2 = float(self.txt) 
        if self.operator == "+" :
            self.txt = str(self.num1 + self.num2)
        if self.operator == "-" :
            self.txt = str(self.num1 - self.num2)
        if self.operator == "x" :
            self.txt = str(self.num1 * self.num2)
        if self.operator == "/" :
            self.txt = str(self.num1 / self.num2)
        if self.operator == "^" :
            self.txt = str(math.pow(self.num1 , self.num2))
        if self.operator == "mod" :
            self.txt = str(self.num1 % self.num2)
        
        self.setBgColorWhite()
        self.operator=""
        self.ui.TextBox.setText(self.txt)
       

if __name__ == "__main__":
    my_app = QApplication()
    main_window = Calc()
    my_app.exec()