from PyQt5.QtWidgets import *
from mevcut_araclar import Ui_Form
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'otopark')
cursor = con.cursor()

class MevcutAraclar(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.mevcutaraclar = Ui_Form()
        self.mevcutaraclar.setupUi(self)
        self.mevcutaraclar.aracgetir.clicked.connect(self.AracGetir)
        self.mevcutaraclar.aracguncelle.clicked.connect(self.AracGuncelle)
    




    def AracGetir(self):
        query = "select aracplaka,giristarihi,kalacagisure from mevcutaraclar"
        cursor.execute(query)
        veriler = cursor.fetchall()
        self.mevcutaraclar.mevcutaraclar.setRowCount(len(veriler))
        self.mevcutaraclar.mevcutaraclar.setColumnCount(3)
        self.mevcutaraclar.mevcutaraclar.setHorizontalHeaderLabels(["Araç Plaka", "Giriş Tarihi", "Kalacağı Süre"])
        for satir,kayit in enumerate(veriler):
            for sutun, deger in enumerate(kayit):
               self.mevcutaraclar.mevcutaraclar.setItem(satir,sutun,QTableWidgetItem(str(deger)))
    


    def AracGuncelle(self):
        plaka = self.mevcutaraclar.aracplaka.text()
        tarih = self.mevcutaraclar.giristarih.text()
        sure = self.mevcutaraclar.kalacagisure.text()

        if tarih == "":
            cursor.execute("update mevcutaraclar set kalacagisure = %s where aracplaka = %s",(sure,plaka))
            con.commit()
            QMessageBox.information(self,"Uyarı","Süre Güncellendi !")
            self.mevcutaraclar.kalacagisure.clear()
            self.mevcutaraclar.aracplaka.clear()
        elif sure == "":
            cursor.execute("update mevcutaraclar set giristarihi = %s where aracplaka = %s",(tarih,plaka))
            con.commit()
            QMessageBox.information(self,"Uyarı","Tarih Güncellendi !")
            self.mevcutaraclar.giristarih.clear()
            self.mevcutaraclar.aracplaka.clear()
        else:
            cursor.execute("update mevcutaraclar set giristarihi = %s,kalacagisure = %s where aracplaka = %s",(tarih,sure,plaka))
            con.commit()
            QMessageBox.information(self,"Uyarı","Bilgiler Güncellendi !")
            self.mevcutaraclar.giristarih.clear()
            self.mevcutaraclar.kalacagisure.clear()
            self.mevcutaraclar.aracplaka.clear()
