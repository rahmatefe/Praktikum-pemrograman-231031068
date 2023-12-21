print('pratikum 3')

nama = 'rahmat efendi'
nim  = '231031068'
meet = 'pratikum 3 (String)'
prodi = 'Sistem Informasi C'
email = 'rahmatefendi15@smk.belajar.id'
TTL = 'Barru, 01-05-2005'
Alamat = 'Pacciro, jl pahlawan'
Asal = 'Barru'
hobi = 'Volly'
tinggi = '170'
sp = 40
print("-"*sp)
print(nama.upper().center(sp))
print(nim.center(sp))
print('\n')
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.lower().rjust(sp))
print("-"*sp)

print(f'''\tHelo, nama saya {nama} dengan NIM {nim} dari Prodi {prodi} ini adalah file {meet} . Terima kasih.\n''')

print(f'''Biodata saya,
nama\t: {nama.upper() } 
NIM \t: {nim}
prodi\t: {prodi}
TTL \t: {TTL}
Alamat\t: {Alamat}
Asal\t: {Asal}
hobi\t: {hobi}
tinggi\t: {tinggi}
''')

#Tugas pratikum 3
stat1 = 'duFort Frankel Sir Issac'
# Issac duFort Frankel Sir

stat2 = 'duFort Frankel Sir Issac'
# d F S Issac

stat3 = 'duFort Frankel Sir Issac'
# duFort F S I

stat4 = 'duFort Frankel Sir Issac'
# I duFort Frankel Sir

stat5 = 'duFort Frankel Sir Issac'
# Issac d F S

stat6 = 'duFort Frankel Sir Issac'
# ISSAC D F S

stat7 = '#duFort Frankel Sir Issac$'
# duFort Frankel Sir Issac

stat8 = '#duFort-Frankel-Sir-Issac$'
# duFort Frankel Sir Issac

stat9 = '#duFort@ ^Frankel* (Sir( (Issac$'
# duFort Frankel Sir Issac

stat10 = '#duFort@-^Frankel*-(Sir(-(Issac$'
# DUFORT FRANKEL SIR ISSAC


# Stat1: Issac duFort Frankel Sir
stat1 = 'duFort Frankel Sir Issac'
result1 = stat1.split()
result1 = result1[-1] + ' ' + ' '.join(result1[:-1])
print(result1)

# Stat2: d F S Issac
stat2 = 'duFort Frankel Sir Issac'
result2 = stat2.split()
result2 = ' '.join([word[0] for word in result2]) + ' ' + result2[-1]
print(result2)

# Stat3: duFort F S I
stat3 = 'duFort Frankel Sir Issac'
result3 = stat3.split()
result3 = ' '.join([word if word == 'duFort' else word[0] for word in result3])
print(result3)

# Stat4: I duFort Frankel Sir
stat4 = 'duFort Frankel Sir Issac'
result4 = stat4.split()
result4 = result4[-1] + ' ' + ' '.join(result4[:-1])
result4 = result4[0] + ' ' + result4[1:]
print(result4)

# Stat5: Issac d F S
stat5 = 'duFort Frankel Sir Issac'
result5 = stat5.split()
result5 = result5[-1] + ' ' + ' '.join(result5[:-1])
result5 = result5[0] + ' ' + result5[1:]
print(result5)

# Stat6: ISSAC D F S
stat6 = 'duFort Frankel Sir Issac'
result6 = stat6.split()
result6 = result6[-1].upper() + ' ' + ' '.join([word[0].upper() for word in result6[:-1]])
print(result6)

# Stat7: duFort Frankel Sir Issac
stat7 = '#duFort Frankel Sir Issac$'
result7 = ''.join([c for c in stat7 if c.isalpha() or c.isspace()])
print(result7)

# Stat8: duFort Frankel Sir Issac
stat8 = '#duFort-Frankel-Sir-Issac$'
result8 = ''.join([c for c in stat8 if c.isalpha() or c.isspace() or c == '-'])
print(result8)

# Stat9: duFort Frankel Sir Issac
stat9 = '#duFort@ ^Frankel* (Sir( (Issac$'
result9 = ''.join([c for c in stat9 if c.isalpha() or c.isspace()])
print(result9)

# Stat10: DUFORT FRANKEL SIR ISSAC
stat10 = '#duFort@ -^Frankel* -(Sir(-(Issac$'
result10 = ''.join([c for c in stat10 if c.isalpha() or c.isspace()])
result10 = result10.upper()
print(result10)