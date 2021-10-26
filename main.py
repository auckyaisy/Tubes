
import sys
import time

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()
# state_saklar = int(input("Apabila anda ingin menggunakan mesin cuci, maka ketik 1 lalu enter\nuntuk menyalakan saklar."))
# if state_saklar == 1:
#     bool_saklar = True
# else:
#     bool_saklar = False

# print("Halo, selamat datang di mesin cuci laundry")
# print("1. Nyalakan Mesin Cuci")
# print("0. Keluar")
# # menu_laundry = int(input("Silahkan pilih: "))

# masukkan sesuatu yang ingin dicuci
# 1, baju
# 2. celana
# 3. lain-lain
# 4. selesai

# [kaos, kemeja,  ]


# baju
# kaos = 300
# kemeja = 300
# sweater/ hoodie = 300
# gaun = 300
# jaket = 300
# mantel = 300
# singlet 300 
# gamis 300
# jersey 300
# polo 300
# singlet 300

# celana
# jeans = 300 gram
# kulot 300 
# boxer 300 
# rok 300
# chino 300
# jogger 300 
# cargo 300
# formal
# celana dalam

# lain-lain
# seprei = 700g
# sarung bantal = 200g
# sarung guling = 200g
# selimut = 700g
# sarung tangan = 100g

# list = ["kaos"]
# baju
# kaos = 300
# kemeja = 300
# sweater/ hoodie = 300
# gaun = 300
# jaket = 300
# mantel = 300
# singlet 300 
# gamis 300
# jersey 300
# polo 300
# singlet 300

# print baju yang dimasukkan: 5 terakhir, menu list baju
# print("1. Baju")
# print("2. Celana")
# print("3. Lain-lain")
# print("4. Selesai memasukkan")
list_cucian = []
selesai = False
print("Selanjunya, silakan masukkan sesuatu yang akan dicuci.\nApabila sudah selesai, silakan isikan 'selesai' tanpa tanda petik.")
while (selesai == False):
    if len(list_cucian) > 0:
        print(f"Cucian yang telah dimasukkan: {list_cucian}")
    temp_baju = input("Masukkan sesuatu yang akan dicuci: ")
    if temp_baju == "selesai" or temp_baju == "Selesai":
        selesai = True
    list_cucian.append(temp_baju)


data_metode_cuci = [
    {
        "nama": "Cotton",
        "waktu": 30,
        "putaran": 100,
        "suhu": 60
    },
        {
        "nama": "Sports Wear",
        "waktu": 54,
        "putaran": 800,
        "suhu": 40
    },
        {
        "nama": "Mix",
        "waktu": 40,
        "putaran": 800,
        "suhu": 40
    },
        {
        "nama": "Wool",
        "waktu": 35,
        "putaran": 800,
        "suhu": 40
    },
        {
        "nama": "Baby Care",
        "waktu": 20,
        "putaran": 800,
        "suhu": 60
    },
        {
        "nama": "Duvet",
        "waktu": 100,
        "putaran": 800,
        "suhu": 40
    },
        {
        "nama": "Intensive 60",
        "waktu": 60,
        "putaran": 800,
        "suhu": 60
    },
        {
        "nama": "Quick 30",
        "waktu": 30,
        "putaran": 800,
        "suhu": 30
    },
            {
        "nama": "Rinse+Spin",
        "waktu": 18,
        "putaran": 1000,
        "suhu": 20
    },

]

print("Selanjutnya, silakan pilih metode untuk mencuci baju")
print("1. Cotton")
print("2. Sports Wear")
print("3. Mix")
print("4. Wool")
print("5. Baby Care")
print("6. Duvet")
print("7. Intensive 60")
print("8. Quick 30")
print("9. Rinse+Spin")
metode_cuci = int(input("Masukkan metode yang dipilih : "))

print()
print("Metode yang dipilih adalah:")
print("Metode:", data_metode_cuci[metode_cuci - 1]["nama"])
print("Waktu mencuci:", data_metode_cuci[metode_cuci - 1]["waktu"])
print("Putaran mesin dalam mencuci:", data_metode_cuci[metode_cuci - 1]["putaran"])
print("Apakah anda ingin putaran mesin dalam mencuci, masukkan angka 1 apabila iya dan 0 apabila tidak.")
ubah_putaran = int(input("1/0 (Ya/Tidak): "))
if ubah_putaran == 1:
    print("Pilih putaran yang diinginkan")
    print("1. 1000")
    print("2. 800")
    print("3. 400")
    print("4. 0")
    putaran_mesin = int(input("Masukkan putaran yang diinginkan: "))
print("Suhu dalam mencuci:", data_metode_cuci[metode_cuci - 1]["suhu"])
print("Apakah anda ingin mengubah suhu dalam mencuci, masukkan angka 1 apabila iya dan 0 apabila tidak.")
ubah_putaran = int(input("1/0 (Ya/Tidak): "))
if ubah_putaran == 1:
    print("Pilih suhu yang diinginkan")
    print("1. 95")
    print("2. 60")
    print("3. 40")
    print("4. 30")
    print("5. 20")
    putaran_mesin = int(input("Masukkan suhu yang diinginkan: "))
print()
print("Metode " + data_metode_cuci[metode_cuci - 1]["nama"] + ": " + str(data_metode_cuci[metode_cuci - 1]["waktu"])+ " Menit " + str(data_metode_cuci[metode_cuci - 1]["putaran"]) + " Putaran " + str(data_metode_cuci[metode_cuci - 1]["suhu"]) + " derajat celcius.")

tutup_mesin = 0
while tutup_mesin == 0:
    print("Status tutup mesin cuci: Terbuka")
    print("Silahkan tekan 1 untuk menutup mesin cuci, mesin cuci hanya akan berproses apabila tutup terkunci")
    tutup_mesin = int(input("Masukan: "))
print("Status tutup mesin cuci: Tertutup & Terkunci")


print("Mesin cuci akan memproses pencucian baju, mungkin mesin akan sedikit bergetar.")
for i in progressbar(range(15), "Proses: ", 20):
    time.sleep(0.5)

sudah_dicuci = []

    



# print(selesai, list_cucian)

# berat_baju = int(input("Masukkan berat baju yang akan dicuci (kg): "))



