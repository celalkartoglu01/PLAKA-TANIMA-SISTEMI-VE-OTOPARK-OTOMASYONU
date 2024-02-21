from PyQt5.QtWidgets import *
from ana_sayfa import Ui_Form
from mevcutaraclar import MevcutAraclar
from aracgiris import AracGiris
from araccikis import AracCikis
from kayitliaraclar import KayitliAraclar


class AnaSayfa(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.anasayfa = Ui_Form()
        self.anasayfa.setupUi(self)
        self.mevcutaraclar = MevcutAraclar()
        self.aracgiris = AracGiris()
        self.araccikis = AracCikis()
        self.kayitliaraclar = KayitliAraclar()
        self.anasayfa.mevcutaraclar.clicked.connect(self.MevcutAraclarr)
        self.anasayfa.aracgiris.clicked.connect(self.AracGiriss)
        self.anasayfa.araccikis.clicked.connect(self.AracCikiss)
        self.anasayfa.kayitliaraclar.clicked.connect(self.KayitliAraclarr)
    

    def MevcutAraclarr(self):
        self.mevcutaraclar.show()
    

    def AracGiriss(self):
        self.aracgiris.show()
    

    def AracCikiss(self):
        self.araccikis.show()
    

    def KayitliAraclarr(self):
        self.kayitliaraclar.show()
    






