makanan = ['nasi rames', 'nasi rawon', 'nasi pecel', 'nasi tempong']
minuman = ['es jeruk', 'es teh', 'es temulawak', 'es nutrisari']
camilan = ['tahu walek', 'gorengan mix']
keranjang = []

print('=====================================')
print('=          WARTEG MBOK NYI          =')
print('=Menjawab semua kebutuhan perut anda=')
print('=   -----------------------------   =')
print('=                                   =')
print('= silahkan pilih menu yang tersedia =')
print('=====================================\n Silahkan pilih menu dibawah :')

while True:
    menu = input('=   1. makanan             =\n=   2. minuman             =\n=   3. camilan             =\n pilih menu [1-3]')
    if menu == '1':
        print('\nMAKANAN')
        print('Silahkan anda pilih yang anda suka')
        while True:
            for ii in range(0, len(makanan)):
                print(f'{ii + 1}. {makanan}')
                list_makanan = int(input('pilih menu [1 - 4]'))
                if list_makanan == 1:
                    keranjang.append(makanan[0])
                    print('\n=== Hidangan anda ===')
                    for a in range(0, len(keranjang)):
                        print(f'= {a + 1}. {makanan[a]}  x1 =')
                    break
                elif list_makanan == 2:
                    keranjang.append(makanan[1])
                    print('\n=== Hidangan anda ===')
                    for a in range(0, len(keranjang)):
                        print(f'= {a + 1}. {makanan[a]}  x1 =')
                    break
                elif list_makanan == 3:
                    keranjang.append(makanan[2])
                    print('\n=== Hidangan anda ===')
                    for a in range(0, len(keranjang)):
                        print(f'= {a + 1}. {makanan[a]}  x1 =')
                    break
                elif list_makanan == 4:
                    keranjang.append(makanan[3])
                    print('\n=== Hidangan anda ===')
                    for a in range(0, len(keranjang)):
                        print(f'= {a + 1}. {makanan[a]}  x1 =')
                    break
                else:
                    print('menu tidak dapat di temukan')
                    continue
    elif menu == '2':
        print('\nMINUMAN')
        print('Silahkan anda pilih yang anda suka')
        while True:
            for ii in range(0, len(minuman)):
                print(f'{ii + 1}. {minuman}')
                list_minuman = int(input('pilih menu [1 - 4]'))
                if list_minuman == 1:
                    keranjang.append(minuman[0])
                    print('\n=== Hidangan anda ===')
                    for a in range(0, len(keranjang)):
                        print(f'= {a + 1}. {minuman[a]}  x1 =')
                    break
                elif list_minuman == 2:
                    keranjang.append(minuman[1])
                    print('\n=== Hidangan anda ===')
                    for a in range(0, len(keranjang)):
                        print(f'= {a + 1}. {minuman[a]}  x1 =')
                    break
                elif list_minuman == 3:
                    keranjang.append(minuman[2])
                    print('\n=== Hidangan anda ===')
                    for a in range(0, len(keranjang)):
                        print(f'= {a + 1}. {minuman[a]}  x1 =')
                    break
                elif list_minuman == 4:
                    keranjang.append(minuman[3])
                    print('\n=== Hidangan anda ===')
                    for a in range(0, len(keranjang)):
                        print(f'= {a + 1}. {minuman[a]}  x1 =')
                    break
                else:
                    print('menu tidak dapat di temukan')
                    continue
    elif menu == '3':
        print('\nCAMILAN')
        print('Silahkan anda pilih yang anda suka')
        while True:
            for ii in range(0, len(camilan)):
                print(f'{ii + 1}. {camilan}')
                list_camilan = int(input('pilih menu [1 - 2]'))
                if list_camilan == 1:
                    keranjang.append(camilan[0])
                    print('\n=== Hidangan anda ===')
                    for a in range(0, len(keranjang)):
                        print(f'= {a + 1}. {camilan[a]}  x1 =')
                    break
                elif list_camilan == 2:
                    keranjang.append(camilan[1])
                    print('\n=== Hidangan anda ===')
                    for a in range(0, len(keranjang)):
                        print(f'= {a + 1}. {camilan[a]}  x1 =')
                    break
                else:
                    print('menu tidak dapat di temukan')
                    continue
    Tambah = input('ada menu yang perlu di tambahkan? (y/n)')
    if Tambah == 'y' or Tambah == 'Y':
        continue
    else:
        print('\nTerimakasih, silahkan cari tempat duduk yang kosong dan pesanan akan segera diantar')
        break