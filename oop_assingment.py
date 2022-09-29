'''Öğrenci Ad Soyad=ESAT CİHAN ÖZGÜLTEKİN
Öğrenci No=20217170028
Bölüm=Bilgisayar Mühendisliği
Sınıf=1.grup'''


class urunler:
    urun_adi=""
    urun_alis_fiyati=0
    urun_otv_orani=0
    urun_kdv_orani=0

    def _init_(self,urun_adi, urun_alis_fiyati, urun_otv_orani, urun_kdv_orani):
        self.urun_adi=urun_adi
        self.urun_alis_fiyati=urun_alis_fiyati
        self.urun_otv_orani=urun_otv_orani
        self.urun_kdv_orani=urun_kdv_orani

   
    def  urun_satis_fiyati(self,kar_orani) :
        toplam=0
        toplam=self.urun_alis_fiyati+(self.urun_alis_fiyati*kar_orani)
        toplam=toplam +(toplam*self.urun_otv_orani)
        toplam=toplam+(toplam*self.urun_kdv_orani)
        return toplam
        
    
def sepet_fiyati(kar_orani):
    '''
    Fonksiyon urunlerin toplam fiyatini geri dönüş değeri olarak dondurmelidir. (5 puan)
    Sadece #------**------ işareti ile belirtilen 
    kısımlar arasını değiştiriniz. 

    toplam değişkenini doldurmanız beklenmektedir.
    '''
    ekmek=urunler('ekmek',1,0.20,0.12)
    patates=urunler('patates',2,0.16,0.18)
    elma=urunler('elma',3,0.11,0.22)
    un=urunler('un',4,0.17,0.05)
    yumurta=urunler('yumurta',5,0.30,0.19)
    toplam=0   
    #-------**-----------
    toplam+=ekmek.urun_satis_fiyati(kar_orani)
    toplam+=patates.urun_satis_fiyati(kar_orani)
    toplam+=elma.urun_satis_fiyati(kar_orani)
    toplam+=un.urun_satis_fiyati(kar_orani)
    toplam+=yumurta.urun_satis_fiyati(kar_orani)
    #-------**-----------
    return toplam


def odev_test():
    sepet_toplam = sepet_fiyati(0.15)
    if sepet_toplam==23.91218:
        print("doğru")
    else:
        print("yanlış")


#bu test methodunu kullanarak yazdığınız kodu test edebilirsiniz
odev_test()
