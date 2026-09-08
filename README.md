# Python: Eszamanlilik Denemeleri

Python'da ayni isi uc farkli yolla yapmanin suresini karsilastiran kucuk bir
calisma. Kripto para fiyatlarini donduren bir JSON adresine cok sayida istek
atilip gecen sure olculuyor.

## Dosyalar

| Dosya | Ne yapiyor |
|---|---|
| `main.py` | Tek bir istekle kripto listesini cekiyor, kullanicinin girdigi para biriminin fiyatini yaziyor |
| `asyncandthreading.py` | Ayni istekleri sirayla (senkron), `threading` ile ve `asyncio` ile atip surelerini karsilastiriyor |

Amac ucunun arasindaki farki sayiyla gormek: senkron surum istekleri tek tek
bekler, digerleri beklemeyi ust uste bindirir.

## Calistirma

```bash
pip install requests aiohttp
python main.py
```

## Bilinen sorun

`asyncandthreading.py` su an **calismiyor**: 5. satirdaki `import aiohttpgit`
bir yazim hatasi, dogrusu `import aiohttp`. Duzeltilmeden dosya
`ModuleNotFoundError` veriyor. Kod ogrenme surecinin kaydi olarak oldugu gibi
birakildi.
