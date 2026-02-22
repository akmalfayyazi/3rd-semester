[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Cyjdl0AQ)
# Tugas 8 – Deep Learning (CNN)

| Nama              | NRP        |
|-------------------|------------|
| Mohammad Akmal Fayyazi            | 5054241045      |

---

## Link Deployment

## Deskripsi Tugas

Kali ini, kita akan menggunakan dataset **RealWaste** (gambar limbah nyata) yang dapat diakses via tautan berikut:  
🔗 [RealWaste – Kaggle / UCI / GitHub](https://www.kaggle.com/datasets/joebeachcapital/realwaste/data)  

---

## Langkah-langkah

### 1. Persiapan Dataset & Eksplorasi Awal
- Muat dataset dan lihat struktur folder/gambar.
- Lihat jumlah gambar per kategori (label), ukuran gambar, tipe file.
- Cek apakah terdapat kategori yang sangat sedikit (imbalance).
- Visualisasi beberapa contoh gambar dari tiap kategori.

### 2. Preprocessing Data
- Ubah ukuran (resize) gambar agar seragam (misalnya 224×224 atau 256×256).
- Lakukan augmentasi data (flip, rotate, zoom, shear) untuk mengatasi overfitting dan ketidakseimbangan.
- Normalisasi piksel gambar (misalnya ke rentang 0-1 atau mean subtraction).
- Encode label kategori (misalnya one-hot encoding jika multi-kelas).

### 3. Membangun Model CNN
- Desain model CNN
- Tentukan beberapa hyperparameter: jumlah epoch, batch size, learning rate, optimizer (misalnya Adam), loss function (misalnya categorical crossentropy) dan metrik (accuracy, precision/recall).

### 4. Training dan Validasi
- Jalankan training model pada data training.
- Monitor metrik pada data validation: accuracy, loss; juga lihat evolusi tiap epoch (plot learning curve).
- Perhatikan apakah terjadi overfitting atau underfitting.
- Gunakan teknik seperti early stopping, model checkpointing.

### 5. Evaluasi pada Data Test & Analisis
- Evaluasi model terbaik pada data test yang belum pernah dilihat.
- Buat confusion matrix, classification report (precision, recall, F1-score) untuk tiap kategori limbah.
- Visualisasikan beberapa prediksi: gambar asli + label sebenarnya + label prediksi + apakah benar/salah.

### 6. Visualisasi & Interpretabilitas
- Jalankan visualisasi hasil, seperti:
- Learning curves (accuracy & loss vs epoch)
- Confusion matrix heatmap
- (Opsional) Visualisasikan contoh gambar yang model salah klasifikasi dan analisis kenapa.

### 7. Analisis
Tuliskan analisis berdasarkan hasil yang diperoleh:
- Kategori limbah mana yang paling sulit diklasifikasi dan kenapa (misalnya tumpang-tindih visual, deformasi objek limbah).  
- Apakah terjadi overfitting/underfitting? Jika ya, bagaimana sebaiknya diperbaiki?  
- Apakah data imbalance mempengaruhi hasil? Apakah perlu teknik seperti class weighting atau oversampling?  
- Bandingkan jika menggunakan arsitektur sederhana vs penggunaan pre-trained model.  
- Kesimpulan akhir

---

## Tambahan (Opsional)
- Eksperimen dengan beberapa arsitektur berbeda (misalnya ResNet50, EfficientNet, MobileNetV2) dan bandingkan performanya.
- Uji pengaruh ukuran gambar (misalnya 128×128 vs 224×224) terhadap akurasi dan waktu training.
- Uji pengaruh teknik augmentasi berbeda (misalnya heavy vs light augmentation).
- Uji penggunaan teknik class‐imbalance seperti oversampling Minoritas, undersampling Mayoritas, atau cost-sensitive learning.

---