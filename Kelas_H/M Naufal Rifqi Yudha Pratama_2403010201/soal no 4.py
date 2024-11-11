# Menghitung Jumlah Huruf Vokal dalam Kalimat
kalimat = input("Masukkan kalimat: ")

vokal = 'aeiouAEIOU'
jumlah_vokal = sum(1 for char in kalimat if char in vokal)

print(f"Jumlah huruf vokal: {jumlah_vokal}")
# keterangan program di atas bertujuan untuk menghitung jumlah huruf vokal dalam sebuah kalimat yang dimasukan oleh pengguna.
#1 input kata,Daftar Huruf vokal,Perhitungan jumlah huruf vokal
#Muhammad Naufal Rifqi Yudha Pratama 2403010201
