admin_sifre = "admin1234"
admin_ka = "admin"

kullanici_sifre = "kullanici1234"
kullanici_ka = "kullanici"

sepet = {}
ürün = {}

while True:
    
    giris = int(input("Bir Giriş Yöntemi Seçin \n1 - Yönetici Girişi \n2 - Kullanıcı Girişi \n3 - Programı Sonlandır\n"))

    if giris == 1:
        giris_admin_ka = input("Yönetici Kullanıcı Adınızı Girin: ")
        giris_admin_sifre = input("Yönetici Parolanızı Girin: ")

        if giris_admin_ka == admin_ka and giris_admin_sifre == admin_sifre:
            print("----- YÖNETİCİ PANELİNE HOŞGELDİNİZ -----")
            admin_islem = int(input("Yapmak İstediğiniz İşlemi Seçin: \n1 - Ürün Ekle \n2 - Çıkış Yap\n"))

            if admin_islem == 1:
                while True:
                    ürün_adi = input("Eklemek İstediğiniz Ürünün Adını Girin: ")
                    ürün_fiyat = int(input("Ürünün Fiyatını Girin: "))

                    ürün[ürün_adi] = ürün_fiyat

                    print("Ürün Başarıyla Eklendi🎉")

                    devam = input("Ürün Eklemeye Devam Etmek İster Misiniz? E/H\n")

                    if devam.lower()== "h":
                        break

            elif admin_islem == 2:
                print("--- ÇIKIŞ YAPILDI ---")
                exit()

        else:
            print("Kullanıcı Adı veya Parola Hatalı!")

    elif giris == 2:
        giris_kullanici_ka = input("Kullanıcı Adını Girin: ")
        giris_kullanici_sifre = input("Kullanıcı Parolasını Girin: ")

        if giris_kullanici_ka == kullanici_ka and giris_kullanici_sifre == kullanici_sifre:
            print("----- ANASAYFAYA -----")
            kullanici_islem = int(input("Yapmak İstediğiniz İşlemi Seçin: \n1 - Ürün Listesi \n2 - Çıkış Yap\n"))

            if kullanici_islem == 1:
                while True:
                    for ürün_adi, ürün_fiyat in ürün.items():
                        print(f"{ürün_adi} -- {ürün_fiyat} TL")

                    ürün_secim = input("Sepete Eklemek İstediğiniz Ürünü Seçin: ")

                    if ürün_secim in ürün:
                        sepet[ürün_secim] = ürün[ürün_secim]
                        print("Ürün Sepete Eklendi.")

                    else:
                        print("Böyle Bir Ürün Bulunamadı!")

                    devam = input("Başka Ürün Eklemek İstiyor Musunuz? E/H\n")

                    if devam.lower() == "h":
                        break

                    

                toplam = sum(sepet.values())
                print(f"Sepet Toplamı: {toplam} TL")

                onay = input("Sepeti Onaylamak İstiyor Musunuz? E/H\n")
                if onay.lower() == "e":
                    print("Sepetiniz Onaylandı 🎉")
                    break
                else:
                    print("Sepetiniz İptal Edildi!")
                    break

            elif kullanici_islem == 2:
                print("--- ÇIKIŞ YAPILDI ---")
                exit()

        else:
            print("Kullanıcı Adı veya Parola Hatalı!")
    elif giris == 3:
        print("--- PROGRAM KAPATILDI---")
        break