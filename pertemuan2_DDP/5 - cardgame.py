kartu = [
    (10, "sepuluh"),
    (11, "jack"),
    (12, "queen"),
    (13, "king"),
    (14, "AS"),
    (15, "joker")
]
random.shuffle(kartu)

print(kartu)
pilihan = int(input("masukan angka 1/2/3 untuk memilih kartu secara acak:"))
if pilihan == 1:
    pemain = kartu[0]
elif pilihan == 2:
    pemain = kartu[1]
elif pilihan == 3:
    pemain = kartu[2]
    
print(f"kartu kamu adalah {pemain[1]}")

komputer = random.choice(kartu)
print(f"kartu lawan adalah {komputer[1]}")

if pemain[0] == komputer[0]:
    print("seimbang, tidak ada yang menang")
elif pemain[0] > komputer[0]:
    print("selamat kamu menang")
else:
    print("kamu kalah")
