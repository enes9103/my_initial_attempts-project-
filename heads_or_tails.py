from random import choice
import random
yazi_gelen = 0
tura_gelen = 0
para_yuzeyi = ["Tura", "Yazi"]
atilacak_para = int(input("Kaç kez para atmak istiyorsunuz?: "))
while atilacak_para > 0:
    para_ustu = random.choice(para_yuzeyi)
    if para_ustu == "Tura":
        tura_gelen += 1
        print("Tura Geldi!")
    else:
        yazi_gelen += 1
        print("Yazı Geldi!")
    atilacak_para -= 1
print("Tura Sayısı : {}, Yazi Sayisi : {}".format(yazi_gelen,tura_gelen))
