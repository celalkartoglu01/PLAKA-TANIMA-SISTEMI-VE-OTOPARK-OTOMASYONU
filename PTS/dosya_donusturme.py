from PyQt5 import uic

with open("giris_.py","w",encoding="utf-8") as fout:
    uic.compileUi("giris.ui", fout)


with open("ana_sayfa.py","w",encoding="utf-8") as fout:
    uic.compileUi("anasayfa.ui", fout)


with open("arac_giris.py","w",encoding="utf-8") as fout:
    uic.compileUi("aracgiris.ui", fout)


with open("arac_cikis.py","w",encoding="utf-8") as fout:
    uic.compileUi("araccikis.ui", fout)


with open("kayitli_araclar.py","w",encoding="utf-8") as fout:
    uic.compileUi("kayitliaraclar.ui", fout)


with open("mevcut_araclar.py","w",encoding="utf-8") as fout:
    uic.compileUi("mevcutaraclar.ui", fout)