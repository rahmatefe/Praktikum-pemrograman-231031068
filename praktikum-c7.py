import os 
os.system('clear')

pwd_benar = 'si23c'
a = True
limit = 3
i = 0
while a:
    i += 1
    pwd = input('masukkan password: ')
    if pwd == pwd_benar:
        print('selamat anda berhasil login!')
        a = False
    else:
        if i < limit:
             print('password salah!')
             print(f'kesempatan Anda tersisa {limit-i} kali')
             a = True
        else:
            print('kesempatan anda habis!')
            a = False


