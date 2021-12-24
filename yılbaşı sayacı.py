import datetime
import time
while 1:
    now = datetime.datetime.now()
    kalan_zaman = datetime.datetime(now.year + 1, 1, 1) - now #sonraki yılın ilk gününden mevcut tarihi çıkar
    saat= kalan_zaman.seconds//3600 #kalan zamanı saniye cinsinden alıp 3600'e kalansız bölerek kalan saati bul
    dakika = (kalan_zaman.seconds%3600) //60 #kalan zamanın 3600'e bölümünden kalanı 60'a kalansız bölerek dakikayı bul(yani saate çevirdikten sonra kalan saniyeleri 60'a böl)
    saniye = (kalan_zaman.seconds%3600) %60  #kalan zamanın 3600'e bölümünden kalanın 60'a bölümünden kalanı bul(yani kalan saniye cinsinden süreyi saat ve dakikaya çevirdikten sonra kalan)

    print("Yeni yıla kalan zaman: " + str(kalan_zaman.days) + " gün,"+ str(saat) + " saat,"+ str(dakika) + " dakika," + str(saniye) + " saniye.", end = "\r") #kalan süreyi gün, saat,dakika olarak yazdır
    time.sleep(1) #1 saniye aralıklı döngüler halinde sürekli tekrarla
