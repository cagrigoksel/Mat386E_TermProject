# Daily Stock Buy-Sell Prediction Model

Bu proje, seçilen hisse senetleri ve endeksler için günlük al-sat kararlarını tahmin eden bir model geliştirmeyi amaçlamaktadır. Proje, veri çekme, işleme, analiz, modelleme ve veritabanına tahmin sonuçlarını yazma gibi bir dizi adımı içeren uçtan uca bir analitik akış sunar.

## İçindekiler
- [Proje Hakkında](#proje-hakkında)
- [Özellikler](#özellikler)
- [Klasör Yapısı](#klasör-yapısı)
- [Kurulum](#kurulum)
- [Kullanım Talimatları](#kullanım-talimatları)
- [Gereksinimler](#gereksinimler)
- [Proje Akışı](#proje-akışı)
- [Sonuçların Değerlendirilmesi](#sonuçların-değerlendirilmesi)

## Proje Hakkında

Bu proje, **Apple, NVIDIA, Microsoft** gibi en az bir hisse senedi ve **S&P 500** gibi bir endeks için günlük al-sat-tut kararlarını tahmin etmeye odaklanmaktadır. Modelin başarısı, başlangıçtaki sermaye ile model sonunda elde edilen kar/zarar oranlarına göre değerlendirilecektir.

## Özellikler

- **Yahoo Finance API** kullanılarak veri çekme
- **PySpark** ile büyük veri işleme ve ETL (Extract, Transform, Load) süreci
- **PostgreSQL** ile veritabanı işlemleri
- **Python & Jupyter Notebook** ile veri analizi, modelleme ve görselleştirme
- **Günlük Al-Sat-Tut Kararları** üreten zaman serisi ve makine öğrenimi modelleri

## Klasör Yapısı

```plaintext
Term_Project/
├── data/
│   ├── raw/                  # Ham veri dosyaları
│   ├── processed/            # İşlenmiş veri dosyaları
│   └── database/             # PostgreSQL veri yedekleri
│
├── notebooks/
│   ├── EDA_and_Feature_Engineering.ipynb    # Keşifsel veri analizi ve özellik mühendisliği
│   └── Modeling_and_Evaluation.ipynb        # Model eğitimi ve değerlendirme
│
├── src/
│   ├── etl/
│   │   ├── data_fetch.py                     # Veri çekme
│   │   ├── data_processing.py                # Veri işleme
│   │   └── load_to_postgres.py               # Veriyi PostgreSQL’e yükleme
│   │
│   ├── models/
│   │   ├── train_model.py                    # Model eğitimi
│   │   ├── evaluate_model.py                 # Model değerlendirme
│   │   └── prediction_pipeline.py            # Tahminlerin PostgreSQL’e yazılması
│   │
│   └── utils/
│       ├── data_utils.py                     # Veri ile ilgili yardımcı fonksiyonlar
│       ├── model_utils.py                    # Modelleme ile ilgili yardımcı fonksiyonlar
│       └── db_utils.py                       # Veritabanı ile ilgili yardımcı fonksiyonlar
│
├── reports/
│   ├── figures/                              # Grafik ve görseller
│   └── final_report.pdf                      # Nihai rapor
│
├── presentation/
│   └── final_presentation.pptx               # Proje sunumu
│
├── requirements.txt                          # Gerekli Python paketleri
├── README.md                                 # Proje açıklamaları ve kullanım talimatları
└── config.yaml                               # API anahtarları ve veritabanı ayarları

```

## Kurulum

Projeyi çalıştırmak için aşağıdaki adımları izleyin:

1. Projeyi klonlayın:

```plaintext
git clone <your-repo-link>
cd Term_Project
```

2. Gerekli Python kütüphanelerini yükleyin:

```plaintext
pip install -r requirements.txt
```


3. PostgreSQL veritabanınızı ayarlayın ve config.yaml dosyasına bağlantı bilgilerini ekleyin.


## Kullanım Talimatları

### 1. Veri Çekme ve İşleme

```plaintext 
src/etl/data_fetch.py
``` 
scripti ile Yahoo Finance API'den veri çekin ve 

```plaintext 
src/etl/load_to_postgres.py 
``` 
ile PostgreSQL'e yükleyin.

### 2. Veri Analizi ve Özellik Mühendisliği

```plaintext 
notebooks/EDA_and_Feature_Engineering.ipynb
``` 
dosyasını kullanarak veri analizi ve özellik çıkarma işlemlerini yapın.

### 3. Model Eğitimi ve Değerlendirme

```plaintext 
notebooks/Modeling_and_Evaluation.ipynb 
```
dosyasındaki yönergeleri izleyerek modelleri eğitin, değerlendirin ve en iyi modeli seçin.

### 4. Tahmin Ve Sonuçları Kaydetme

```plaintext 
src/models/prediction_pipeline.py 
```
scripti ile seçilen modelle tahmin yapın ve sonuçları PostgreSQL’e kaydedin.

## Gereksinimler
Python 3.9 ve üzeri

PostgreSQL veritabanı

PySpark, yfinance, Prophet gibi Python kütüphaneleri (detaylar requirements.txt dosyasında)


## Proje Akışı
1. Veri Çekme (ETL): Ham veriyi çekip veritabanına yükleyin.
2. EDA ve Özellik Mühendisliği: Veriyi analiz edip modelleme için anlamlı özellikler çıkarın.
3. Modelleme: Farklı modellerle deney yapıp en başarılı modeli seçin.
4. Tahmin ve Kayıt: Günlük al-sat kararlarını veritabanına yazacak bir tahmin hattı kurun.

## Sonuçların Değerlendirilmesi
Başarı oranı, başlangıç sermayesinden elde edilen getiriye göre hesaplanacaktır.

ROI, Net Profit, Win Rate (Accuracy) ve Beta metriklerini kullanarak performans değerlendirmesi yapabilirsiniz.

