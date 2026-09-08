# Python: Eszamanlilik Denemeleri

Python'da ayni isi uc farkli yolla yapmanin suresini karsilastiran kucuk bir
calisma. Kripto para fiyatlarini donduren bir JSON adresine cok sayida istek
atilip gecen sure olculuyor.

## Dosyalar

| Dosya | Ne yapiyor |
|---|---|
| `main.py` | Tek bir istekle kripto listesini cekiyor, kullanicinin girdigi para biriminin fiyatini yaziyor |
| `asyncandthreading.py` | Ayni istekleri once sirayla (senkron), sonra `threading` ile atip gecen sureyi olcuyor |

Amac ikisi arasindaki farki sayiyla gormek: senkron surum her istegin
bitmesini tek tek bekler, `threading` surumu beklemeleri ust uste bindirir.
Olcum icin kasitli olarak 3 saniye geciken bir test adresi kullaniliyor.

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
