nim = ["2","3","1","0","3","1","0","6","8"]
print(nim)

print("item index 0 pertama",nim[0])
print("item index 1 pertama",nim[1])

print(f"item index 0 (pertama) {nim[0]}")
print(f"item index 1 (kedua)   {nim[-1]}")
print(f"item index terakhir {nim[len(nim)-1]}")
print(f"item index terakhir {nim[-1]}")
print(f"item index terakhir {nim[-len(nim)]}")

data = ["Rahmat Efendi",2023,"Aktif"]
nilai= [90,89,93,97]

print("Nama: "+ data[0])
print("angkatan:", data[1])
print("status:", data[2])

#Von Neumann status Kuliah: Aktif
print(f"{data[0]} status aktif: {data[2]}")
# Data terbesar nilai adalah: 97
print(f"data terbesar nilai adalah {max(nilai)}")
# Data terkecil nilai adalah: 89
print(f"data terkecil nilai adalah {min(nilai)}")
#Rata-rata nilai adalah: 92.25
rataan =sum(nilai) / len(nilai)
print(f"rata-rata nilai adalah {rataan}")

data = [("Rahmat Efendi",2023,"Aktif",231031068),
        (90,89,93,97),
        (20,22),
        ("S1-Reguler","sistem informasi c","Ganjil")]
print(data[0][0])
print(data[-1][0])
print(data[2][0:])
print()

#  Nama Mahasiswa: Rahmat Efendi
print(f"Nama Mahasiswa : {data[0][0]}")
#  Inisial Rahmat Efendi: R E
print(f"Inisial Rahmat Efendi : {data[0][0][0]} {data[0][0][7]}")
#  NIM Rahmat Efendi: 231031068
print(f"Nim {data[0][0]} : {nim[0]}{nim[1]}{nim[2]}{nim[3]}{nim[4]}{nim[5]}{nim[6]}{nim[7]}{nim[8]}")
#  Program pendidikan Rahmat Efendi: Sistem Informasi C S1-Reguler
print(f"program pendidikan {data[3][1]} {data[3][0]}")
#  Angkatan Rahmat Efendi: 2023-Ganjil
print(f"Angkatan {data[0][0]} : {2023}")
#  Jumlah nilai Rahmat Efendi adalah: 5
print(f"Jumlah nilai {data[0][0]} {11}")
#  Data terbesar Rahmat Efendi adalah: 100
print(f"Data terbesar {data[0][0]} : {max(nilai)}")
#  Data terkecil Rahmat Efendi adalah: 89
print(f"Data terkecil {data[0][0]} : {min(nilai)}")
#  Rata-rata nilai Rahmat Efendi adalah: 92.25 
print(f"Rata-rata {data[0][0]} : {sum(nilai)/len(nilai)}")

print()
matkul=["matkul Agama Islam",
          "matkul Pancasila",
          "matkul Bahasa Indonesia",
          "matkul Wawasan Cinta IPTEK dan IMTAQ",
          "matkul Pengantar Pemrograman"]
sks = [2,2,2,2,3] 
matkul.append("matkul Pengantar Teknologi Informasi")
matkul.append("matkul Kalkulus Dasar I")
matkul.append("matkul Sains Terpadu")
print(matkul)
sks.append(3)
sks.append(3)
sks.append(3)
print(sks) 

# Tambahkan matkul dan sks ke dalam data (pakai append)

# Daftar Mata kuliah
# Mata kuliah 1: Matkul1 dengan jumlah 2 sks
# Mata kuliah 2: Matkul2 dengan jumlah 3 sks
# Mata kuliah 3: Matkul3 dengan jumlah 2 sks
# Mata kuliah 4: Matkul4 dengan jumlah 3 sks
# Mata kuliah 5: Matkul5 dengan jumlah 3 sks
# Mata kuliah 6: Matkul6 dengan jumlah .. sks
# Mata kuliah 7: Matkul7 dengan jumlah .. sks
# Mata kuliah 8: Matkul8 dengan jumlah .. sks

# Tambah Nilai jadi 8 (pakai append)

#Daftar mata kuliah
print(f"mata kuliah 1: {matkul[0]} dengan jumlah {sks[0]} sks")
print(f"mata kuliah 2: {matkul[1]} dengan jumlah {sks[1]} sks")
print(f"mata kuliah 3: {matkul[2]} dengan jumlah {sks[2]} sks")
print(f"mata kuliah 4: {matkul[3]} dengan jumlah {sks[3]} sks")
print(f"mata kuliah 5: {matkul[4]} dengan jumlah {sks[4]} sks")
print(f"mata kuliah 6: {matkul[5]} dengan jumlah {sks[5]} sks")
print(f"mata kuliah 7: {matkul[6]} dengan jumlah {sks[6]} sks")
print(f"mata kuliah 8: {matkul[7]} dengan jumlah {sks[7]} sks")