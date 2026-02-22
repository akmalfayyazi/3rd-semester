[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/yl8pAPnw)
# oop-bouncing-ball-pygame

## Capaian Pembelajaran

Setelah menyelesaikan tutorial ini, mahasiswa diharapkan mampu:

1. Memodelkan permasalahan simulasi bola memantul menggunakan kelas dan objek di Python.
2. Menggunakan PyGame untuk membuat area simulasi, menggambar objek, dan membuat animasi.
3. Menerapkan logika tabrakan bola dengan dinding dan dengan bola lainnya.
4. Menggabungkan event mouse untuk menambah bola baru secara interaktif.

---

## Lingkungan Pengembangan

1. Platform: Python 3.12+
2. Bahasa: Python
3. Editor/IDE yang disarankan:

   * VS Code + Python Extension
   * Terminal
4. Library:

   * pygame 2.6.1

---

## Cara Menjalankan Project

1. Clone repositori project `oop-bouncing-ball-pygame` ke direktori lokal Anda:

   ```bash
   git clone https://github.com/USERNAME/oop-bouncing-ball-pygame.git
   cd oop-bouncing-ball-pygame
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

4. Menjalankan simulasi:

   ```bash
   python -m src.main
   ```

5. Menjalankan unit test:

   ```bash
   pytest
   ```

> PERINGATAN: Lakukan push ke remote repository hanya jika seluruh unit test telah berhasil dijalankan (semua hijau).

---

## Struktur Direktori

Program ini menggunakan struktur sebagai berikut:

```text
oop-bouncing-ball-pygame/
├─ README.md
├─ requirements.txt
└─ src/
   ├─ __init__.py
   ├─ ball.py          # Kelas Ball
   ├─ ball_area.py     # Kelas BallArea (batas area simulasi)
   └─ main.py          # Game loop dan komposisi objek (Ball + BallArea)
```

---

# Pemodelan Objek

Pada bagian ini **objek-objek utama** yang diidentifikasi sesuai dengan studi kasus.

### 1. Kelas `BallArea`

* Mewakili **area bermain** tempat bola bergerak.
* Menyimpan batas koordinat:

  * `min_x`, `min_y`
  * `max_x`, `max_y`
* Memiliki method:

  * `draw(surface)`: menggambar area ke layar.

### 2. Kelas `Ball`

* Mewakili **satu bola** dalam simulasi.
* Menyimpan:

  * Posisi: `x`, `y`
  * Kecepatan: `speed_x`, `speed_y`
  * `radius`
  * `color`
* Memiliki method:

  * `draw(surface)`: menggambar bola.
  * `update()`: memperbarui posisi berdasarkan kecepatan.
  * `collide_with_walls(area)`: memantulkan bola saat menyentuh dinding.
  * `collide_with_ball(other)`: menangani tabrakan dengan bola lain.

### 3. Kelas `BallSimulation` (di `main.py`)

* Mengatur:

  * Window PyGame (`screen`).
  * Objek `BallArea`.
  * List `balls`.
  * Game loop utama.
* Menangani:

  * Event PyGame (klik mouse).
  * Update posisi dan tabrakan bola.
  * Gambar ulang frame setiap iterasi loop.

---

# Langkah-langkah Tutorial

## Langkah 1 — Membuat Window dan Kelas `BallSimulation` Kosong

**Tujuan:** Membuat kerangka awal program PyGame dengan window kosong dan loop utama.

### 1. Membuat file `src/main.py`

Buat folder `src/` (jika belum ada), lalu file `src/main.py`:

```python
# src/main.py
import pygame

class BallSimulation:
    def __init__(self, width: int = 800, height: int = 600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Bouncing Balls Simulation")

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(60)

        pygame.quit()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _update(self):
        # Untuk sementara, belum ada yang di-update
        pass

    def _draw(self):
        self.screen.fill((0, 0, 0))  # Latar belakang hitam
        pygame.display.flip()


if __name__ == "__main__":
    sim = BallSimulation()
    sim.run()
```

**Narasi:**

* Di sini Anda membuat kelas `BallSimulation` yang bertanggung jawab atas:

  * Inisialisasi PyGame.
  * Membuat window (`screen`).
  * Menjalankan loop utama game.
* Method `_handle_events`, `_update`, dan `_draw` masih kosong/sederhana. Nantinya akan diisi dengan logika simulasi.

Jalankan perintah berikut:

```bash
python -m src.main
```

Seharusnya Anda akan melihat jendela hitam kosong.

---

## Langkah 2 — Menambahkan `BallArea` sebagai Area Simulasi

**Tujuan:** Membatasi area tempat bola boleh bergerak dan menggambarnya ke layar.

### 1. Membuat file `src/ball_area.py`

```python
# src/ball_area.py
import pygame
from dataclasses import dataclass

@dataclass
class BallArea:
    min_x: int
    min_y: int
    max_x: int
    max_y: int
    fill_color: tuple = (0, 0, 0)
    border_color: tuple = (255, 255, 255)

    def draw(self, surface: pygame.Surface) -> None:
        width = self.max_x - self.min_x
        height = self.max_y - self.min_y

        # Menggambar area berwarna
        pygame.draw.rect(surface, self.fill_color, (self.min_x, self.min_y, width, height))
        # Menggambar garis tepi
        pygame.draw.rect(surface, self.border_color, (self.min_x, self.min_y, width, height), 2)
```

**Penjelasan singkat:**

* `BallArea` menyimpan batas area simulasi.
* Method `draw` menggambar **persegi panjang** dengan warna latar dan border.

### 2. Menghubungkan `BallArea` dengan `BallSimulation`

Kembali ke `src/main.py` dan tambahkan import:

```python
# ... kode sebelumnya ...
from ball_area import BallArea
```

Lalu, di dalam `__init__`:

```python
class BallSimulation:
    def __init__(self, width: int = 800, height: int = 600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Bouncing Balls Simulation")

        self.clock = pygame.time.Clock()
        self.running = True

        # Tambahkan area simulasi
        self.area = BallArea(
            min_x=50,
            min_y=50,
            max_x=750,
            max_y=550,
            fill_color=(0, 0, 0),
            border_color=(255, 255, 255),
        )
```

Dan di `_draw`:

```python
    def _draw(self):
        self.screen.fill((30, 30, 30))  # latar belakang abu gelap

        # Gambar area simulasi
        self.area.draw(self.screen)

        pygame.display.flip()
```

Jalankan kembali perintah berikut:

```bash
python -m src.main
```

Sekarang Anda akan melihat **persegi panjang** putih (border) di dalam window. Area ini adalah tempat bola nanti akan bergerak.

---

## Langkah 3 — Membuat Kelas `Ball` dan Menampilkan Bola Statis

**Tujuan:** Memodelkan bola sebagai objek dan menggambarnya di `BallArea`.

### 1. Membuat file `src/ball.py`

```python
# src/ball.py
from __future__ import annotations
import pygame
from dataclasses import dataclass

@dataclass
class Ball:
    x: float
    y: float
    radius: float
    color: tuple

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))
```

Pada bagian ini terdapat beberapa hal yang perlu diperhatikan:

* `Ball` hanya tahu:

  * posisi (`x`, `y`),
  * `radius`,
  * `color`.
* Untuk saat ini, `Ball` belum bergerak — hanya menggambar lingkaran.

### 2. Menambahkan List Bola ke `BallSimulation`

Di `src/main.py`, tambahkan import:

```python
from ball import Ball
```

Lalu di `__init__`:

```python
        # ... setelah self.area = ...
        self.balls: list[Ball] = []
        self._create_initial_balls()
```

Tambahkan method private di `BallSimulation`:

```python
    def _create_initial_balls(self):
        # Tambah satu bola merah statis di tengah area
        center_x = (self.area.min_x + self.area.max_x) / 2
        center_y = (self.area.min_y + self.area.max_y) / 2

        self.balls.append(
            Ball(x=center_x, y=center_y, radius=20, color=(255, 0, 0))
        )
```

Update `_draw` agar menggambar bola:

```python
    def _draw(self):
        self.screen.fill((30, 30, 30))
        self.area.draw(self.screen)

        # Gambar semua bola
        for ball in self.balls:
            ball.draw(self.screen)

        pygame.display.flip()
```

Jalankan perintah berikut:

```bash
python -m src.main
```

Anda akan melihat ada **satu bola merah statis** di tengah area.

---

## Langkah 4 — Menambahkan Pergerakan dan Tabrakan dengan Dinding

**Tujuan:** Membuat bola bergerak dan memantul ketika menyentuh dinding area.

### 1. Menambah Kecepatan dan `collide_with_walls` di `Ball`

Buka `src/ball.py` dan perluas kelas:

```python
# ... kode sebelumnya ...
from dataclasses import dataclass
from ball_area import BallArea

@dataclass
class Ball:
    x: float
    y: float
    radius: float
    color: tuple
    speed_x: float = 0.0
    speed_y: float = 0.0

    # ... method draw tetap sama ...

    def update(self) -> None:
        self.x += self.speed_x
        self.y += self.speed_y

    def collide_with_walls(self, area: BallArea) -> None:
        # Cek kiri/kanan
        if self.x - self.radius < area.min_x or self.x + self.radius > area.max_x:
            self.speed_x = -self.speed_x

        # Cek atas/bawah
        if self.y - self.radius < area.min_y or self.y + self.radius > area.max_y:
            self.speed_y = -self.speed_y
```

### 2. Menggerakkan Bola di `BallSimulation`

Di `src/main.py`, ubah `_create_initial_balls`:

```python
    def _create_initial_balls(self):
        center_x = (self.area.min_x + self.area.max_x) / 2
        center_y = (self.area.min_y + self.area.max_y) / 2

        # Bola biru yang bergerak
        self.balls.append(
            Ball(
                x=center_x,
                y=center_y,
                radius=20,
                color=(0, 150, 255),
                speed_x=4,
                speed_y=3,
            )
        )
```

Lalu update `_update`:

```python
    def _update(self):
        for ball in self.balls:
            ball.collide_with_walls(self.area)
            ball.update()
```

Jalankan perintah berikut:

```bash
python -m src.main
```

Sekarang bola akan **bergerak dan memantul** ketika menyentuh dinding `BallArea`.

---

## Langkah 5 — Tabrakan Antar Bola dan Penambahan Bola dengan Klik Mouse

**Tujuan:** Menambahkan interaksi antar bola dan membuat simulasi lebih dinamis.

### 1. Menambahkan `collide_with_ball` di `Ball`

Di `src/ball.py`, tambahkan:

```python
import math
# ... kode sebelumnya ...

    def collide_with_ball(self, other: "Ball") -> None:
        dx = other.x - self.x
        dy = other.y - self.y
        distance = math.sqrt(dx * dx + dy * dy)

        if distance == 0:
            return

        if distance < self.radius + other.radius:
            # Sederhana: tukar arah (pantulan kasar)
            self.speed_x = -self.speed_x
            self.speed_y = -self.speed_y
            other.speed_x = -other.speed_x
            other.speed_y = -other.speed_y
```

### 2. Memanggil `collide_with_ball` di `_update`

Di `src/main.py`, di dalam `_update` setelah loop `for ball in self.balls`:

Tambahkan loop kedua:

```python
    def _update(self):
        # Update posisi dan tabrakan dengan dinding
        for ball in self.balls:
            ball.collide_with_walls(self.area)
            ball.update()

        # Tabrakan antar bola
        for i in range(len(self.balls)):
            for j in range(i + 1, len(self.balls)):
                self.balls[i].collide_with_ball(self.balls[j])
```

### 3. Menambahkan Bola Baru dengan Klik Mouse

Kita ingin bisa menambah bola baru dengan meng-klik area simulasi.

Tambahkan import `random` dan `math` di `src/main.py`:

```python
import pygame
import random
import math

from ball_area import BallArea
from ball import Ball
```

Lalu di method `_handle_events`:

```python
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Hanya tambahkan jika klik di dalam area
                if (self.area.min_x < x < self.area.max_x and
                        self.area.min_y < y < self.area.max_y):
                    self._add_ball_at(x, y)
```

Tambahkan method `_add_ball_at`:

```python
    def _add_ball_at(self, x: int, y: int):
        radius = 15
        speed = 5
        angle_deg = random.randint(0, 359)
        angle_rad = math.radians(angle_deg)

        speed_x = speed * math.cos(angle_rad)
        speed_y = -speed * math.sin(angle_rad)

        color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
        )

        self.balls.append(
            Ball(
                x=x,
                y=y,
                radius=radius,
                color=color,
                speed_x=speed_x,
                speed_y=speed_y,
            )
        )
```

Jalankan perintah ini kembali:

```bash
python -m src.main
```
Perhatikan dan lakukan observasi sebagai berikut:

* Awalnya hanya ada satu bola bergerak.
* Klik di dalam area → bola baru muncul dengan warna dan arah acak.
* Bola akan:

  * Memantul di dinding.
  * Saling bertabrakan dengan pantulan sederhana.

---