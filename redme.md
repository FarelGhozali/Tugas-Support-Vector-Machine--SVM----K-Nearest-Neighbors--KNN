# Komparasi Supervised Learning: SVM vs KNN (Wine Dataset)

Proyek ini bertujuan untuk membandingkan performa dua algoritma klasifikasi populer, **Support Vector Machine (SVM)** dan **K-Nearest Neighbors (KNN)**, menggunakan dataset klasifikasi Wine (Wine Recognition Dataset).

## 📂 Struktur Repositori
- `main.py`: Kode utama implementasi model, evaluasi, dan visualisasi.
- `requirements.txt`: Daftar dependensi library Python yang dibutuhkan.
- `visualisasi_wine.png`: Output grafik confusion matrix hasil eksekusi program.
- `PPT.md`: Panduan konten untuk pembuatan slide presentasi.

## 🚀 Cara Menjalankan Program

Ikuti langkah-langkah berikut untuk menjalankan simulasi di perangkat lokal:

1. **Clone/Download Repositori** ini ke komputer Anda.
2. **Buat Virtual Environment** (Opsional tapi disarankan):
   > python -m venv env

3. **Aktifkan Virtual Environment**:
   - Windows: `env\Scripts\activate`
   - Linux/macOS: `source env/bin/activate`

4. **Instal Dependensi**:
   > pip install -r requirements.txt

5. **Jalankan Skrip**:
   > python main.py

6. **Cek Hasil**: Program akan menampilkan akurasi di terminal dan menyimpan file `visualisasi_wine.png` secara otomatis.

## 📊 Hasil Analisis Singkat
Berdasarkan pengujian pada data uji (20% dari total dataset):
- **Akurasi SVM:** 97.22% (Hanya 1 kesalahan klasifikasi).
- **Akurasi KNN:** 94.44% (2 kesalahan klasifikasi).

*Catatan: SVM menunjukkan performa generalisasi yang lebih stabil pada dataset Wine dibandingkan KNN dengan k=5.*