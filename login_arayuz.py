from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

def window():
    app=QApplication(sys.argv)
    pencere=QWidget()
    form=QFormLayout()
    g1=QLineEdit()
    g2=QLineEdit()
    button=QPushButton("Giriş Yap")
    g2.setEchoMode(QLineEdit.Password)
    form.addRow(QLabel("Kullanıcı Adı:"),g1)
    form.addRow(QLabel("Şifre:"),g2)
    form.addRow(button)
    pencere.setLayout(form)
    pencere.setWindowTitle("Login Basic - 1")
    pencere.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    window()