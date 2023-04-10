#Menu

print('**************************************')
print('Selamat Datang di Program Bangun Datar')
print('======================================')
print('Pilih bangun datar :')
print('1. Segitiga')
print('2. Lingkaran')
print('3. Persegi')
print('4. Persegi Panjang')
pilihan = input('Pilih Bangun Datar :')

#Segitiga

if pilihan == '1':
    print('Pilih salah satu :')
    print('1. Luas Segitiga')
    print('2. Keliling Segitiga')
    jawaban = input('Masukkan pilihan :')
    
    if jawaban == '1':
        print('    Menghitung Luas Segiitiga   ')
        print('================================')
        a = float(input('Masukkan Alas :'))
        t = float(input('Masukkan Tinggi :'))
        l = (0.5 * a * t)
        print('================================')
        print('Luas segitiga dari alas' ,int(a),'cm','dan tinggi',int(t),'cm', 'adalah',l,'cm')
        print('Terima kasih telah menggunakan program saya:)')

    elif jawaban == '2':
        print('  Menghitung Keliling Segiitiga  ')
        print('=================================')
        a = float(input('Masukkan Alas :'))
        t = float(input('Masukkan Tinggi :'))
        s = float(input('Masukkan Sisi Miring :'))
        k = a + t + s
        print('=================================')
        print('Keliling segitiga dari alas' ,int(a),'cm','tinggi',int(t),'cm', 'dan sisi miring',int(s),'cm','adalah',k,'cm')
        print('Terima kasih telah menggunakan program saya:)')
    
    else:
        print('Masukkan jawaban yang sudah tersedia di menu dek!')

#Lingkaran

elif pilihan == '2':
    print('Pilih salah satu :')
    print('1. Luas Lingkaran')
    print('2. Keliling Lingkaran')
    jawaban = input('Masukkan pilihan :')

    if jawaban == '1':
        print('  Menghitung Luas Lingkaran  ')
        print('=============================')
        r = float(input('Masukkan jari-jari :'))
        l = (3.14 * r * r)
        print('=============================')
        print('Luas lingkaran dari jari-jari' ,int(r),'cm','adalah',l,'cm')
        print('Terima kasih telah menggunakan program saya:)')

    elif jawaban == '2':
        print('  Menghitung Keliling Lingkaran  ')
        print('=================================')
        d = float(input('Masukkan diameter / 2 x jari-jari :'))
        k =  3.14 * d
        print('=================================')
        print('Keliling lingkaran dari diameter',int(d),'cm','adalah',k,'cm')
        print('Terima kasih telah menggunakan program saya:)')

    else:
        print('Masukkan jawaban yang sudah tersedia di menu dek!')    

#Persegi

elif pilihan == '3':
    print('Pilih salah satu :')
    print('1. Luas Persegi')
    print('2. Keliling Persegi')
    jawaban = input('Masukkan pilihan :')

    if jawaban == '1':
        print('  Menghitung Luas Persegi  ')
        print('===========================')
        s = float(input('Masukkan Sisi :'))
        l = (s * s)
        print('===========================')
        print('Luas persegi yang memiliki sisi' ,int(s),'cm','adalah',l,'cm')
        print('Terima kasih telah menggunakan program saya:)')

    elif jawaban == '2':
        print('  Menghitung Keliling Persegi  ')
        print('===============================')
        s = float(input('Masukkan Sisi :'))
        k = 4 * s
        print('===============================')
        print('Keliling persegi yang memiliki sisi' ,int(s),'cm','adalah',k,'cm')
        print('Terima kasih telah menggunakan program saya:)')
    
    else:
        print('Masukkan jawaban yang sudah tersedia di menu dek!')

#Persegi Panjang

elif pilihan == '4':
    print('Pilih salah satu :')
    print('1. Luas persegi panjang')
    print('2. Keliling persegi panjang')
    jawaban = input('Masukkan pilihan :')

    if jawaban == '1':
        print('  Menghitung Luas Persegi Panjang  ')
        print('===================================')
        p = float(input('Masukkan Panjang :'))
        b = float(input('Masukkan Lebar :'))
        l = (p * b)
        print('===================================')
        print('Luas persegi panjang dari panjang' ,int(p),'cm','dan lebar',int(b),'cm', 'adalah',l,'cm')
        print('Terima kasih telah menggunakan program saya:)')

    elif jawaban == '2':
        print('  Menghitung Keliling Persegi Panjang  ')
        print('=======================================')
        p = float(input('Masukkan Panjang :'))
        b = float(input('Masukkan Lebar :'))
        k = (2 * p) + (2 * b)
        print('=======================================')
        print('Keliling persegi panjang dari panjang' ,int(p),'cm','dan lebar',int(b),'cm','adalah',k,'cm')
        print('Terima kasih telah menggunakan program saya:)')
    
    else:
        print('Masukkan jawaban yang sudah tersedia di menu dek!')

else:
        print('Masukkan jawaban yang sudah tersedia di menu dek!')

