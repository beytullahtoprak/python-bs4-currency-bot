from PyQt5.QtWidgets import *
import sys
import requests
from bs4 import BeautifulSoup

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        
        self.progOzellik()
        self.dovuzBot()
        self.progElement()
        self.cmbDoviz()
        self.progDuzen()
        
    def progOzellik(self):
        self.setWindowTitle("Döviz Dönüştürücü  Code By Beytullah Toprak")
        self.resize(300, 50)
        
            
    def dovuzBot(self):
        # Döviz Kurları
        site = requests.get("https://kur.doviz.com/")
        kaynak = BeautifulSoup(site.content, "html.parser")
        
        self.amerikan_dolari = kaynak.find("td", {"data-socket-key":"USD"}, {"data-socket-attr":"b"}).text
        self.euro = kaynak.find("td", {"data-socket-key":"EUR"}, {"data-socket-attr":"b"}).text
        self.ingiliz_sterlini = kaynak.find("td", {"data-socket-key":"GBP"}, {"data-socket-attr":"b"}).text
        self.isvicre_frangi = kaynak.find("td", {"data-socket-key":"CHF"}, {"data-socket-attr":"b"}).text
        self.kanada_dolari = kaynak.find("td", {"data-socket-key":"CAD"}, {"data-socket-attr":"b"}).text
            
    def progElement(self):
        self.lbl1 = QLabel("Birim")
        self.lbl2 = QLabel("Sonuç")
        self.lbl3 = QLabel("Döviz Türü")
        self.lblkur = QLabel("<b>Güncel Kurlar</b> <br> <b>USD:</b> {} - <b>EUR:</b> {} - <b>GBP:</b> {} - <b>CHF:</b> {} - <b>CAD:</b> {}"
                             .format(self.amerikan_dolari,self.euro,self.ingiliz_sterlini,self.isvicre_frangi,self.kanada_dolari))
        self.birim = QLineEdit(self)
        self.fiyat = QLineEdit(self)
        self.buton = QPushButton(self)
        self.buton.setText("Dönüştür")
            
    def cmbDoviz(self):
        self.cmb = QComboBox()
        self.money = ["Döviz Türü Seçin","ABD Doları","Euro", "İngiliz Sterlin", "İsviçre Fargı", "Kanada Doları"]
        self.cmb.addItems(self.money)
        
    def progDuzen(self):
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.lblkur)
        self.layout.addWidget(self.lbl1)
        self.layout.addWidget(self.birim)
        self.layout.addWidget(self.lbl3)
        self.layout.addWidget(self.cmb)
        self.layout.addWidget(self.lbl2)
        self.layout.addWidget(self.fiyat)
        self.layout.addWidget(self.buton)
        self.buton.clicked.connect(self.donustur)

    def donustur(self):
        cmbIndex = self.cmb.currentIndex()
        birimAl = self.birim.text()

        if birimAl == "":
            QMessageBox.about(self, "Uyarı", "Lütfen Bir Birim Fiyatı Giriniz")
        elif cmbIndex == 0:
             QMessageBox.about(self, "Uyarı", "Lütfen Bir Para Birimi Seçiniz")
        elif cmbIndex == 1:
            sonuc = round(float(birimAl.replace(",",".")) * float(self.amerikan_dolari.replace(",",".")),2)
            self.fiyat.setText(str(sonuc))
        elif cmbIndex == 2:
            sonuc = round(float(birimAl.replace(",",".")) * float(self.euro.replace(",",".")),2)
            self.fiyat.setText(str(sonuc))
        elif cmbIndex == 3:
            sonuc = round(float(birimAl.replace(",",".")) * float(self.ingiliz_sterlini.replace(",",".")),2)
            self.fiyat.setText(str(sonuc))
        elif cmbIndex == 3:
            sonuc = round(float(birimAl.replace(",",".")) * float(self.isvicre_frangi.replace(",",".")),2)
            self.fiyat.setText(str(sonuc))
        elif cmbIndex == 4:
            sonuc = round(float(birimAl.replace(",",".")) * float(self.kanada_dolari.replace(",",".")),2)
            self.fiyat.setText(str(sonuc))
            
uygulama = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
uygulama.exec_()