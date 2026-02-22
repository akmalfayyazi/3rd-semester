[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/D_GoKxZj)
# Tugas 7 – Clustering: DBSCAN & BIRCH

| Nama              | NRP        |
|-------------------|------------|
| Mohammad Akmal Fayyazi            | 5054241045      |

---

## Deskripsi Tugas

Pada tugas ini, kita akan menggunakan **Give Me Some Credit** yang dapat diakses melalui link berikut:  
🔗 [Give Me Some Credit Dataset – Kaggle](https://www.kaggle.com/competitions/GiveMeSomeCredit/data?select=cs-training.csv)

Tujuan utama dari tugas ini adalah melakukan **unsupervised learning (clustering)** menggunakan dua metode:

- **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**
- **BIRCH (Balanced Iterative Reducing and Clustering using Hierarchies)**

---

## 1. Persiapan Dataset & Eksplorasi Awal

Langkah pertama adalah memuat dataset dan melakukan eksplorasi awal terhadap struktur datanya.

- Memahami struktur data (kolom, tipe data, dan jumlah record)
- Mengetahui apakah ada nilai yang hilang
- Mengamati distribusi awal fitur

---

## 2. Preprocessing Data

Sebelum melakukan clustering, lakukan preprocessing agar hasil lebih optimal:

- Tangani missing values (hapus atau imputasi)
- Encode fitur kategorikal menjadi numerik (gunakan **One-Hot Encoding** atau **Label Encoding**)
- Normalisasi fitur numerik menggunakan **StandardScaler** atau **MinMaxScaler** agar semua fitur berada pada skala yang sama

---

## 3. DBSCAN Clustering

- Gunakan algoritma **DBSCAN** dari `sklearn.cluster`
- Tentukan parameter penting:
  - `eps` (radius tetangga)
  - `min_samples` (jumlah minimum titik dalam satu cluster)
- Gunakan **k-distance graph** untuk membantu menentukan nilai `eps` yang optimal
- Tampilkan hasil clustering:
  - Jumlah cluster yang terbentuk (tidak termasuk noise)
  - Jumlah data yang dianggap noise (`label = -1`)

---

## 4. BIRCH Clustering

- Gunakan algoritma **BIRCH** dari `sklearn.cluster`
- Tentukan parameter:
  - `threshold`
  - `n_clusters`
- Lakukan clustering pada dataset yang sudah dinormalisasi
- Tampilkan hasil clustering:
  - Jumlah cluster yang terbentuk
  - Distribusi data pada tiap cluster

---

## 5. Visualisasi Hasil Clustering

- Visualisasikan hasil clustering **DBSCAN** dan **BIRCH** secara terpisah.
- Gunakan **PCA (Principal Component Analysis)** untuk menurunkan dimensi ke 2D.
- Berikan **scatter plot** dengan warna berbeda untuk setiap cluster.

---

## 6. Analisis

Berikan analisis dan interpretasi berdasarkan hasil clustering yang diperoleh:

- Bagaimana pola yang terbentuk dari masing-masing metode?
- Apakah DBSCAN dan BIRCH menghasilkan jumlah cluster yang berbeda?
- Metode mana yang lebih baik untuk dataset ini? Jelaskan alasannya.
- Apakah terdapat noise atau outlier yang signifikan pada hasil DBSCAN?
- Berikan kesimpulan umum akhir

---
