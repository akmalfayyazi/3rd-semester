[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Vtvcjow0)
# oop-event-handling-pygame

## Capaian Pembelajaran

1. Mahasiswa memahami dasar penggunaan PyGame sebagai library untuk membuat aplikasi permainan.
2. Mahasiswa memahami konsep event loop, event-driven programming, dan koordinat layar.
3. Mahasiswa mampu menerapkan event handling mouse dan keyboard dalam sebuah program PyGame.
4. Mahasiswa mampu membangun objek interaktif sederhana menggunakan pemrograman berorientasi objek.

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

1. Clone repositori project `oop-event-handling-pygame` ke direktori lokal Anda:

   ```bash
   git clone https://github.com/USERNAME/oop-event-handling-pygame.git
   cd oop-event-handling-pygame
   ```

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

   *Mouse Event Handling:*

   ```bash
   python -m src.mouse_event_handling
   ```

   *Keyboard Event Handling:*

   ```bash
   python -m src.keyboard_event_handling
   ```


---

# Tutorial Event Handling dengan PyGame

Tutorial ini akan memperkenalkan:

* Cara membuat window PyGame
* Cara menggambar objek
* Cara menangani **event mouse**
* Cara menangani **event keyboard**
* Konsep **event loop**
* Cara membuat program interaktif sederhana

Seluruh kode dapat ditulis di dalam file:

```
src/
├─ mouse_event_handling.py
└─ keyboard_event_handling.py
```

---

# Bagian 1 — Mouse Event Handling

Pada bagian ini kita akan membuat sebuah program yang menampilkan:

* Sebuah kotak di tengah layar
* Teks status event di bagian atas
* Program akan merespons:

  * Klik mouse
  * Bergeraknya mouse
  * Masuk/keluar area kotak

---

## 1. Membuat File dan Mengimpor PyGame

Buat file:

```
src/mouse_event_handling.py
```

Tuliskan kode berikut:

```python
import pygame
import random
```

**Penjelasan:**

* `pygame` digunakan untuk membuat window dan event loop.
* `random` digunakan untuk mengubah warna kotak secara acak.

Tuliskan kode berikut untuk menginisialisasi PyGame:

```python
# ... kode sebelumnya ...

pygame.init()
```

PyGame harus diinisialisasi sebelum digunakan.

---

## 2. Membuat Window Pertama

Tambahkan kode berikut:

```python
# ... kode sebelumnya ...

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mouse Event Handling")
```

**Penjelasan:**

* `set_mode((400,400))` membuat window 400x400 piksel.
* `set_caption()` mengubah judul jendela.

Coba jalankan program sekarang (belum ada apa-apa selain window kosong):

```bash
python -m src.mouse_event_handling
```

---

## 3. Menyiapkan Warna, Font, dan Teks

Tambahkan kode:

```python
# ... kode sebelumnya ...

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 20)
info_text = "Arahkan mouse ke kotak atau klik kotak."
```

---

## 4. Membuat Kotak (Rect)

Tambahkan:

```python
# ... kode sebelumnya ...

box_rect = pygame.Rect(150, 150, 100, 100)
box_color = BLUE
```

---

## 5. Membuat Event Loop

Setiap program PyGame harus memiliki *loop utama*:

```python
# ... kode sebelumnya ...

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```

**Penjelasan:**

* Loop berjalan 60 FPS.
* Ketika window ditutup → program berhenti.

---

## 6. Menggambar Kotak dan Teks ke Layar

Tambahkan:

```python
    # ... kode event loop sebelumnya ...

    screen.fill(BLACK)
    pygame.draw.rect(screen, box_color, box_rect)

    label = font.render(info_text, True, WHITE)
    screen.blit(label, (10, 10))

    pygame.display.flip()
    clock.tick(60)
```

Jalankan program maka kotak sudah terlihat.

---

## 7. Menangani Mouse Click

Tambahkan dalam event loop:

```python
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if box_rect.collidepoint(event.pos):
                box_color = (
                    random.randint(0,255),
                    random.randint(0,255),
                    random.randint(0,255),
                )
                info_text = f"Mouse clicked at {event.pos}"
```

---

## 8. Menangani Mouse Move / Enter / Leave

Tambahkan:

```python
        elif event.type == pygame.MOUSEMOTION:
            if box_rect.collidepoint(event.pos):
                info_text = f"Mouse moving at {event.pos}"
                mouse_inside = True
            else:
                if mouse_inside:
                    info_text = "Mouse left the box area."
                    mouse_inside = False
```

Sekarang program sudah penuh dengan interaksi mouse.

---

# Bagian 2 — Keyboard Event Handling

Pada bagian ini, kita akan membuat lingkaran yang bisa digerakkan dengan tombol panah.

---

## 1. Membuat File Baru

Buat:

```
src/keyboard_event_handling.py
```

Isi awalnya:

```python
import pygame
pygame.init()
```

---

## 2. Membuat Window

Tambahkan:

```python
# ... kode sebelumnya ...

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Keyboard Event Handling")
```

---

## 3. Membuat Objek Lingkaran

Tambahkan:

```python
# ... kode sebelumnya ...

circle_x, circle_y = 250, 200
radius = 30
speed = 200

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,220,0)

font = pygame.font.SysFont(None, 20)
info_text = "Gunakan tombol panah untuk menggerakkan lingkaran."
```

---

## 4. Membuat Event Loop

Tambahkan:

```python
# ... kode sebelumnya ...

clock = pygame.time.Clock()
running = True

while running:
    dt = clock.tick(60) / 1000.0
```

---

## 5. Menangani Tombol Panah (Pergerakan)

Tambahkan:

```python
    # ... kode event loop sebelumnya ...

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        circle_x -= speed * dt
    if keys[pygame.K_RIGHT]:
        circle_x += speed * dt
    if keys[pygame.K_UP]:
        circle_y -= speed * dt
    if keys[pygame.K_DOWN]:
        circle_y += speed * dt
```

---

## 6. Menangani Tombol SPACE dan ESC

Tambahkan ke event loop:

```python
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                info_text = "SPACE ditekan!"
            elif event.key == pygame.K_ESCAPE:
                running = False
```

---

## 7. Agar Lingkaran Tidak Keluar Layar

Tambahkan:

```python
    circle_x = max(radius, min(circle_x, 500 - radius))
    circle_y = max(radius, min(circle_y, 400 - radius))
```

---

## 8. Menggambar ke Layar

Tambahkan:

```python
    screen.fill(BLACK)
    pygame.draw.circle(screen, GREEN, (int(circle_x), int(circle_y)), radius)

    label = font.render(info_text, True, WHITE)
    screen.blit(label, (10, 10))

    pygame.display.flip()
```

---

## 9. Jalankan Program

Mouse handling:

```bash
python -m src.mouse_event_handling
```

Keyboard handling:

```bash
python -m src.keyboard_event_handling
```

---
