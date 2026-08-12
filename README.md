#  Alışveriş Simülasyonu

Python kullanılarak geliştirilmiş basit bir **alışveriş simülasyonu** uygulamasıdır.

Proje; yönetici ve kullanıcı girişleri, ürün yönetimi, ürün listeleme, sepete ürün ekleme, toplam fiyat hesaplama ve sipariş onaylama gibi temel alışveriş işlemlerini terminal üzerinden gerçekleştirmektedir.

Bu proje, Python'da temel programlama yapılarının ve veri yapılarının pratik edilmesi amacıyla geliştirilmiştir.

---

##  Proje Özellikleri

###  Yönetici Paneli

Yönetici, sisteme kullanıcı adı ve parola ile giriş yapabilir.

Yönetici panelinde:

- Yeni ürün ekleme
- Ürünün fiyatını belirleme
- Birden fazla ürün ekleme
- Ürün ekleme işlemini sonlandırma

işlemleri gerçekleştirilebilir.

Yönetici aynı zamanda panelden çıkış yapabilir.

---

### 👤 Kullanıcı Paneli

Kullanıcı, sisteme kullanıcı adı ve parolası ile giriş yapabilir.

Kullanıcı panelinde:

- Sistemde bulunan ürünleri görüntüleme
- Ürün seçme
- Ürünü sepete ekleme
- Birden fazla ürün ekleme
- Sepet toplamını görüntüleme
- Siparişi onaylama
- Siparişi iptal etme

işlemleri gerçekleştirilebilir.

---

##  Alışveriş Süreci

Programın temel çalışma mantığı şu şekildedir:

```text
Program Başlangıcı
       │
       ▼
Giriş Yöntemi Seç
       │
   ┌───┴────┐
   ▼        ▼
Yönetici  Kullanıcı
   │        │
   ▼        ▼
Ürün Ekle  Ürünleri Görüntüle
   │        │
   │        ▼
   │     Ürün Seç
   │        │
   │        ▼
   │    Sepete Ekle
   │        │
   │        ▼
   │   Başka Ürün?
   │      Evet │ Hayır
   │        │     │
   │        └─────┘
   │              ▼
   │        Sepet Toplamı
   │              │
   │              ▼
   │        Sipariş Onayı
   │
   └──────────────┐
                  ▼
             Giriş Menüsü
