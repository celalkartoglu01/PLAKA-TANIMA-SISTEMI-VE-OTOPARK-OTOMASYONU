# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aracgiris.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1165, 689)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, -40, 1221, 751))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("desktop-wallpaper-logo-full-backgrounds-logo-ferrari.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.durum = QtWidgets.QLineEdit(Form)
        self.durum.setGeometry(QtCore.QRect(850, 210, 101, 31))
        self.durum.setObjectName("durum")
        self.plaka = QtWidgets.QLineEdit(Form)
        self.plaka.setGeometry(QtCore.QRect(690, 210, 101, 31))
        self.plaka.setObjectName("plaka")
        self.girisiniyap = QtWidgets.QPushButton(Form)
        self.girisiniyap.setGeometry(QtCore.QRect(790, 560, 101, 41))
        self.girisiniyap.setObjectName("girisiniyap")
        self.bariyer = QtWidgets.QLineEdit(Form)
        self.bariyer.setGeometry(QtCore.QRect(1020, 210, 101, 31))
        self.bariyer.setObjectName("bariyer")
        self.bariyerackapat = QtWidgets.QPushButton(Form)
        self.bariyerackapat.setGeometry(QtCore.QRect(1020, 140, 101, 41))
        self.bariyerackapat.setObjectName("bariyerackapat")
        self.aracsec = QtWidgets.QPushButton(Form)
        self.aracsec.setGeometry(QtCore.QRect(180, 620, 101, 41))
        self.aracsec.setObjectName("aracsec")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 70, 161, 41))
        self.label_3.setObjectName("label_3")
        self.plakagoster = QtWidgets.QPushButton(Form)
        self.plakagoster.setGeometry(QtCore.QRect(690, 140, 101, 41))
        self.plakagoster.setObjectName("plakagoster")
        self.durumgoster = QtWidgets.QPushButton(Form)
        self.durumgoster.setGeometry(QtCore.QRect(850, 140, 101, 41))
        self.durumgoster.setObjectName("durumgoster")
        self.aracgoruntu = QtWidgets.QGraphicsView(Form)
        self.aracgoruntu.setGeometry(QtCore.QRect(30, 130, 451, 461))
        self.aracgoruntu.setObjectName("aracgoruntu")
        self.kalacagisure = QtWidgets.QLineEdit(Form)
        self.kalacagisure.setGeometry(QtCore.QRect(840, 480, 141, 31))
        self.kalacagisure.setObjectName("kalacagisure")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(120, 20, 861, 51))
        self.label_6.setObjectName("label_6")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(630, 390, 195, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.girisiniyap.setText(_translate("Form", "Girişini Yap"))
        self.bariyerackapat.setText(_translate("Form", "Bariyer"))
        self.aracsec.setText(_translate("Form", "Girecek Aracı Seç"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Araç Görüntüsü</span></p></body></html>"))
        self.plakagoster.setText(_translate("Form", "Plaka"))
        self.durumgoster.setText(_translate("Form", "Durum"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">ARAÇ GİRİŞİ</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Kalacağı Süre (DK) :</span></p></body></html>"))
