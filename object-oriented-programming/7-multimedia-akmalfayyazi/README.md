[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/0x-JdOjy)
# oop-multimedia-pygame

## Capaian Pembelajaran

1. Mahasiswa memahami dasar penggunaan PyGame untuk memproses multimedia (visual & audio).
2. Mahasiswa mampu menggambar bentuk-bentuk dasar (shapes) menggunakan PyGame.
3. Mahasiswa mampu memuat, menampilkan, dan memanipulasi gambar (image loading & transformation).
4. Mahasiswa mampu memuat dan memainkan suara/efek suara (sound/SFX) menggunakan PyGame Mixer.
5. Mahasiswa mampu menggabungkan gambar, suara, dan drawing ke dalam program multimedia interaktif sederhana.

---

## Lingkungan Pengembangan

1. Platform: Python 3.12+
2. Bahasa: Python
3. Editor/IDE yang disarankan:
   - VS Code + Python Extension
   - Terminal
4. Library:
   - pygame 2.6.1

---

## Cara Menjalankan Project

1. Clone repositori project `oop-multimedia-pygame` ke direktori lokal Anda:

   ```bash
   git clone https://github.com/USERNAME/oop-multimedia-pygame.git
   cd oop-multimedia-pygame
   ````

2. Buat dan aktifkan virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate        # Linux/macOS
   .venv\Scripts\activate           # Windows
   ```

3. Install dependensi:

   ```bash
   pip install -r requirements.txt
   ```

4. Menjalankan program:

   *Drawing Shapes:*

   ```bash
   python -m src.drawing_shapes
   ```

   *Image Demo:*

   ```bash
   python -m src.image_demo
   ```

   *Sound Demo:*

   ```bash
   python -m src.sound_demo
   ```

---

# Tutorial Multimedia dengan PyGame

Pada modul ini, kita akan mempelajari tiga kemampuan dasar untuk membuat aplikasi multimedia interaktif:

1. **Menggambar bentuk (drawing shapes)**
2. **Menampilkan dan memanipulasi gambar (image)**
3. **Memutar suara/efek audio (sound/SFX)**

File tutorial dapat ditemukan pada folder:

```
src/
├─ drawing_shapes.py
├─ image_demo.py
└─ sound_demo.py
```

Setiap bagian dimulai dari konsep, diikuti langkah kode, lalu diakhiri dengan penjelasan hasil yang seharusnya terlihat.

---

# Bagian 1 — Drawing Shapes dengan PyGame

Pada bagian ini kita akan belajar bagaimana menggambar bentuk-bentuk dasar menggunakan PyGame.
Ini adalah pondasi untuk memahami bagaimana game 2D menampilkan objek visual.

Bentuk yang akan kita gambar:

* Persegi (rectangle)
* Lingkaran (circle)
* Garis (line)
* Polygon (bentuk bebas)

---

## 1. Inisialisasi PyGame dan Window

Pertama, kita membuat file:

```
src/drawing_shapes.py
```

Kemudian tambahkan kode berikut:

```python
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Drawing Shapes")
clock = pygame.time.Clock()
running = True
```

### Penjelasan

* `pygame.init()` wajib dipanggil sebelum menggunakan PyGame.
* `set_mode()` membuat window ukuran 600×400 px.
* `clock` digunakan untuk mengatur FPS (frame per second).
* Variabel `running` digunakan untuk menjalankan loop utama.

Jalankan perintah berikut:

```bash
python -m src.drawing_shapes
```

Setelah menjalankan perintah tersebut, Anda sudah bisa membuka window kosong PyGame.

---

## 2. Mendefinisikan Warna

Untuk menggambar shapes, kita perlu mendefinisikan warna:

```python
WHITE  = (255, 255, 255)
RED    = (255,   0,   0)
GREEN  = (0,   255,   0)
BLUE   = (0,     0, 255)
YELLOW = (255, 255,   0)
```

### Penjelasan

* Warna direpresentasikan oleh tuple `(R, G, B)`.
* Rentang masing-masing nilai: 0–255.
* Warna digunakan oleh fungsi-fungsi drawing PyGame.

---

## 3. Menggambar Shapes di Dalam Game Loop

Tambahkan loop utama berikut:

```python
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, (50, 50, 120, 80))
    pygame.draw.circle(screen, BLUE, (300, 200), 50)
    pygame.draw.line(screen, GREEN, (100, 350), (500, 350), 5)
    pygame.draw.polygon(screen, YELLOW, [(400, 50), (450, 150), (350, 150)])

    pygame.display.flip()
    clock.tick(60)
```

### Penjelasan

* `screen.fill(WHITE)` membersihkan layar setiap frame.
* `draw.rect` menggambar persegi.
* `draw.circle` menggambar lingkaran di tengah layar.
* `draw.line` menggambar garis horizontal.
* `draw.polygon` menggambar segitiga kuning.
* `pygame.display.flip()` memperbarui tampilan.

### Hasil yang diharapkan

Anda akan melihat empat bentuk berwarna yang ditampilkan bersamaan di layar.

Jalankan perintah berikut untuk melihat hasilnya:

```bash
python -m src.drawing_shapes
```

---

# Bagian 2 — Menampilkan Gambar (Image Loading)

Setelah memahami drawing shapes, kita beralih ke memuat gambar dari file.
PyGame mendukung format `.png`, `.jpg`, `.bmp`, dll.

Siapkan gambar:

```
assets/images/spaceship.png
```

---

## 1. Load Image dari File

Buat file:

```
src/image_demo.py
```

Tambahkan kode berikut:

```python
import pygame
import os

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

BASE = os.path.dirname(os.path.dirname(__file__))
IMG_PATH = os.path.join(BASE, "assets", "images", "spaceship.png")

image = pygame.image.load(IMG_PATH).convert_alpha()
```

### Penjelasan

* `convert_alpha()` menjaga transparansi gambar (RGBA).
* `os.path.join()` memastikan path file benar di semua OS.

Jika gambar tidak ditemukan, maka PyGame akan melempar error.

---

## 2. Scaling (Mengubah Ukuran Gambar)

```python
image = pygame.transform.scale(image, (80, 80))
x, y = 250, 150
```

### Penjelasan

* `transform.scale` mengubah ukuran gambar sesuai kebutuhan.
* Variabel `x, y` digunakan untuk posisi gambar di layar.

---

## 3. Menampilkan Gambar di Layar

Tambahkan loop utama:

```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))
    screen.blit(image, (x, y))

    pygame.display.flip()
    clock.tick(60)
```

### Hasil yang diharapkan

Anda akan melihat gambar spaceship muncul di tengah layar di atas background gelap.

Jalankan:

```bash
python -m src.image_demo
```

---

# Bagian 3 — Memutar Suara (Sound & SFX)

PyGame Mixer memungkinkan Anda memainkan:

* suara klik
* efek laser
* background music

Siapkan file suara:

```
assets/sounds/laser.wav
```

---

## 1. Inisialisasi Mixer

Buat file:

```
src/sound_demo.py
```

Tambahkan:

```python
import pygame
import os

pygame.init()
pygame.mixer.init()
```

### Penjelasan

* `pygame.mixer.init()` wajib sebelum memuat suara.
* Mixer dapat gagal jika hardware audio sedang digunakan aplikasi lain.

---

## 2. Load File Suara

```python
BASE = os.path.dirname(os.path.dirname(__file__))
SOUND_PATH = os.path.join(BASE, "assets", "sounds", "laser.wav")

laser_sound = pygame.mixer.Sound(SOUND_PATH)
```

### Penjelasan

* `Sound()` memuat file suara ke memori.
* Format umum: `.wav` (paling stabil di PyGame).

---

## 3. Mainkan Suara Saat SPACE ditekan

```python
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Sound Demo")

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                laser_sound.play()
```

### Penjelasan

* Setiap kali SPACE ditekan → efek laser diputar.
* Suara dapat diputar overlap / bersamaan.

---

## 4. Menampilkan Teks Instruksi

Tambahkan:

```python
font = pygame.font.SysFont(None, 24)
```

Lalu di bagian rendering:

```python
screen.fill((0, 0, 0))
label = font.render("Tekan SPACE untuk memainkan suara", True, (255, 255, 255))
screen.blit(label, (90, 130))

pygame.display.flip()
clock.tick(60)
```

### Hasil yang diharapkan

Saat SPACE ditekan maka efek laser terdengar.
Teks instruksi akan tampil di tengah layar.

Jalankan:

```bash
python -m src.sound_demo
```

---