bilangan = int(input('jika bilangan : '))

if bilangan > 0:
    if bilangan % 2 == 0:
        print(bilangan, 'adalah bilangan positif genap')
    else:
        print(bilangan, 'adalah bilangan positif ganjil')
else:
    print(bilangan, 'adalah bilangan negatif')