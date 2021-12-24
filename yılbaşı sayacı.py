import datetime
import time
while 1:
    now = datetime.datetime.now()
    kalan_zaman = datetime.datetime(now.year + 1, 1, 1) - now
    saat= kalan_zaman.seconds//3600
    dakika = (kalan_zaman.seconds%3600) //60
    saniye = (kalan_zaman.seconds%3600) %60

    print("Yeni yıla kalan zaman: " + str(kalan_zaman.days) + " gün,"+ str(saat) + " saat,"+ str(dakika) + " dakika," + str(saniye) + " saniye.", end = "\r")
    time.sleep(1)
