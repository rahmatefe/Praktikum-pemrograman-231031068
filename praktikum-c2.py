print("Nama          : Rahmat Efendi")
print("Nim           : 231031068")
print("prodi         : Sistem Informasi")
print("Tanggal lahir : 01-mei-2005")

print()
#operasi aritmatika
a=68
print('Nilai a =' ,a )
a=68
a+=1
print('Nilai a +=1 akan menjadi' ,a)
a=68
a-=1
print('Nilai a -=1 akan menjadi' ,a)
a=68
a*=2

print('Nilai a *=2 akan menjadi' ,a)
a=68
a/=2
print('Nilai a /=2 akan menjadi' ,a)
a=68
a%=2
print('Nilai a %=2 akan menjadi' ,a)
a=68
a//=2

print('Nilai a //=2 akan menjadi' ,a )
a=68
a**=2
print('Nilai a **=2 akan menjadi ' ,a )
#OR
b=True
print('Nilai b =' ,b )
b|=False
print('Nilai b|= False akan menjadi' ,b )
b=False
print ('Nilai b =' ,b )
b|=False
print('Nilai b|= False akan menjadi' ,b )
#AND
b=True
print('Nilai b =' ,b )
b&=False
print ('Nilai b&= False akan menjadi ' ,b )
b= False
print('Nilai b =' ,b )
b&=False
print('Nilai b&= False akan menjadi ',b )
#XOR
b=True
print('Nilai b =',b )
b^=False
print('Nilai b^= False akan menjadi ',b )
b=False
print('Nilai b =' ,b )
b^=False
print ('Nilai b^= False akan menjadi ' ,b )
#Shifting
c=0b0100
print('Nilai c =',format (c , '04b'))
c>>=1
print('Nilai c >>=1 akan menjadi',format(c , '04b'))
c=0b0100
c <<=1
print('Nilai c <<=1 akan menjadi',format(c, '04b'))

print()
a =8 #isi dengan ujung NIM
b =13 #Ubah dengan hasil jumlah ujung NIM dengan 5
print('================== Besar dari 13')
hasil = a>13
print(a,'> 13 adalah',hasil)
hasil = b >13
print(b,'> 13 adalah ',hasil)


print('================== Kecil dari 13')
hasil = a <13
print(a,'< 13 adalah ',hasil)
hasil = b <13
print(b,'< 13 adalah ', hasil)

print('================== Besar atau sama dari 13')
hasil = a >=13
print(a,' >= 13 adalah ',hasil)
hasil = b >=13
print(b,' >= 13 adalah ',hasil)

print('================== Besar atau sama dari 13')
hasil = a <=13
print(a,' <= 13 adalah',hasil)
hasil = b <=13
print(b,' <= 13 adalah' ,hasil)

print(' ================== Sama dengan 13')
hasil = a==13
print (a,'== 13 adalah',hasil)
hasil = b ==13
print (b,'== 13 adalah',hasil)

print(' ================== Tidak sama dengan 13')
hasil = a !=13
print(a,'!= 13 adalah',hasil)
hasil = b !=13
print(b,'!= 13 adalah',hasil)

print('============= NOT =============')
a=True
c=not a
print('a adalah',a)
print('------c = not a-------NOT')
print('c adalah ',c)

print('============= OR =============')
a=True
b=True
c=a or b
print(a,'OR ',b ,'menjadi',c)

a=True
b=False
c=a or b
print(a, 'OR',b,'menjadi',c)

a=False
b=True
c=a or b
print(a,'OR',b,'menjadi',c)

a=False
b=False
c=a or b
print(a,'OR',b,'menjadi',c)

print(' ============= AND =============')
a=True
b=True
c=a and b
print(a,'AND',b,'menjadi',c)

print('============= AND =============')
a=True
b=True
c=a and b
print(a,'AND',b,'menjadi',c)

a=False
b=True
c=a and b
print(a,'AND',b,'menjadi',c)

a = False
b = False
c=a and b
print(a,'AND',b,'menjadi',c)

print('============= XOR =============')
a=True
b=True
c= a^ b
print(a,'^',b,'menjadi',c)

a=True
b=False
c=a ^ b
print(a,'^',b,'menjadi',c)

a=False
b=True
c=a ^ b
print(a,'^',b,'menjadi',c)

a=False
b=False
c=a ^ b
print(a,'^',b,'menjadi',c )
# TUGAS
# Buat kode untuk masing masing operator berikut
print('============= NAND =============')
print('============= NOR ==============')
print('============= NXOR =============')

#print ('============= NAND =============')
print('==========','NAND','==========')
a = True
b = False
c = not(a and b)
print(a,'NAND',b,'menjadi',c)
a = True
b = True
c = not(a and b)
print(a,'NAND',b,'menjadi',c)
b = False
a = True
c = not(a and b)
print(a,'NAND',b,'menjadi',c)
a = False
b = False
c = not(a and b)
print(a,'NAND',b,'menjadi',c)

# print (' ============= NOR ============== ')
print('==========','NOR','==========')
a = True
b = False
c = not(a or b)
print(a,'NOR',b,'menjadi',c)
a = True
b = True
c = not(a or b)
print(a,'NOR',b,'menjadi',c)
b = False
a = True
c = not(a or b)
print(a,'NOR',b,'menjadi',c)
a = False
b = False
c = not(a or b)
print(a,'NOR',b,'menjadi',c)

# print (' ============= NXOR ============= ')
print('==========','NXOR','==========')
a = True
b = False
c = not(a ^ b)
print(a,'NXOR',b,'menjadi',c)
a = True
b = True
c = not(a ^ b)
print(a,'NXOR',b,'menjadi',c)
b = False
a = True
c = not(a ^ b)
print(a,'NXOR',b,'menjadi',c)
a = False
b = False
c = not(a ^ b)
print(a,'NXOR',b,'menjadi',c)

print()
print()

#operator identitas
print('============== IS')
a=5
b=5
print('Nilai a =',a,'Identitas =',hex(id(a)))
print('Nilai b =',b,'Identitas =',hex(id(b)))
hasil = a is b
print('a is b = ', hasil )

a=5
b=6

print('Nilai a =',a,'Identitas =',hex(id(a)))
print('Nilai b =',b,'Identitas =',hex(id(b)))
hasil = a is b
print('a is b =', hasil)

print('============== IS NOT')
a=5
b=5
print('Nilai a =',a,'Identitas =',hex(id(a)))
print('Nilai b =',b,'Identitas =',hex(id(b)))
hasil= a is not b
print('a is not b = ', hasil )

a=5
b=6
print('Nilai a =',a,'Identitas =',hex(id(a)))
print('Nilai b =',b,'Identitas =',hex(id(b)))
hasil = a is not b
print('a is not b = ', hasil )

print()
#operator Membership
print('======================= IN')
nama_lengkap = 'Bachariduddn jusuf Habibiie'
test = 'a'
cek = test in nama_lengkap
print(test+' terdapat di '+nama_lengkap+' adalah '+ str(cek))

test = 'rud'
cek = test in nama_lengkap
print(test+' terdapat di '+nama_lengkap +' adalah '+ str(cek))

test = 'bac'
cek = test in nama_lengkap
print(test +' terdapat di '+nama_lengkap +' adalah '+ str(cek))

print('======================= NOT IN ')
nama_lengkap = 'Bachariduddn jusuf Habibiie'
test = 'a'
cek = test not in nama_lengkap
print(test+' tidak terdapat di s' + nama_lengkap + ' adalah ' + str(cek))

test = 'rud'
cek = test not in nama_lengkap
print(test+' tidak terdapat di '+nama_lengkap +' adalah '+str(cek ))
      
test = 'bac'
cek = test not in nama_lengkap
print(test+' tidak terdapat di '+nama_lengkap +' adalah '+str(cek ))

#TUGAS
#Dengan cara yang sama buat operator in dan not in , ubah nama ←- lengkap menjadi nama masing-masing dengan uji test
# test1 = ab # pilih dua huruf berurut yang ada pada nama anda
print('==========','IN','==========')
nama_lengkap = "Rahmat efendi"
test = 'ah'
cek = test in nama_lengkap
print(test, 'terdapat di',nama_lengkap,'adalah',cek)

# test2 = ba # balik dua huruf tersebut
test = 'ha'
cek = test in nama_lengkap
print(test, 'terdapat di',nama_lengkap,'adalah',cek)

# test3 = 'a'
est = 'a'
cek = test in nama_lengkap
print(test, 'terdapat di',nama_lengkap,'adalah',cek)

# test4 = 'i'
test = 'i'
cek = test in nama_lengkap
print(test, 'terdapat di',nama_lengkap,'adalah',cek)

# test5 = 'u'
test = 'u'
cek = test in nama_lengkap
print(test, 'terdapat di',nama_lengkap,'adalah',cek)

# test6 = 'e'
test = 'e'
cek = test in nama_lengkap
print(test, 'terdapat di',nama_lengkap,'adalah',cek)

# test7 = '0'
test = 'o'
cek = test in nama_lengkap
print(test, 'terdapat di',nama_lengkap,'adalah',cek)

print('==========','NOT IN','==========')
nama_lengkap = "Rahmat efendi"
test = 'ah'
cek = test not in nama_lengkap
print(test, 'tidak terdapat di',nama_lengkap,'adalah',cek)

#test 2
test = 'ha'
cek = test not in nama_lengkap
print(test, 'tidak terdapat di',nama_lengkap,'adalah',cek)

# test3 = 'a'
test = 'a'
cek = test not in nama_lengkap
print(test, 'tidak terdapat di',nama_lengkap,'adalah',cek)

# test4 = 'i'
test = 'i'
cek = test not in nama_lengkap
print(test, 'tidak terdapat di',nama_lengkap,'adalah',cek)

# test5 = 'u'
test = 'u'
cek = test not in nama_lengkap
print(test, 'tidak terdapat di',nama_lengkap,'adalah',cek)

# test6 = 'e'
test = 'e'
cek = test not in nama_lengkap
print(test, 'tidak terdapat di',nama_lengkap,'adalah',cek)

# test7 = '0'
test = 'o'
cek = test not in nama_lengkap
print(test, 'tidak terdapat di',nama_lengkap,'adalah',cek)



#operator Bitwise
a=1 # ubah manjadi tanggal lahir anda
a +=60
b=5 # ubah manejadi bulan lahir
b+= 90
print('=============================OR')
print('Nilai',a,'dalam biner   = ',format(a,'08b'))
print('----------------------------(|)')
hasil=a|b
print('Nilai',a,'|',b,'dalam biner =', format(hasil,'08b'))

print('============================= AND')
print('Nilai',a, 'dalam biner     = ', format(a,'08b'))
print('Nilai',b, 'dalam biner     = ', format(a,'08b'))
print('----------------------------(&)')
hasil = a & b
print('Nilai',a,'&',b, 'dalam biner = ', format(hasil,'08b'))

print('=============================XOR')
print('Nilai',a,'dalam biner = ', format (a,'08b'))
print('Nilai',b,'dalam biner = ', format (b,'08b'))
print('----------------------------(^)')
hasil = a ^ b
print('Nilai',a,'^',b, 'dalam biner = ', format(hasil,'08b'))

print('=============================NOT')
print('Nilai',a,'dalam biner =', format(a, '08b'))
print('------------------------(~a)')
hasil = ~a
print('Nilai ~',a ,'dalam biner = ', format ( hasil ,'08b'))

print('Nilai',b,'dalam biner = ', format (b ,'08b'))
print('------------------------(~b)')
hasil = ~b
print('Nilai ~',b,'dalam biner = ', format ( hasil ,'08b'))

print('=============================>>')
print('Nilai ',a ,'dalam biner = ', format (a ,'08b'))
print('--------------------------( > >2)')
hasil = a >> 2
print('Nilai',a,'>>2 dalam biner = ', format ( hasil ,'b'))

print('Nilai ',b,'dalam biner = ', format (b ,'8b') )
print('--------------------------(>>2)')
hasil = b >> 2
print('Nilai',b, '>>2 dalam biner = ', format(hasil,'08b'))

print('=============================<<')
print('Nilai ',a,'dalam biner = ', format (a ,'08b'))
print('--------------------------(<<2)')
hasil = a << 2
print('Nilai ',a,' <<2 dalam biner = ', format ( hasil ,'08b'))

print('Nilai' ,b,'dalam biner = ', format (b ,'08b'))
print ('--------------------------(<<2)')
hasil = b << 2
print ('Nilai ',b ,' <<2 dalam biner = ', format ( hasil ,'08b'))

#TUGAS 
a=35
a +=51
b=84
b+=89
print('=============================NOT AND')
print('Nilai",a,"dalam biner=' , format(a,'08b'))
print("Nilai",b,"dalam biner=" , format(b,"08b"))
print("--------------------------(&)")
hasil=a&b
print("Nilai",a,"&",b,"dalam biner", format (hasil,"08b"))

print('=============================NOT OR')
print("Nilai",a,"dalam biner=", format(a,"08b"))
print("Nilai",b,"dalam biner=" ,format(b,"08b"))
print("--------------------------(|)")
hasil=a|b
print("Nilai",a,"|",b,"dalam biner", format (hasil,"08b"))

print('=============================NOT XOR')
print("Nilai",a,"dalam biner=", format(a,"08b"))
print("Nilai",b,"dalam biner=" ,format(b,"08b"))
print("--------------------------(^)")
hasil=a^b
print("Nilai",a,"^",b,"dalam biner", format (hasil,"08b"))

print('=============================NOT (>>2)')
print("Nilai",a,"dalam biner=", format(a,"08b"))
print("--------------------------(>>2)")

print('=============================NOT (<<2)')
print("Nilai",a,"dalam biner=", format(a,"08b"))
print("--------------------------(>>2)")
hasil=a >>2
print("Nilai~",a,">>2 dalam biner=", format(hasil,"08b"))
print("Nilai",b,"dalam biner=", format(b,"08b"))
print("--------------------------(>>2)")
hasil=b >>2
print("Nilai~",b,">>2 dalam biner=", format(hasil,"08b"))

