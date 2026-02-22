# Tugas 4 - Klasifikasi Risiko Stroke dengan SVM dan ANN

| Nama              | NRP        |
|-------------------|------------|
| Mohammad Akmal Fayyazi            | 5054241045      |

## Deskripsi Tugas
Pada tugas ini, kita akan menggunakan **Rice Type Classification Dataset**. Dataset bisa diakses melalui link berikut:\
🔗 https://www.kaggle.com/datasets/mssmartypants/rice-type-classification

Tujuan utama dari tugas ini adalah membangun model SVM (Support Vector Machine) atau ANN (Artificial Neural Network) untuk menentukan jenis beras berdasarkan karakteristik fisik beras.

Langkah-langkah yang harus dilakukan antara lain:

1. Persiapan Dataset & Eksplorasi Awal
- Memuat dataset, melihat struktur data, tipe fitur (numerik atau kategorikal), dan distribusi label.

2. Preprocessing 
- Memproses data agar siap untuk digunakan dalam model, termasuk menangani missing value, encoding fitur kategorikal, dan normalisasi/standardisasi jika diperlukan.

3. Eksperimen Model 
Untuk SVM:
- Bangun model Support Vector Machine Classifier.
- Eksperimen dengan kernel (linear, rbf, poly), parameter regularisasi C, dan parameter kernel lain seperti gamma.

Untuk ANN:
- Bangun Artificial Neural Network menggunakan satu atau beberapa hidden layer.
- Eksperimen dengan jumlah neuron, jumlah layer, fungsi aktivasi (relu, sigmoid, tanh), optimizer, dan jumlah epoch.

4. Evaluasi Model
- Hitung metrik evaluasi seperti Accuracy, Precision, Recall, F1-Score, serta visualisasikan Confusion Matrix.
- Untuk ANN, visualisasikan learning curve (loss dan accuracy terhadap epoch).

5. Analisis & Kesimpulan
- Bandingkan performa antar eksperimen parameter, kernel (SVM) atau arsitektur (ANN).
- Tentukan kombinasi parameter terbaik yang menghasilkan performa optimal.
- Identifikasi fitur yang paling berpengaruh dalam memprediksi risiko stroke.
- Menarik kesimpulan mengenai kemampuan SVM/ANN dalam menangani dataset ini, termasuk kelebihan dan keterbatasannya.
