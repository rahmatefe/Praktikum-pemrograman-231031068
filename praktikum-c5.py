import os
os.system('clear')
 
a = True
limit = 5
i = 0            # 1.2.3.....limit

while a:
    i += 1 # i =i + 1
    print(f'menjalankan program {limit + 1 - i } ')
    if i == limit:
        a = False
        print('program berhenti disini!')
    else:
        a = True

#while a:
#    i = i+i
#    if i <= limit:
#        print('menjalankan program')
#        a = True
#    else:
#        a = False


