[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/sEDn54aG)
# Tugas 3 - Klasifikasi Pendapatan dengan Decision Tree

| Nama              | NRP        |
|-------------------|------------|
| Mohammad Akmal Fayyazi            | 5054241045      |

## Deskripsi Tugas
Pada tugas ini, kita akan menggunakan **Adult Census Income Dataset**. Dataset bisa diakses melalui link berikut:\
🔗 https://www.kaggle.com/datasets/uciml/adult-census-income/data

Tujuan utama dari tugas ini adalah membangun model **Decision Tree** untuk memprediksi apakah pendapatan seseorang lebih dari $50K per tahun berdasarkan fitur demografis dan pekerjaan.

Langkah-langkah yang harus dilakukan antara lain:

1. Persiapan Dataset & Eksplorasi Awal
- Memuat dataset, melihat struktur data, tipe fitur (numerik atau kategorikal), dan distribusi label.

2. Preprocessing 
- Memproses data agar siap untuk digunakan dalam model, termasuk menangani missing value, encoding fitur kategorikal, dan normalisasi/standardisasi jika diperlukan.

3. Eksperimen Model 
- Bangun model **Decision Tree Classifier**, lalu latih menggunakan data training.
- Eksperimen dapat dilakukan dengan pemilihan subset fitur atau mengatur parameter Decision Tree (seperti `max_depth`, `min_samples_split`, dan lain sebagainya) untuk mengetahui pengaruhnya terhadap performa model.

4. Evaluasi Model
- Hitung metrik evaluasi seperti Accuracy, Precision, Recall, F1-Score, serta visualisasikan Confusion Matrix.
- Visualisasikan struktur pohon keputusan untuk interpretasi.

5. Analisis & Kesimpulan
- Membandingkan performa antar eksperimen parameter maupun fitur.
- Menentukan kombinasi parameter & fitur terbaik.
- Menarik kesimpulan mengenai fitur apa yang paling berpengaruh dalam memprediksi pendapatan serta seberapa baik Decision Tree bekerja pada dataset ini.
