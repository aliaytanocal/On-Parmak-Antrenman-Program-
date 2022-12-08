#Bu kısımda gerekli kütüphaneleri içe aktarıyoruz.
import random
import time

#Bu kısımda on parmak yazı için gerekli karakterleri tanımlıyoruz.
harfler = "abcdefghijklmnopqrstuvwxyz"
rakamlar = "0123456789"
on_parmak_yazi = harfler + rakamlar

#Bu kısımda antreman süresini belirtiyoruz.
antreman_suresi = 60

#Bu kısımda antreman için bir döngü oluşturuyoruz.
#Bu döngü süresince rastgele bir karakter ekrana yazdırılacaktır.
#Döngü süresi bittiğinde antreman sona erecektir.
for i in range(antreman_suresi):
    #Bu kısımda rastgele bir karakter seçiliyor ve ekrana yazdırılıyor.
    print(random.choice(on_parmak_yazi), end="")
    #Bu kısımda bir süre bekleniyor.
    #Bu sayede karakterler arka arkaya yazdırılmış olacaktır.
    time.sleep(0.1)

#Bu kısımda antreman bittikten sonra bir mesaj yazdırılıyor.
print("\nAntreman bitti!")
