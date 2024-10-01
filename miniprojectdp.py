print('selamat datang di pandawa store ')
print('silahkan login terlebih dahulu')
username = input('username: ')
password = input('password: ')
print('\n------ DATA DIKONFIRMASI ------')

while True:
    username2 = input('username: ')
    password2 = input('password: ')

    if username == username2 and password == password2:
        print('\nanda berhasil login')
        nama_barang = input('masukkan nama barang: ')
        harga = int(input('masukkan harga: '))
        jumlah_barang = int(input('masukkan jumlah barang: '))
        total_harga = harga * jumlah_barang
        if total_harga >= 250000:
            diskon = total_harga * 0.25
            total = total_harga + diskon
            print ("anda mendapat diskon 25% = ", total)
        else:
            print('anda tidak mendapat diskon')
        print('silahkan pilih menu di bawah ini')
        print('1.mengulang program \n2.exit')
        pilihan=int(input('masukkan pilihan: '))
        if pilihan == 1:
            print('silahkan login terlebih dahulu')
        elif pilihan == 2:
            break 
        else:
            print('anda salah memasukkan pilihan')
    else:
        print('anda gagal login') 
