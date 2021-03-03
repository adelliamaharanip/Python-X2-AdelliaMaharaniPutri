#Pengulangan while #syarat

count = 0
while count < 11:
    print('perulangan ke ', count)
    count += 1 # berfungsi untuk penambahan nilai count
    if count % 3 == 0:
        break #memberhentikan, karena sudah memenuhi syarat baru
print('stop')


#count += 1
#jika ini tidak ada, maka hasilmya akan true terus menerus dan count awal tidak bertambah (nol terus)

#continue
#berfungsi untuk melewati