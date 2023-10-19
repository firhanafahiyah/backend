import random

list_soal = [
    ["pala bapa kau keras","A.lembek B.kenyal C.lembut","A"],
    ["siapa yang mau jadi putri duyung","A.saya B.kamu C.dia","A"],
    ["apa warna laut","A.biru B.merah C.hitam","A"]
]

random.choice(list_soal)
soal = random.choice(list_soal)


# print list_soal indeks ke 0 dan ke 1


print(soal)

pemain = input("pilih satu A B C: ")
if pemain == "A":
    print("jawaban kamu benar") 
else:
    print("jawaban kamu salah")
