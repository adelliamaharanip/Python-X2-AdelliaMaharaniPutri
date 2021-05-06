#menampilkan deret fibonancy
 
def deret_fibo(n):
    if n <= 1:
        return n
    else:
        return(deret_fibo(n-1) + deret_fibo(n-2))
    
jumlah_deret = int(input('jumlah deret : '))
 
if jumlah_deret <= 0:
    print ('masukkan bilangan bulat positif')
else:
    print ('deret fibonanci : ')
    for i in range(jumlah_deret):
        print (deret_fibo(i))
