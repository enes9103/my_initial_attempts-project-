from time import sleep as bekle

print(" --- BANKAYA HOŞ GELDİNİZ --- \n")
secim = input("Kart sokmak için 's', Ayrılmak için 'l' yazınız: ")
mevcut_para = 2300
# İlk satırda yaptığımız işlemi ilerleyen derslerde göreceğiz o yüzden umursamayın. Kullanıcıdan gerekli seçimi aldık ve mevcut parayı belirledik.

if secim == "s":
    print("kartınız okunuyor")
    for i in range(3):
        print(".")
        bekle(1)
# Kartınız okunuyor yazdırdıktan sonra for döngüsü üç tur döndü ve her turda bir kere  '.'  yazdırıp bir saniya bekledi. (bekle isimli fonksiyonu ilk satırda yaptığımız işlemle dahil ettik)
    while True:
        islem = int(input("""
        
            *******************************
            Para Çekmek İçin ------------ 1
            Para Yatırmak İçin ---------- 2
            Hesap Durumu İçin ----------- 3
            Çıkmak için ----------------- 4
            *******************************
        istediğiniz işlemin numarasını yazın: 
        """))
# Bir sonsuz döngü tanımladık ve kullanıcıdan istediği işlemi aldık

        if islem == 1:
            miktar = int(input(f"Kaç lira çekmek istersiniz (mevcut bakiye = {mevcut_para} : )"))
            if miktar > mevcut_para:
                print("Bu kadar paranız yok :( ")
            else:
                print("işlem yapılıyor")
                for i in range(3):
                    print(".")
                    bekle(1)
                print("işlem başarılı")
                mevcut_para -= miktar
# Kullanıcı para çekmek istediğinde önce istediği miktarı aldık, istediği miktar parasından fazla ise ekrana üzücü haberi yazdırdık. Eğer parası yetiyorsa işlem yapılıyor yazdırıp tekrar yukarıdaki bekleme işlemini yaptırdık. Son olarak işlem başarılı yazdırıp mevcut_para'dan miktar'ı çıkardık.

        if islem == 2:
            miktar = int(input(f"Kaç lira yatırmak istersiniz (mevcut bakiye = {mevcut_para} : )"))
            print("işlem yapılıyor")
            for i in range(3):
                print(".")
                bekle(1)
            print("işlem başarılı")
            mevcut_para += miktar
# Aynı işlemi para yatırmak için de yaptık. Tek fark parayı azaltmak yerine arttırmak ve miktar'ın mevcut_para'dan çok olma durumunu kontrol etmemek oldu.

        if islem == 3:
            print(f"""
                ***********************
                Ad ------ Mert
                Soyad --- Sis
                IBAN ---- xxxxxxxxxxx
                Para ---- {mevcut_para}
                ***********************           
            """)
# Kullanıcı hesap bilgilerini istediğinde ekrana yazdırdık.
        
        if islem == 4:
            print("çıkış yapılıyor")
            for i in range(3):
                print(".")
                bekle(1)
            print("\n *** GÖRÜŞMEK ÜZERE *** ")
            break