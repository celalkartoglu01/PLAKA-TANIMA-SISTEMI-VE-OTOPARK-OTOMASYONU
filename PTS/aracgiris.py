from PyQt5.QtWidgets import *
from arac_giris import Ui_Form
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import cv2
from alg1 import plaka_konum_don
from plakatanima import plakaTani
import mysql.connector


con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'otopark')
cursor = con.cursor()



class AracGiris(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.aracgiris = Ui_Form()
        self.aracgiris.setupUi(self)
        self.aracgiris.aracsec.clicked.connect(self.AracSec)
        self.aracgiris.plakagoster.clicked.connect(self.AracPlaka)
        self.aracgiris.durumgoster.clicked.connect(self.DurumGoster)
        self.aracgiris.bariyerackapat.clicked.connect(self.BariyerDurum)
        self.aracgiris.girisiniyap.clicked.connect(self.GirisiniYap)
        self.scene = QtWidgets.QGraphicsScene()  
        self.aracgiris.aracgoruntu.setScene(self.scene)
        self.file_path = None
    


    def AracSec(self):
        self.file_path,_ = QFileDialog.getOpenFileName(self, "Fotoğraf Seç", "", "*.png *.jpg *.jpeg")

        if self.file_path:
            pixmap = QPixmap(self.file_path)
            view_rect = self.aracgiris.aracgoruntu.rect()
            scaled_pixmap = pixmap.scaled(view_rect.size(), aspectRatioMode=Qt.KeepAspectRatio)
            self.scene.clear()  
            self.scene.addPixmap(scaled_pixmap)
            self.aracgiris.aracgoruntu.setScene(self.scene)
            self.aracgiris.aracgoruntu.horizontalScrollBar().setVisible(False)
            self.aracgiris.aracgoruntu.verticalScrollBar().setVisible(False)
            
    

    def AracPlaka(self):
        dosya_yolu = self.file_path[37:]
        img = cv2.imread(dosya_yolu)
        img = cv2.resize(img,(500,500))
        plaka = plaka_konum_don(img)
        plakaImg,plakaKarakter = plakaTani(img,plaka)
        self.aracgiris.plaka.setText(plakaKarakter)
            

    def DurumGoster(self):
        plaka = self.aracgiris.plaka.text()
        query = "SELECT * FROM kayitliaraclar WHERE aracplaka = %s"
        cursor.execute(query, (plaka,))
        result = cursor.fetchone()

        if result:
            self.aracgiris.durum.setText("Araç Kayıtlı")
        else:
            self.aracgiris.durum.setText("Araç Kayıtlı Değil")
    


    def BariyerDurum(self):
        durum = self.aracgiris.durum.text()

        if durum == "Araç Kayıtlı":
            self.aracgiris.bariyer.setText("Bariyer Açıldı !")
        elif durum == "Araç Kayıtlı Değil":
            self.aracgiris.bariyer.setText("Bariyer Kapalı !")
    


    def GirisiniYap(self):
        plaka = self.aracgiris.plaka.text()
        sure = self.aracgiris.kalacagisure.text()
        query = "insert into mevcutaraclar(aracplaka,kalacagisure) values(%s,%s)"
        cursor.execute(query,(plaka,sure))
        con.commit()
        QMessageBox.information(self,"Uyarı","Araç Girişi Yapıldı !")
        self.aracgiris.kalacagisure.clear()
        self.aracgiris.plaka.clear()
        self.aracgiris.durum.clear()
        self.aracgiris.bariyer.clear()
        self.scene.clear()
