from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

def window():
    def uygulama():
        kullanici_adi="Selim"
        sifre="12345"
        
        if kullanici_adi==g1.text() and sifre==g2.text():
            durumlabel.setText("Hoşgeldiniz !")
        else:
            durumlabel.setText("Kullanıcı adı veya sifre hatalı!")
            g1.clear()
            g2.clear()

    app=QApplication(sys.argv)
    pencere=QWidget()
    form=QFormLayout()
    g1=QLineEdit()
    g1.setFont(QFont("Helvetica",13))
    g2=QLineEdit()
    button=QPushButton("Giriş Yap")
    g2.setEchoMode(QLineEdit.Password)
    form.addRow(QLabel("Kullanıcı Adı:"),g1)
    form.addRow(QLabel("Şifre:"),g2)
    form.addRow(button)
    durumlabel=QLabel("")
    durumlabel.setFont(QFont("Helvetica",13))
    form.addRow(durumlabel)
    pencere.setLayout(form)

    button.clicked.connect(uygulama)

    pencere.setWindowTitle("Login Basic - 1")
    pencere.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    window()