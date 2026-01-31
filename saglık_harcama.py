import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Veri
data = {
    "yil": [2015,2016,2017,2018,2019,2020,2021,2022],
    "toplam_harcama_milyar_tl": [105.4,118.9,141.3,166.8,201.5,252.4,356.7,612.9],
    "kamu_harcamasi_milyar_tl": [78.2,90.1,107.6,124.2,153.8,199.6,278.4,470.5],
    "ozel_harcama_milyar_tl": [27.2,28.8,33.7,42.6,47.7,52.8,78.3,142.4],
    "kisi_basi_harcama_tl": [1350,1490,1735,2040,2450,3020,4180,7200],
    "gsyh_orani": [4.6,4.7,4.5,4.4,4.7,5.0,4.9,4.8]
}

df = pd.DataFrame(data)

# 2️⃣ Oran ve Yıllık Artış Hesapları
df["kamu_orani"] = df["kamu_harcamasi_milyar_tl"] / df["toplam_harcama_milyar_tl"] * 100
df["ozel_orani"] = df["ozel_harcama_milyar_tl"] / df["toplam_harcama_milyar_tl"] * 100
df["yillik_artis_orani"] = df["toplam_harcama_milyar_tl"].pct_change() * 100

# 3️⃣ Dashboard tarzı grafikler
fig, axes = plt.subplots(2, 2, figsize=(14,10))
fig.suptitle("Türkiye Sağlık Harcamaları Analizi (2015–2022)", fontsize=16)

# 🔹 Toplam Harcama
axes[0,0].plot(df["yil"], df["toplam_harcama_milyar_tl"], marker='o', color='blue')
axes[0,0].set_title("Toplam Sağlık Harcamaları (Milyar TL)")
axes[0,0].set_xlabel("Yıl")
axes[0,0].set_ylabel("Milyar TL")
axes[0,0].grid(True)

# 🔹 Kamu ve Özel Oranları
axes[0,1].plot(df["yil"], df["kamu_orani"], marker='o', label="Kamu %")
axes[0,1].plot(df["yil"], df["ozel_orani"], marker='o', label="Özel %")
axes[0,1].set_title("Kamu ve Özel Harcama Oranları")
axes[0,1].set_xlabel("Yıl")
axes[0,1].set_ylabel("Oran (%)")
axes[0,1].legend()
axes[0,1].grid(True)

# 🔹 Kişi Başı Harcama
axes[1,0].plot(df["yil"], df["kisi_basi_harcama_tl"], marker='o', color='green')
axes[1,0].set_title("Kişi Başı Sağlık Harcaması (TL)")
axes[1,0].set_xlabel("Yıl")
axes[1,0].set_ylabel("TL")
axes[1,0].grid(True)

# 🔹 Yıllık Artış Oranı
axes[1,1].bar(df["yil"], df["yillik_artis_orani"], color='orange')
axes[1,1].set_title("Toplam Harcama Yıllık Artış Oranı (%)")
axes[1,1].set_xlabel("Yıl")
axes[1,1].set_ylabel("%")
axes[1,1].grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])  # Başlık üstte sıkışmasın
plt.show()  # PyCharm'da ekranda göster

# İstersen kaydetmek için:
fig.savefig("saglik_harcamalari_dashboard.png")
