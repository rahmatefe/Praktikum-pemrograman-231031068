import os

def judul():
    os.system('clear')
    print('PROGRAM MENGHITUNG VOLUME DA LAUS PERMUKAAN KUBUS')
    print('BANGUN RUANG KUBUS')
    print()

def inputan():
    p = float(input('masukan panjang:'))
    l = float(input('Masukan lebar:'  ))
    t = float(input('Masukan Tinggi:' ))
    return p,l,l

def perhitang(p,l,t):
    vol = p * l * t
    luas = 2 * (p*l + p*t + l*t)
    luas_non_tutup = luas - p*l
    return vol,luas,luas_non_tutup

def tampilkan(jenis,nilai):
    print(f'Nilai dari {jenis} adalah : {nilai}')

def pilihan():
    pilih = input('Apakah lanjutan [y/n]')
    if pilih == 'y':
        a = True
    else:
        a = False
        print('sampai jumpa lagi.')
    return

def main():
    judul()                                   #judul
    p,l,t = inputan()                         # inputan
    vol,luas,luas_non_tutup = perhitang(p,l,t)#perhitungan 
    #tampilkan
    tampilkan('Volume',vol)
    tampilkan('luas permukaan',luas)
    tampilkan('luas permukaan tanpa tutup',luas_non_tutup)
    a = pilihan()    #pilihan

a = True
while a:
    main()