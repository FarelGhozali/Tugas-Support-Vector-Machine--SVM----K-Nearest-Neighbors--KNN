# Konten Presentasi (Panduan Slide)

### Slide 1: Judul & Identitas
- **Judul Utama:** Analisis Komparatif Algoritma SVM dan KNN pada Klasifikasi Wine.
- **Sub-judul:** Tugas Besar Machine Learning - Supervised Learning.

### Slide 2: Pembagian Tugas (Role)
- nama anggota kelompok

### Slide 3: Tujuan Proyek
- Mengimplementasikan algoritma Supervised Learning untuk klasifikasi multikelas.
- Membandingkan akurasi antara metode berbasis margin (SVM) dan metode berbasis jarak (KNN).
- Menganalisis model mana yang lebih optimal dalam meminimalkan kesalahan diagnosis/klasifikasi.

### Slide 4: Dataset: Wine Recognition
- **Sumber Data:** UCI Machine Learning Repository (`sklearn.datasets.load_wine`).
- **Karakteristik:**
  - 178 sampel data analisis kimiawi wine.
  - 13 fitur numerik (Alkohol, Magnesium, Fenol, dll).
  - 3 kelas target (Kultivar Wine).
- **Link:** https://archive.ics.uci.edu/dataset/109/wine

### Slide 5: Metodologi & Preprocessing
1. **Pembersihan Data:** Memisahkan fitur dan label kelas.
2. **Data Splitting:** 80% data latih, 20% data uji.
3. **Standardisasi:** Menggunakan `StandardScaler` agar fitur dengan satuan berbeda (misal: Alkohol vs Magnesium) memiliki skala yang sama. *Sangat krusial bagi KNN dan SVM.*

### Slide 6: Hasil Perbandingan (Metrik)

| Metrik | Support Vector Machine (SVM) | K-Nearest Neighbor (KNN) |
| :--- | :--- | :--- |
| **Akurasi** | **97.22%** | **94.44%** |
| **Jumlah Salah Tebak** | 1 Sampel | 2 Sampel |
| **Keunggulan** | Efektif pada dimensi tinggi | Sederhana & tanpa fase latih berat |

### Slide 7: Visualisasi (Confusion Matrix)
- *Instruksi untuk rekan:* Masukkan gambar `visualisasi_wine.png` ke sini.
- **Analisis:** Matriks menunjukkan bahwa SVM hampir sempurna dalam mengklasifikasikan semua kelas, sedangkan KNN sedikit kesulitan membedakan kelas 1 dan kelas 0/2.

### Slide 8: Kesimpulan
- Untuk dataset Wine, **SVM lebih unggul** karena mampu menciptakan pemisah (hyperplane) yang lebih baik di ruang dimensi tinggi.
- KNN tetap kompetitif namun sangat bergantung pada pemilihan nilai `k` dan skala data.