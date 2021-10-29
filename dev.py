
import sys
import time
from collections import Counter

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

def cekInput(datatype,string, errormsg):
    error = False
    if datatype == 'int':
        while not error:
            try:
                masukan = int(input(string))
            except:
                print(errormsg)
            else:
                error = True
                return masukan
            # if input.is_integer():
            #     error = True
    elif datatype == 'string':
        while not error:
            try:
                masukan = string(input(string))
            except:
                print(errormsg)
            else:
                error = True
                return masukan
            # if input.is_string():
            #     error = True

# def saklar():
#     print("Apabila anda ingin menggunakan mesin cuci, maka masukkan y untuk menyalakan saklar dan n untuk keluar")
#     state_saklar = input("Masukan (y/n): ")
#     if state_saklar == 'y':
#         return True

# def menu():
#     print("Halo, selamat datang di mesin cuci laundry")
#     print("1. Nyalakan Mesin Cuci")
#     print("0. Keluar")
#     menu_laundry = int(input("Silahkan pilih: "))

# masukkan sesuatu yang ingin dicuci
# 1, baju
# 2. celana
# 3. lain-lain
# 4. selesai

# [kaos, kemeja,  ]


jenis_cucian = ["baju", 
"kaos",
"kemeja",
"sweater",
"hoodie",
"gaun",
"jaket",
"mantel",
"celana",
"singlet",
"gamis",
"jersey",
"polo",
"singlet",
"celana",
"jeans",
"kulot",
"boxer",
"rok",
"chino",
"jogger", 
"cargo",
"formal",
"celana dalam",
"sempak",
"seprei",
"sarung bantal",
"sarung",
"sarung guling",
"selimut",
"sarung tangan"]

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
list_selimut = []

def banyakCucian(input, x=None, y=None):
    count_cuci = Counter(input)
    for count in count_cuci:
        if count == "seprei" and x != None:
            print("-",count.capitalize(), "sebanyak", count_cuci[count] * x)
        if count == "selimut" and y != None:
            print("-",count.capitalize(), "sebanyak", count_cuci[count] * y)
        else:
            print("-",count.capitalize(), "sebanyak", count_cuci[count])
    print()

def masukCucian():
    selesai = False
    print("Silakan masukkan sesuatu yang akan dicuci.\nApabila sudah selesai, silakan isikan 'selesai' tanpa tanda petik.")
    while (selesai == False):
        error = False
        bool_baju = False
        if len(list_cucian) > 0:
            print(f"Cucian yang telah dimasukkan:")
            banyakCucian(list_cucian)
        temp_baju = input("Masukkan sesuatu yang akan dicuci: ")
        if temp_baju.lower() == "selesai":
            if len(list_cucian) != 0:
                selesai = True
                break
            else:
                error = True
                print("Masukkan sesuatu terlebih dahulu sebelum lanjut!")
        if not error:
            pisah = temp_baju.split()
            for jenis in jenis_cucian:
                if jenis in pisah:
                    bool_baju = True
                    break
                else:
                    error = True
            if error and not bool_baju:
                print("Maaf kami tidak bisa mencuci barang ini.")
        if bool_baju:
            banyak_baju = cekInput("int","Berapa banyak yang akan dicuci: ", "Anda memasukkan jumlah yang salah!")
            if banyak_baju < 1:
                error = True
                print("Anda memasukkan jumlah yang salah!")
            for i in range(banyak_baju):
                    list_cucian.append(temp_baju)



# print(list_cucian)

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




def metodeCuci():
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
    metode_cuci = cekInput("int", "Masukkan metode yang dipilih (nomor pilihan): ", "Maaf anda memasukkan pilihan yang salah!")
    print(metode_cuci)
    if 0 < metode_cuci or 10 > metode_cuci:
        print()
        print("Metode yang dipilih adalah:",data_metode_cuci[metode_cuci - 1]["nama"])
        print("Waktu mencuci:", data_metode_cuci[metode_cuci - 1]["waktu"],"menit")
        print("Putaran mesin dalam mencuci:", data_metode_cuci[metode_cuci - 1]["putaran"], "rpm")
        print("Suhu air cucian:", data_metode_cuci[metode_cuci - 1]["suhu"], "derajat Celcius")
        print()
        return metode_cuci
    else:
        print()
        print("Anda memasukkan nomor pilihan yang salah!")
        print("====================================================")
        metodeCuci()


def pilihan(pilihan_list, nama_pilihan, satuan):
    print()
    print(f"Pilih {nama_pilihan} yang diinginkan")
    for i in range (0, len(pilihan_list)):
        print(f"{i + 1}. {pilihan_list[i]} {satuan}")
    pilih_pilihan = int(input(f"Masukkan {nama_pilihan} yang diinginkan (nomor pilihan): "))
    return pilih_pilihan - 1

def gantiMetode(metode_cuci):
    print("Apakah sudah sesuai dengan pilihan anda?")
    if not masukan():
        print()
        metodeCuci()
    bool_pilihan = True
    while bool_pilihan:
        print()
        print("Putaran mesin dalam mencuci:", data_metode_cuci[metode_cuci - 1]["putaran"], "rpm")
        print("Apakah anda ingin mengganti putaran mesin dalam mencuci?")
        ubah_putaran = masukan()
        bool_putaran = True
        putaran = [1000, 800, 400, 0]
        if ubah_putaran:
            while bool_putaran == True:
                pilih_putaran = pilihan(putaran, "putaran", "rpm")
                try:
                    data_metode_cuci[metode_cuci - 1]["putaran"] = putaran[pilih_putaran]
                    bool_putaran = False
                except:
                    print("Silakan pilih putaran sesuai dengan pilihan yang diberikan.")

        suhu = [95, 60, 40, 30, 20]
        print()
        print("Suhu dalam mencuci:", data_metode_cuci[metode_cuci - 1]["suhu"], "derajat Celcius")
        print("Apakah anda ingin mengubah suhu dalam mencuci?")
        ubah_suhu = masukan()
        if ubah_suhu:
            pilih_suhu = pilihan(suhu, "suhu", "derajat Celcius")
            try:
                data_metode_cuci[metode_cuci - 1]["suhu"] = suhu[pilih_suhu]
                bool_putaran = False
            except:
                print("Silakan pilih putaran sesuai dengan pilihan yang diberikan.")

        print()
        print("Metode " + data_metode_cuci[metode_cuci - 1]["nama"] + ": " + str(data_metode_cuci[metode_cuci - 1]["waktu"])+ " Menit, " + str(data_metode_cuci[metode_cuci - 1]["putaran"]) + " Putaran, " + str(data_metode_cuci[metode_cuci - 1]["suhu"]) + " derajat celcius.")
        print("Apakah sudah sesuai?")
        if masukan():
            bool_pilihan = False
            print()


def statusMesin():
    tutup_mesin = "n"
    while tutup_mesin == "n":
        print("Status tutup mesin cuci: Terbuka")
        print("Silahkan masukkan y untuk menutup mesin cuci, mesin cuci hanya akan berproses apabila tutup terkunci")
        tutup_mesin = input("Masukan: ")
        if tutup_mesin.lower() != "y":
            tutup_mesin = "n"
            print("Mesin cuci tidak dapat bekerja")
            print()
    print()
    print("Status tutup mesin cuci: Tertutup & Terkunci")

sudah_dicuci = []
jumlah_cucian = (len(list_cucian) - 1)

def masukan():
    print("Masukkan y untuk ya dan n untuk tidak")
    masukan = input("Masukan (y/n): ")
    if masukan.lower() == 'y':
        return True
    else:
        return False

def cekSelimut():
    i = 0
    while i < len(list_cucian):
        if list_cucian[i].lower() == "seprei" or list_cucian[i].lower() == "selimut":
            list_selimut.append(list_cucian[i])
            list_cucian.remove(list_cucian[i])
            i -= 1
        else:
            i += 1
            
def cekSeprei():
    
    for list in list_cucian:
        if list.lower() == "seprei" or list.lower() == "selimut":
            return True

def prosesCuci():
    print("Mesin cuci akan memproses pencucian baju, mungkin mesin akan sedikit bergetar.")
    banyak_dicuci = 20
    if len(list_cucian) < banyak_dicuci:
        banyak_dicuci = len(list_cucian)
    for i in progressbar(range(banyak_dicuci), "Proses: ", 20):
        sudah_dicuci.append(list_cucian.pop(0))
        # if i != (jumlah_cucian):
        #     continue
        # else:
        #     sudah_dicuci.append(list_cucian.pop(0))
        # if i <= (len(list_cucian) - 1):
            # sudah_dicuci.append(list_cucian.pop(i))
        time.sleep(0.5)
    print()
    print("Tutup mesin cuci telah terbuka, silakan keluarkan cucian yang telah selesai dicuci!")
    print(f"Baju yang telah selesai dicuci adalah:")
    banyakCucian(sudah_dicuci)
    

# print(len(list_cucian))
# banyak_dicuci = 9
# if len(list_cucian) < banyak_dicuci:
#     banyak_dicuci = len(list_cucian)
# for i in range(0, banyak_dicuci):
#     print("Cuci")
#     sudah_dicuci.append(list_cucian.pop(0))
#     # print(list_cucian)
# # print(sudah_dicuci)
# print(f"Baju yang telah selesai dicuci adalah {sudah_dicuci}")

def ulangCuci():
    bool_selimut = False
    jumlah_selimut = 0
    jumlah_seprei = 0
    jumlah_pop = 0
    if not len(list_cucian) > 0:
        if len(list_selimut) > 0:
            for list in list_selimut:
                if list == "seprei":
                    jumlah_seprei += 1
                if list == "selimut":
                    jumlah_selimut += 1
    if not len(list_cucian) > 0:
        if len(list_selimut) > 0:
            for list in list_selimut:
                list_cucian.append(list_selimut.pop(0))
                break
    while len(list_cucian) > 0:
        print("Apakah semua pakaian telah dikeluarkan? (y/n)")
        print()
        print(f"Masih tersisa:")
        banyakCucian(list_cucian, jumlah_seprei, jumlah_selimut)
        bool_pakaian = masukan()
        if bool_pakaian:
            print()
            print("Apakah anda ingin mencuci dengan metode yang sama seperti sebelumnya?")
            bool_cuci = masukan()
            if bool_cuci:
                print("====================================================")
                prosesCuci()
                print(list_cucian)
                print(list_selimut)
                n = cekSeprei()
                print(n)
                if cekSeprei():
                    cekSelimut()
                print(list_cucian)
                print(list_selimut)
                    
            else:
                print("====================================================")
                gantiMetode(metodeCuci())
                print("====================================================")
                statusMesin()
                print("====================================================")
                prosesCuci()
        else:
            print("Keluarkan semua pakaian yang telah dicuci!")
            print()
            ulangCuci()




def main():
    # if not saklar():
    #     print("Terima kasih")
    #     sys.exit()
    # print("====================================================")
    # menu()
    # print("====================================================")
    masukCucian()
    print("====================================================")
    gantiMetode(metodeCuci())
    # print("Apakah sudah sesuai?")
    # # if masukan():
    # #     metodeCuci()
    # #     gantiMetode(metodeCuci())
    print("====================================================")
    if cekSeprei():
        cekSelimut()
    statusMesin()
    print("====================================================")
    prosesCuci()
    ulangCuci()

    print("Seluruh pakaian telah dicuci.")

    



# seprei selimut 1 maksimal jika
# baju dan barang2 lain maks 20
# try:
main()
# except BaseException as error:
#     print("Telah terjadi error: {}".format(error))

# print(selesai, list_cucian)

# berat_baju = int(input("Masukkan berat baju yang akan dicuci (kg): "))

# baju 5
# selimut 1

# [baju, baju, baju, baju, baju, selimut, baju]