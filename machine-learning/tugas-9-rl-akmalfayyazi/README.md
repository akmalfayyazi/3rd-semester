[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/C9_Ee_gF)
# Tugas 9 – Reinforcement Learning

| Nama              | NRP        |
|-------------------|------------|
| Mohammad Akmal Fayyazi            | 5054241045      |

---

## Deskripsi Tugas

Implementasikan reinforcement learning (RL) pada proyek bebas.

---

## Langkah-langkah (Proses Step-by-step untuk Reinforcement Learning)

### 1. Definisikan masalah & lingkungan (Environment)
- Jelaskan tugas yang ingin diselesaikan (goal/objective).
- Jelaskan lingkungan yang digunakan: simulator yang digunakan (Gym, PyBullet, MuJoCo, Unity, custom).

### 2. Formalkan MDP (State, Action, Reward)
- State: tentukan observasi (raw pixels, vectored features, stacked frames).
- Action: tentukan ruang aksi (diskrit vs kontinu).
- Reward: desain fungsi reward yang mendorong tujuan utama; hindari reward sparsity atau shaping yang memicu eksploitasi tak diinginkan.
- Tentukan terminal conditions dan horizon (max steps per episode).

### 3. Arsitektur model & komponen penting
- Desain model dan policy.
- Tentukan beberapa hyperparameter, seperti learning rate, batch size, $\gamma$ (discount), $\lambda$ (GAE), $\tau$ (soft update), target update freq, replay size, update frequency.

### 4. Desain loop training & eksplorasi
- Implementasikan loop: kumpulkan rollouts → update model → evaluasi periodik → simpan checkpoint.
- Uji strategi eksplorasi, seperti epsilon-greedy, noise (OU, Gaussian), entropy regularization.

### 5. Evaluasi & metrik
- Metrik utama: rata-rata return per episode, median, variance, success rate, sample efficiency (return vs environment steps).
- Visualisasi: learning curves (reward & loss vs steps/episodes), moving average, boxplots per seed.

### 6. Analisis eksperimen
- Uji stabilitas: jalankan beberapa seed random untuk estimasi variabilitas.
- Bandingkan algoritma & arsitektur.
- Diagnosa failure (jika ada), seperti reward hacking, mode collapse, divergensi training.
