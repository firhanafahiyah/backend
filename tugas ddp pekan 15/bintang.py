# Fungsi untuk menampilkan bintang
def segitiga_bintang(a):
  # Menampilkan bintang segitiga atas
  for i in range(a):
    print('*' * (i+1))

  # Menampilkan bintang segitiga bawah
  for i in range(a-1, 0, -1):
    print('*' * i)

# Output bintang dengan angka yang ditentukan
# print(segitiga_bintang(6))
segitiga_bintang(6)