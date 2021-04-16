import math
print("Membuat program dengan fungsi numeric".upper())
print('')

# program menghitung nilai dengan fungsi min, max dan ceil
nilai_satu = 88.73
nilai_dua = 90.65
nilai_tiga = 75.53
nilai_total = (nilai_satu + nilai_dua + nilai_tiga)
nilai_akhir = (nilai_satu + nilai_dua + nilai_tiga)/3

print("Nilai tertinggi anda adalah: ", max(nilai_satu, nilai_dua, nilai_tiga))
print("Nilai terendah anda adalah: ", min(nilai_satu, nilai_dua, nilai_tiga))
print("Nilai total anda adalah: ", nilai_total)
print("Nilai akhir anda adalah: ", math.ceil(nilai_akhir))
print("-"*35)

# program menghitung salah satu nilai dalam angka satuan dan huruf menggunakan fungsi nilai sqrt() math
nilai_satu = 88.73
print("Nilai pertama anda dalam satuan adalah: ", int(float(math.sqrt(nilai_satu))))
print("Nilai pertama anda dalam huruf adalah: ")
if nilai_satu >= 8.5:
    print("A")
elif nilai_satu >= 7.5:
    print("B")
elif nilai_satu == 6.0:
    print("C")
else:
    pass
print("-"*35)

# program menghitung salah satu nilai menggunakan fungsi floor, pow dan abs
nilai_dua = 90.65
nilai_tiga = 75.53
nilaidua_setelah_dikonversi = int(float(math.floor(nilai_dua)))
nilaitiga_setelah_dikonversi = int(float(math.floor(nilai_tiga)))
nilai_rerata = (math.floor(nilai_dua + nilai_tiga)/2)
hasil_reratadua = abs(nilai_rerata - nilaidua_setelah_dikonversi)
hasil_reratatiga = abs(nilai_rerata - nilaitiga_setelah_dikonversi)
hasil_pangkat_rerata = int(pow(hasil_reratadua, hasil_reratatiga))
print("Nilai kedua anda dalam satuan adalah: ", nilaidua_setelah_dikonversi)
print("Nilai ketiga anda dalam satuan adalah: ", nilaitiga_setelah_dikonversi)
print("nilai rata-rata anda adalah: ", nilai_rerata)
print("hasil dari perpangkatan nilai rerata: ", hasil_pangkat_rerata)