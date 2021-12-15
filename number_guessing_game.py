import time
import random
# Gerekli modülleri çağırdık.

def sayı_al():
    sayı_tahmin = int(input("Bir sayı giriniz? "))
    return sayı_tahmin
# Kullanıcıdan sayı alacağımız bir fonksiyon tanımladık.

def oyun_baslat():
    print("""
        *** SAYI TAHMİN OYUNUNA HOŞ GELDİNİZ ***
    """)
    dogru_sayı = random.randint(1,100)

# Random modülünün randint fonksiyonu ile 1 ile 100 arasında bulunan rastgele bir tam sayı aldık.
    while True:
        sayı_tahmin = sayı_al()
        print("Kontrol ediliyor...")
        time.sleep(1)
# Kullanıcıdan sayıyı aldıktan sonra programı 1 saniye durdurduk.

        if dogru_sayı < sayı_tahmin:
            print("Biraz aşağı gelin")
        elif dogru_sayı > sayı_tahmin:
            print("Biraz yukarı gelin")
        else:
            print("\n *** SAYI DOĞRU! ***")
            break
# Aldığımız sayıya göre gerekli işlemleri yaptık.

oyun_baslat()