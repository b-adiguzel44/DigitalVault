# region Imported Modules/Packages
from time import *              # time modülünün bütün metot,sınıflarını dahil ettim
import random                   # random modülünü projeme dahil ettim
import os                       # işletim sistemine göre yapılacak işlemler için os modülünü projeme dahil ettim
# endregion

# region Description
# 10 haneli rastgele 0-9 rakamlarından oluşan bir şifre üretir, otomatikmen dijital kasanın şifresini
# girmeye çalışır. Yanlış girdiğinde dijital kasa 30 saniye boyunca kendisini kitler. Kitleme bittikten sonra
# tekrar 10 haneli rastgele bir şifre üretip şifreyi bulana kadar girmeye çalışır
# endregion

# region Rules
# Dijital bir kasanın açılabilmesi için gerekli olan şifrelerin bir listesini oluşturan ve oluşturulan liste
# ile bu kasanın açılması için gereken zamanın hesaplayabilen bir yazılım çözümünün oluşturulmasını içermektedir.

# Dijital kasa ile ilgili detaylar aşağıda yer almaktadır.
#
# Dijital kasanın şifresi rakamlardan oluşan 10 haneli bir seridir. K
# asanın şifresi belirlenirken aşağıdaki kurallara uyulduğu bilinmektedir.
#
# -Şifrenin ilk hanesi şifre üzerinde kaç tane sıfır rakamının kullanıldığını belirtmektedir.
# -Şifrenin ikinci hanesi şifre üzerinde kaç tane bir rakamının kullanıldığını belirtmektedir.
# -Şifrenin üçüncü hanesi şifre üzerinde kaç tane iki rakamının kullanıldığını belirtmektedir.
# -Şifrenin dördüncü hanesi şifre üzerinde kaç tane üç rakamının kullanıldığını belirtmektedir.
# -Şifrenin beşinci hanesi şifre üzerinde kaç tane dört rakamının kullanıldığını belirtmektedir.
# -Şifrenin altıncı hanesi şifre üzerinde kaç tane beş rakamının kullanıldığını belirtmektedir.
# -Şifrenin yedinci hanesi şifre üzerinde kaç tane altı rakamının kullanıldığını belirtmektedir.
# -Şifrenin sekizinci hanesi şifre üzerinde kaç tane yedi rakamının kullanıldığını belirtmektedir.
# -Şifrenin dokuzuncu hanesi şifre üzerinde kaç tane sekiz rakamının kullanıldığını belirtmektedir.
# -Şifrenin onuncu hanesi şifre üzerinde kaç tane dokuz rakamının kullanıldığını belirtmektedir.
#
# Dijital kasanın üzerinde yer alan tuş takımı rastgele şifre denemelerini önlemek için özel bir kitleme donanımına
# sahiptir.
# Kasanın sahip olduğu bu donanım hatalı şifre girildiğinde tuş takımını otuz saniyeliğine kitleyerek kullanılmasını
# engellemektedir.

# endregion

# region Functions


def terminal_clean():
    '''İşletim sistemine göre terminaldeki ekranı temizler'''
    if os.name == 'nt':
        os.system('cls')   # Terminal ekranını temizler (Windows için)
    elif os.name == 'posix':
        os.system('clear')  # Terminal ekranını temizler (Linux için)


def cooldown(msg, sec=30):
    '''Şifre doğru bilinmez veya hatalı girilir ise programı 30 saniye bekletir'''
    if sec == 0:  # Bekleme süresinin bittiği zaman
        return
    else:
        print(msg)                              # Mesaj bilgisi
        print(f"{sec} saniye bekleyiniz")       # Kaç saniye kaldı
        sleep(1)                                # Programı 1 saniye beklet
        terminal_clean()                        # Hangi işletim sisteminde çalışıyor ise ilgili komutları çalıştır
        cooldown(msg, sec - 1)                  # Bekletme devam ediyor


def generate_a_passw():
    '''Dijital kasa için açılabilecek şifreyi oluşturmaya çalışır'''
    def is_this_one(num):
        '''Gelen 10 haneli şifrenin istenilen dijital kasanın açabileceği şifre olup olmadığını belirler'''
        bool_list = [False for i in range(10)]

        # Her hanedeki rakamdan kaç adet tutalacağını belirlemek için hazırladığımız bir dict
        digit_dict = {
            '0': 0,
            '1': 0,
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
            '7': 0,
            '8': 0,
            '9': 0}

        # Gelen şifrenin her hanesinden kaç adet bulduğunu bulup dictionary de topluyoruz
        for new_digit in num:
            if new_digit in digit_dict:
                digit_dict[new_digit] += 1

        for x in digit_dict:
            # İki durumu kontrol edicez
            # İlgili hanedeki rakam, şifredeki kaç adet olduğuna eşit mi?
            # Kendi hanesindeki rakam, şifredeki kendi rakamının adetine eşit mi?
            if digit_dict[x] == num.count(x) and digit_dict[num[int(x)]] == digit_dict[x]:
                bool_list[int(x)] = True

        # Bool listesi farklı olmayacak, olursa istenilen şifre değildir
        if not any(bool_list):
            return True
        else:
            return False

    # 10 haneli rastgele 0-9 arası şifre üretimi
    passw = [random.randint(0, 9) for x in range(10)]

    # 10 haneli şifreyi bir string ifadesinde toplamı
    digits = ''
    for k in passw:
        digits += str(k)

    # rakamlar toplamı 10 ve dijital kasa kuralına uyuyor mu? Kontrol ediliyor
    if sum(passw) == 10 and is_this_one(digits):
        return digits           # string bir değer dönücektir
    else:
        return None


# endregion


if __name__ == "__main__":

    start_timer = False                 # Süremizi başlatmak için kullanacağımız bool değişkeni
    list_of_passw = {'6210001000'}      # Bu şifre dışında başka bir şifre kurala uymamaktadır.
    terminal_clean()

    print('Şifre kırma işlemi 3 saniye içinde başlayacak...')
    sleep(3)
    while True:
            passw = generate_a_passw()      # Rastgele 10 haneli bir şifre üret
            if not start_timer:             # Süreyi başlat
                timer = time()
                start_timer = True     # Bu bloğa bir kere girecek
            terminal_clean()           # Terminal ekranı temizleme

            # Eğer üretilen şifre, dijital kasanın şifresine eşit değil ise bloklama yap
            if passw == None:
                time_passed = round(time() - timer, 2)
                cooldown(f'Şifre yanlış girildi - Geçen süre : {str( time_passed  ) }s')
            else:
                total_time = str(round(time() - timer,2))           # Geçen süreyi hesapla
                print("Şifre çözülmüştür")
                print("Geçen zaman", total_time + "s")
                exit(0)