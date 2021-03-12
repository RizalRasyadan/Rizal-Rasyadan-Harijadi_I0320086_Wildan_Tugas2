
def  pspanjang():
    print("Selamat Datang")
    print("Silahkan Masukan Panjang")
    x=float(input("Panjang :"))
    print("Silahkan Masukan Lebar Persegi Panjang")
    y=float(input("Lebar :"))
    print("Luas Persegi Panjang adalah")
    print(x*y)

def lingkaran():
    phi=3.14
    print("Selamat Datang")
    print("Silahkan Masukan Jari-Jari")
    r=float(input("Jari-Jari :"))
    print("Luas Lingkaran adalah")
    print(phi*(r**2))

def persegi():
    print("Selamat Datang")
    print("Silahkan Masukan Sisi")
    s=float(input("Sisi :"))
    print("Luas Persegi :")
    print(s**2)

def celciustofahrenhait():
    print("Selamat Datang")
    print("Silahkan Masukan Suhu")
    c=float(input("Suhu (Celcius): "))
    f= ((9/5)*c)+32
    print("Suhu Fahrenhait adalah")
    print(f)

def reamurtokelvin():
    print("Selamat Datang")
    print("Silahkan Masukan Suhu")
    re=float(input("Suhu Reamur): "))
    k= ((5/4)*re)+273
    print("Suhu Kelvin adalah")

def menu():
    print("Silahkan Pilih Fungsi dari Program ini")
    print("1. Menghitung Luas Persegi Panjang")
    print("2. Menghitung Luas Lingkaran")
    print("3. Menghitung Luas Persegi")
    print("4. Menghitung Suhu Celcius ke Fahrenhait")
    print("5. Menghitung Suhu Reamur to Kelvin")
    pilihan=int(input("Pilihan : "))
    select(pilihan)

def select(pilih):
    if pilih == 1:
        pspanjang()
    elif pilih == 2:
        lingkaran()
    elif pilih == 3:
        persegi()
    elif pilih == 4:
        celciustofahrenheit()
    elif pilih == 5:
        reamurtokelvin()
    else:
        print("Pilihan Tidak Valid")
    menu()

menu()

