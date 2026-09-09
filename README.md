# Python: Eszamanlilik Denemeleri

Python'da ayni isi uc farkli yolla yapmanin suresini karsilastiran kucuk bir
calisma. Kripto para fiyatlarini donduren bir JSON adresine cok sayida istek
atilip gecen sure olculuyor.

## Dosyalar

| Dosya | Ne yapiyor |
|---|---|
| `main.py` | Tek bir istekle kripto listesini cekiyor, kullanicinin girdigi para biriminin fiyatini yaziyor |
| `asyncandthreading.py` | Ayni istegi hem sirayla (senkron) hem `threading` ile atan iki fonksiyon; gecen sureyi olcuyor |

Amac ikisi arasindaki farki sayiyla gormek: senkron surum her istegin
bitmesini tek tek bekler, `threading` surumu beklemeleri ust uste bindirir.
Olcum icin kasitli olarak 3 saniye geciken bir test adresi kullaniliyor.

Dosyanin sonunda `get_data_sync(urls)` cagrisi **yorum satirinda**; oldugu
gibi calistirilinca yalnizca `threading` surumu olcum veriyor. Karsilastirma
icin o satirin yorumdan cikarilmasi gerekiyor. Ayrica `urls` listesinde tek
adres var; fark ancak birden fazla adres eklenince belirginlesiyor.

## Calistirma

```bash
pip install requests
python main.py                 # kripto fiyati sorgulama
python asyncandthreading.py    # sure karsilastirmasi
```

## Not

Dosya adi `asyncandthreading` olsa da **asyncio bolumu hic yazilmamis**;
yalnizca senkron ve `threading` surumleri var. Karsilastirmanin ucuncu
ayagi eksik.
