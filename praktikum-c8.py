import os
import random as rd
os.system('clear')

warna = ['merah','putih','hitam']
com = rd.choice(warna)
a = True

while a:
    pilih = input('masukan pilihan [merah,putih.hitam]:')
    if pilih == com:
        print(f'pilihan anda benar yaitu {pilih} \n')
        a = False
    else:
        print('Tebakan anda salah! coba lagi.')

#Tugas: buat program tebak angka 1 sampai 10 dengan batas kesempatan 3 kali. berikan pesan "kesempatan "