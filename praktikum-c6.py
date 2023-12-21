import os
os.system('clear')

a = True

while a:
    pilih = input('Apakah ingin melanjutkan [y/n]')
    if pilih == 'y':
        print('Terima kasih!')
    elif pilih == 'n':
        print('sampai jumpa lagi :)')
    else:
        print('jangan aneh deh! :(')