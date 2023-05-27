import sys

from math import log10, tan, sin, cos, sqrt, radians, pi
import math
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox, QMainWindow, QLineEdit

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.setWindowTitle('Calculadora')
        self.setFixedSize(450,500)
        
        self.initUi()
    
    def initUi(self):
        self.btn1 = QPushButton('1',self)
        self.btn1.move(50,100)
        self.btn1.clicked.connect(self.numero1)
        self.btn1.setFixedSize(60,60)
        
        self.btn2 = QPushButton('2',self)
        self.btn2.move(120,100)
        self.btn2.clicked.connect(self.numero2)
        self.btn2.setFixedSize(60,60)
        
        self.btn3 = QPushButton('3',self)
        self.btn3.move(190,100)
        self.btn3.clicked.connect(self.numero3)
        self.btn3.setFixedSize(60,60)
        
        self.btn4 = QPushButton('4',self)
        self.btn4.move(50,170)
        self.btn4.clicked.connect(self.numero4)
        self.btn4.setFixedSize(60,60)
        
        self.btn5 = QPushButton('5',self)
        self.btn5.move(120,170)
        self.btn5.clicked.connect(self.numero5)
        self.btn5.setFixedSize(60,60)
        
        self.btn6 = QPushButton('6',self)
        self.btn6.move(190,170)
        self.btn6.clicked.connect(self.numero6)
        self.btn6.setFixedSize(60,60)
        
        self.btn7 = QPushButton('7',self)
        self.btn7.move(50,240)
        self.btn7.clicked.connect(self.numero7)
        self.btn7.setFixedSize(60,60)
        
        self.btn8 = QPushButton('8',self)
        self.btn8.move(120,240)
        self.btn8.clicked.connect(self.numero8)
        self.btn8.setFixedSize(60,60)
        
        self.btn9 = QPushButton('9',self)
        self.btn9.move(190,240)
        self.btn9.clicked.connect(self.numero9)
        self.btn9.setFixedSize(60,60)
        
        self.btn0 = QPushButton('0',self)
        self.btn0.move(120,310)
        self.btn0.clicked.connect(self.numero0)
        self.btn0.setFixedSize(60,60)
        
        self.btn_equal = QPushButton('=',self)
        self.btn_equal.move(190,310)
        self.btn_equal.clicked.connect(self.numero_equal)
        self.btn_equal.setFixedSize(60,60)
        
        self.btn_plus = QPushButton('+',self)
        self.btn_plus.move(260,100)
        self.btn_plus.clicked.connect(self.numero_plus)
        self.btn_plus.setFixedSize(60,60)
        
        self.btn_minus = QPushButton('-',self)
        self.btn_minus.move(260,170)
        self.btn_minus.clicked.connect(self.numero_minus)
        self.btn_minus.setFixedSize(60,60)
        
        self.btn_multiplication = QPushButton('*',self)
        self.btn_multiplication.move(260,240)
        self.btn_multiplication.clicked.connect(self.numero_multiplication)
        self.btn_multiplication.setFixedSize(60,60)
        
        self.btn_divition = QPushButton('/',self)
        self.btn_divition.move(260,310)
        self.btn_divition.clicked.connect(self.numero_divition)
        self.btn_divition.setFixedSize(60,60)
        
        self.btn_C = QPushButton('C',self)
        self.btn_C.move(50,310)
        self.btn_C.clicked.connect(self.numero_C)
        self.btn_C.setFixedSize(60,60)
        
        self.btn_potencia = QPushButton('^',self)
        self.btn_potencia.move(330,170)
        self.btn_potencia.clicked.connect(self.numero_potencia)
        self.btn_potencia.setFixedSize(60,60)
        
        self.btn_log = QPushButton('log',self)
        self.btn_log.move(330,240)
        self.btn_log.clicked.connect(self.numero_log)
        self.btn_log.setFixedSize(60,60)
        
        self.btn_sin = QPushButton('sin',self)
        self.btn_sin.move(50,380)
        self.btn_sin.clicked.connect(self.numero_sin)
        self.btn_sin.setFixedSize(60,60)
        
        self.btn_cos = QPushButton('cos',self)
        self.btn_cos.move(120,380)
        self.btn_cos.clicked.connect(self.numero_cos)
        self.btn_cos.setFixedSize(60,60)
        
        self.btn_tan = QPushButton('tan',self)
        self.btn_tan.move(190,380)
        self.btn_tan.clicked.connect(self.numero_tan)
        self.btn_tan.setFixedSize(60,60)
        
        self.btn_pi = QPushButton('π',self)
        self.btn_pi.move(260,380)
        self.btn_pi.clicked.connect(self.numero_pi)
        self.btn_pi.setFixedSize(60,60)
        
        self.btn_erase= QPushButton('DEL',self)
        self.btn_erase.move(330,100)
        self.btn_erase.clicked.connect(self.numero_erase)
        self.btn_erase.setFixedSize(60,60)
        
        self.btn_radicacion= QPushButton('√',self)
        self.btn_radicacion.move(330,310)
        self.btn_radicacion.clicked.connect(self.numero_radicacion)
        self.btn_radicacion.setFixedSize(60,60)
        
        self.txt_resultado = QLineEdit(self)
        self.txt_resultado.setEnabled(False)
        self.txt_resultado.setFixedSize(345,50)
        self.txt_resultado.move(50,30)
        
    def numero1(self):
        numero = self.txt_resultado.text()
        numero += '1'
        self.txt_resultado.setText(numero)
        
    def numero2(self):
        numero = self.txt_resultado.text()
        numero += '2'
        self.txt_resultado.setText(numero)
        
    def numero3(self):
        numero = self.txt_resultado.text()
        numero += '3'
        self.txt_resultado.setText(numero)
        
    def numero4(self):
        numero = self.txt_resultado.text()
        numero += '4'
        self.txt_resultado.setText(numero)
        
    def numero5(self):
        numero = self.txt_resultado.text()
        numero += '5'
        self.txt_resultado.setText(numero)
        
    def numero6(self):
        numero = self.txt_resultado.text()
        numero += '6'
        self.txt_resultado.setText(numero)
        
    def numero7(self):
        numero = self.txt_resultado.text()
        numero += '7'
        self.txt_resultado.setText(numero)
        
    def numero8(self):
        numero = self.txt_resultado.text()
        numero += '8'
        self.txt_resultado.setText(numero)
        
    def numero9(self):
        numero = self.txt_resultado.text()
        numero += '9'
        self.txt_resultado.setText(numero)
        
    def numero0(self):
        numero = self.txt_resultado.text()
        numero += '0'
        self.txt_resultado.setText(numero)
        
    def numero_equal(self):
        numero = self.txt_resultado.text()
        
        if numero.count('^') > 0:
            numero = numero.replace('^','**')
        if numero.count('log') > 0:
            numero_1 = ''
            numero_2 = self.txt_resultado.text()
            
            while True:
                for a in range(numero_2.find('log') + 3,len(numero_2)):
                    if numero_2[a]  != '+' and numero_2[a] != '-' and numero_2[a] != '*' and numero_2[a] != '/':
                        numero_1 += numero_2[a]
                    else:
                        break
            
                numero = numero.replace(f'log{numero_1}',f'log10({numero_1})')
                
                numero_2 = numero_2[numero_2.find(f'log{numero_1}') + len(f'log{numero_1}') + 1 : len(numero_2)]
                
                numero_1 = ''
                
                if numero_2.count('log') == 0:
                    break
            
        if numero.count('sin') > 0:
            numero_1 = ''
            numero_2 = self.txt_resultado.text()
            
            while True:
                for a in range(numero_2.find('sin') + 3,len(numero_2)):
                    if numero_2[a]  != '+' and numero_2[a] != '-' and numero_2[a] != '*' and numero_2[a] != '/':
                        numero_1 += numero_2[a]
                    else:
                        break
                    
                numero_3 = int(numero_1)
                numero_3 = radians(numero_3)
                numero_3 = str(numero_3)
            
                numero = numero.replace(f'sin{numero_1}',f'sin({numero_3})')
                
                numero_2 = numero_2[numero_2.find(f'sin{numero_1}') + len(f'sin{numero_1}') + 1 : len(numero_2)]
                
                numero_1 = ''
                
                if numero_2.count('sin') == 0:
                    break
                
        if numero.count('cos') > 0:
            numero_1 = ''
            numero_2 = self.txt_resultado.text()
            
            while True:
                for a in range(numero_2.find('cos') + 3,len(numero_2)):
                    if numero_2[a]  != '+' and numero_2[a] != '-' and numero_2[a] != '*' and numero_2[a] != '/':
                        numero_1 += numero_2[a]
                    else:
                        break
                    
                numero_3 = int(numero_1)
                numero_3 = radians(numero_3)
                numero_3 = str(numero_3)
            
                numero = numero.replace(f'cos{numero_1}',f'cos({numero_3})')
                
                numero_2 = numero_2[numero_2.find(f'cos{numero_1}') + len(f'cos{numero_1}') + 1 : len(numero_2)]
                
                numero_1 = ''
                
                if numero_2.count('cos') == 0:
                    break
                
        if numero.count('tan') > 0:
            numero_1 = ''
            numero_2 = self.txt_resultado.text()
            
            while True:
                for a in range(numero_2.find('tan') + 3,len(numero_2)):
                    if numero_2[a]  != '+' and numero_2[a] != '-' and numero_2[a] != '*' and numero_2[a] != '/':
                        numero_1 += numero_2[a]
                    else:
                        break
                    
                numero_3 = int(numero_1)
                numero_3 = radians(numero_3)
                numero_3 = str(numero_3)
            
                numero = numero.replace(f'tan{numero_1}',f'tan({numero_3})')
                
                numero_2 = numero_2[numero_2.find(f'tan{numero_1}') + len(f'tan{numero_1}') + 1 : len(numero_2)]
                
                numero_1 = ''
                
                if numero_2.count('tan') == 0:
                    break
                
        if numero.count('π') > 0:
            numero = numero.replace(f'π',f'pi')
            
        if numero.count('√') > 0:
            numero_1 = ''
            numero_2 = self.txt_resultado.text()
            
            while True:
                for a in range(numero_2.find('√') + 1,len(numero_2)):
                    if numero_2[a]  != '+' and numero_2[a] != '-' and numero_2[a] != '*' and numero_2[a] != '/':
                        numero_1 += numero_2[a]
                    else:
                        break
            
                numero = numero.replace(f'√{numero_1}',f'sqrt({numero_1})')
                
                numero_2 = numero_2[numero_2.find(f'√{numero_1}') + len(f'√{numero_1}') + 1 : len(numero_2)]
                
                numero_1 = ''
                
                if numero_2.count('√') == 0:
                    break
                        
        if len(numero):             
            try:            
                numero = eval(numero)
            except ZeroDivisionError as e:
                mensaje = QMessageBox()
                mensaje.setText('ERROR: No puede dividir por cero')
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setWindowTitle('MENSAJE')
            
                mensaje.exec_()
            except:
                mensaje = QMessageBox()
                mensaje.setText('ERROR: Vuelva a intentarlo, hubo un error')
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setWindowTitle('MENSAJE')
        else:
            mensaje = QMessageBox()
            mensaje.setText('MENSAJE: No ha ingresado ningun valor')
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setWindowTitle('MENSAJE')
        
            mensaje.exec_()
        
            
            
        
        self.txt_resultado.setText(str(numero))
    
    def numero_plus(self):
        numero = self.txt_resultado.text()
        try:
            if numero[-1] == '-' or numero[-1] == '+' or numero[-1] == '*' or numero[-1] == '/' or numero[-1] == '^':
                numero = numero[:-1] + '+'
            else:
                numero += '+'
        except IndexError as e:
            mensaje = QMessageBox()
            mensaje.setText('MENSAJE: No ha ingresado ningun valor')
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setWindowTitle('MENSAJE')
        
            mensaje.exec_()
        self.txt_resultado.setText(numero)
        
    def numero_minus(self):
        numero = self.txt_resultado.text()
        try:
            if numero[-1] == '-' or numero[-1] == '+' or numero[-1] == '*' or numero[-1] == '/' or numero[-1] == '^':
                numero = numero[:-1] + '-'
            else:
                numero += '-'
        except IndexError as e:
            mensaje = QMessageBox()
            mensaje.setText('MENSAJE: No ha ingresado ningun valor')
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setWindowTitle('MENSAJE')
        
            mensaje.exec_()
        self.txt_resultado.setText(numero)
        
    def numero_multiplication(self):
        numero = self.txt_resultado.text()
        try:
            if numero[-1] == '-' or numero[-1] == '+' or numero[-1] == '*' or numero[-1] == '/' or numero[-1] == '^':
                numero = numero[:-1] + '*'
            else:
                numero += '*'
        except IndexError as e:
            mensaje = QMessageBox()
            mensaje.setText('MENSAJE: No ha ingresado ningun valor')
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setWindowTitle('MENSAJE')
        
            mensaje.exec_()
        self.txt_resultado.setText(numero)
        
    def numero_divition(self):
        numero = self.txt_resultado.text()
        try:
            if numero[-1] == '-' or numero[-1] == '+' or numero[-1] == '*' or numero[-1] == '/' or numero[-1] == '^':
                numero = numero[:-1] + '/'
            else:
                numero += '/'
        except IndexError as e:
            mensaje = QMessageBox()
            mensaje.setText('MENSAJE: No ha ingresado ningun valor')
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setWindowTitle('INFORMACIÓN')
        
            mensaje.exec_()
        self.txt_resultado.setText(numero)
        
    def numero_C(self):
        self.txt_resultado.setText('')
        
    def numero_potencia(self):
        numero = self.txt_resultado.text()
        try:
            if numero[-1] == '-' or numero[-1] == '+' or numero[-1] == '*' or numero[-1] == '/' or numero[-1] == '^':
                numero = numero[:-1] + '^'
            else:
                numero += '^'
        except IndexError as e:
            mensaje = QMessageBox()
            mensaje.setText('MENSAJE: No ha ingresado ningun valor')
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setWindowTitle('MENSAJE')
        
            mensaje.exec_()
        self.txt_resultado.setText(numero)
        
    def numero_log(self):
        numero = self.txt_resultado.text()
        numero += 'log'
        
        self.txt_resultado.setText(numero)
        
    def numero_sin(self):
        numero = self.txt_resultado.text()
        numero += 'sin'
        
        self.txt_resultado.setText(numero)
        
    def numero_cos(self):
        numero = self.txt_resultado.text()
        numero += 'cos'
        
        self.txt_resultado.setText(numero)
        
    def numero_tan(self):
        numero = self.txt_resultado.text()
        numero += 'tan'
        
        self.txt_resultado.setText(numero)
        
    def numero_pi(self):
        numero = self.txt_resultado.text()
        numero += 'π'
        
        self.txt_resultado.setText(numero)
        
    def numero_erase(self):
        numero = self.txt_resultado.text()
        numero = numero[:-1]
        
        self.txt_resultado.setText(numero)
        
    def numero_radicacion(self):
        numero = self.txt_resultado.text()
        numero += '√'
        
        self.txt_resultado.setText(numero)
        

        
def main():
    app = QApplication(sys.argv)
    
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()