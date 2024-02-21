from PyQt5.QtWidgets import *
from kayitli_araclar import Ui_Form
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'otopark')
cursor = con.cursor()

class KayitliAraclar(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.kayitliaraclar = Ui_Form()
        self.kayitliaraclar.setupUi(self)
        self.kayitliaraclar.araclarigoster.clicked.connect(self.AraclariGoster)
        self.kayitliaraclar.aracekle.clicked.connect(self.AracEkle)
        self.kayitliaraclar.aracikaldir.clicked.connect(self.AracKaldir)
    


    def AraclariGoster(self):
        query = "select aracsahibi,telno,aracplaka from kayitliaraclar"
        cursor.execute(query)
        veriler = cursor.fetchall()
        self.kayitliaraclar.araclar.setRowCount(len(veriler))
        self.kayitliaraclar.araclar.setColumnCount(3)
        self.kayitliaraclar.araclar.setHorizontalHeaderLabels(["Araç Sahibi", "Tel No", "Plaka"])
        for satir,kayit in enumerate(veriler):
            for sutun, deger in enumerate(kayit):
               self.kayitliaraclar.araclar.setItem(satir,sutun,QTableWidgetItem(str(deger)))



    def AracEkle(self):
        aracsahibi = self.kayitliaraclar.aracsahibi.text()
        telno = self.kayitliaraclar.telno.text()
        plaka = self.kayitliaraclar.aracplaka2.text()
        query = "insert into kayitliaraclar(aracsahibi,telno,aracplaka) values(%s,%s,%s)"
        cursor.execute(query,(aracsahibi,telno,plaka))
        con.commit()
        QMessageBox.information(self,"Uyarı","Araç Sisteme Eklendi !")
        self.kayitliaraclar.aracsahibi.clear()
        self.kayitliaraclar.telno.clear()
        self.kayitliaraclar.aracplaka2.clear()




    def AracKaldir(self):
        plaka = self.kayitliaraclar.aracplaka1.text()
        query = "delete from kayitliaraclar where aracplaka = %s"
        cursor.execute(query,(plaka,))
        con.commit()
        QMessageBox.information(self,"Uyarı","Araç Sistemden Kaldırıldı !")
        self.kayitliaraclar.aracplaka1.clear()