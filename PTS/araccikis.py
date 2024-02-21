from PyQt5.QtWidgets import *
from arac_cikis import Ui_Form
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
import cv2
from alg1 import plaka_konum_don
from plakatanima import plakaTani
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'otopark')
cursor = con.cursor()

class AracCikis(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.araccikis = Ui_Form()
        self.araccikis.setupUi(self)
        self.araccikis.aracsec.clicked.connect(self.AracSec)
        self.scene = QtWidgets.QGraphicsScene()
        self.araccikis.plakagoster.clicked.connect(self.AracPlaka)
        self.araccikis.kaldigisure.clicked.connect(self.KaldigiSure)
        self.araccikis.odenecektutar_2.clicked.connect(self.OdenecekTutar)
        self.araccikis.odemeyial.clicked.connect(self.OdemeyiAl)
        self.araccikis.cikisiniyap.clicked.connect(self.CikisiniYap)



    def AracSec(self):
        self.file_path,_ = QFileDialog.getOpenFileName(self, "Fotoğraf Seç", "", "*.png *.jpg *.jpeg")

        if self.file_path:
            pixmap = QPixmap(self.file_path)
            view_rect = self.araccikis.aracgoruntu.rect()
            scaled_pixmap = pixmap.scaled(view_rect.size(), aspectRatioMode=Qt.KeepAspectRatio)
            self.scene.clear()  
            self.scene.addPixmap(scaled_pixmap)
            self.araccikis.aracgoruntu.setScene(self.scene)
            self.araccikis.aracgoruntu.horizontalScrollBar().setVisible(False)
            self.araccikis.aracgoruntu.verticalScrollBar().setVisible(False)
    


    def AracPlaka(self):
        dosya_yolu = self.file_path[37:]
        img = cv2.imread(dosya_yolu)
        img = cv2.resize(img,(500,500))
        plaka = plaka_konum_don(img)
        plakaImg,plakaKarakter = plakaTani(img,plaka)
        self.araccikis.plaka.setText(plakaKarakter)
    

    def KaldigiSure(self):
        plaka = self.araccikis.plaka.text()
        query = "select kalacagisure from mevcutaraclar where aracplaka = %s"
        cursor.execute(query,(plaka,))
        result = cursor.fetchone()
        if result:
            sure = result[0]
            self.araccikis.kaldigisuree.setText(str(sure))

    def OdenecekTutar(self):
        plaka = self.araccikis.plaka.text()
        query = "select kalacagisure from mevcutaraclar where aracplaka = %s"
        cursor.execute(query,(plaka,))
        result = cursor.fetchone()
        if result:
            sure = result[0]
            self.araccikis.kaldigisuree.setText(str(sure))
            tutar = (sure/60)*20
            self.araccikis.odenecektutar.setText(str(tutar))
    


    def OdemeyiAl(self):
        QMessageBox.information(self,"Uyarı","Ödeme Yapıldı !")
    


    def CikisiniYap(self):
        plaka = self.araccikis.plaka.text()
        query = "delete from mevcutaraclar where aracplaka = %s"
        cursor.execute(query,(plaka,))
        con.commit()
        cursor.close()
        QMessageBox.information(self,"Uyarı","İyi Günler Dileriz !")
        self.scene.clear()
        self.araccikis.plaka.clear()
        self.araccikis.odenecektutar.clear()
        self.araccikis.kaldigisuree.clear()
    



