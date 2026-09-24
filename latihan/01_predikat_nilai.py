# Pertemuan 04 - Latihan 1
# Nama: Fahrezi sauqi alghani
# NIM: 2225250029

nilai = float(input("Nilai akhir (0-100): "))

if nilai >= 85:
    predikat = "A"
elif nilai >= 70:
    predikat = "B"
elif nilai >= 60:
    predikat = "C"
elif nilai >= 50:
    predikat = "D"
else:
    predikat = "E"

print(f"Nilai {nilai:.2f} memperoleh predikat {predikat}.")