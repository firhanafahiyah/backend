# Fungsi untuk membalik kalimat
def balik_kalimat(s):
  # Pisahkan kata-kata menjadi kalimat
  kata = s.split()

  # Balik urutan kata
  kata = kata[::-1]

  # Gabungkan kata lagi menjadi kalimat
  kalimat_balik = ' '.join(kata)

  return kalimat_balik

# Output
print(balik_kalimat("Saya Mohammad Firhan"))
print(balik_kalimat("saya mahasiswa Nurul Fikri"))
print(balik_kalimat("saya prodi Teknik Informatika"))
print(balik_kalimat("Pemrograman Dasar menyenangkan"))