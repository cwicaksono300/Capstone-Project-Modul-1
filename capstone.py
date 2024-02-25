def main_menu ():
    print("\nSelamat Datang di Gudang Lumajang Agro Lestari")
    print("Main Menu :")
    print("1. Melihat laporan gudang")
    print("2. Menambah laporan gudang")
    print("3. Update laporan gudang")
    print("4. Menghapus laporan gudang")
    print(f"5. Notice ({len(notice)})")
    print("6. Keluar menu")
    program = input("Pilih opsi menu : ")
    program = cekprogram(program)
    if program == 6:
        return print("Terima Kasih")
        exit()
    elif program==1:
        return menu_read()
    elif program==2:
        return menu_create()
    elif program==3:
        return menu_update()
    elif program == 4:
        return menu_delete()
    elif program == 5:
        return menu_pesan()
    else:
        print("Opsi yang anda masukkan tidak ada, kembali ke menu.")
        return main_menu()

def menu_pesan():
    print("\nMenu :")
    print(f"1. Pesan Belum Terselesaikan ({len(notice)})")
    print("2. Riwayat Pesan")
    print("3. Menu Utama")
    program_pesan = input("Pilih opsi menu : ")
    program_pesan = cekprogram(program_pesan)
    if program_pesan == 1:
        for i in range(len(notice)):
            print(f"{i+1}. {notice[i]}")
    elif program_pesan == 2:
        for i in range(len(log_notice)):
            print(f"{i+1}. {log_notice[i]}")
    elif program_pesan == 3:
        return main_menu()
    else:
        print("Opsi yang anda masukkan tidak ada, kembali ke menu.")
        return menu_pesan()
    return menu_pesan()

def menu_delete():
    print("\nMenu :")
    print("1. Delete Laporan Gudang")
    print("2. Recovery Laporan Gudang ")
    print("3. Menu Utama")
    program_delete = input("Pilih opsi menu : ")
    program_delete = cekprogram(program_delete)
    if program_delete == 1:
        return delete()
    elif program_delete == 2:
        return recovery()
    elif program_delete == 3:
        return main_menu()
    else:
        print("Opsi yang anda masukkan tidak ada, kembali ke menu.")
        return menu_delete()
    return menu_delete()

def menu_update():
    print("\nMenu :")
    print("1. Update Laporan Gudang")
    print("2. Selesaikan Notice")
    print("3. Menu Utama")
    program_update = input("Pilih opsi menu : ")
    program_update = cekprogram(program_update)
    if program_update == 1:
        return update()
    elif program_update == 2:
        for i in range(len(notice)):
            print(f"{i+1}. {notice[i]}")
        pesan = input("Pilih nomor pesan yang telah terselesaikan : ")
        pesan = cekprogram(pesan)
        print(notice[pesan-1])
        konfirmasi = input("Apakah pesan ini sudah terselesaikan (Y/N)? ")
        if(konfirmasi == "Y"):
            log_notice.append(notice[pesan-1])
            notice.pop(pesan-1)
            print("Pesan terselesaikan sudah dipindah ke riwayat pesan!")
        elif(konfirmasi =="N"):
            print("Pesan tidak jadi terselesaikan, kembali ke menu.")
            return menu_update()
        else:
            print("Konfirmasi yang anda masukkan salah, coba lagi!")
            return menu_update()
    elif program_update == 3:
        return main_menu()
    else:
        print("Opsi yang anda masukkan tidak ada, kembali ke menu.")
        return menu_update()
    return menu_update


def menu_create():
    print("\nMenu :")
    print("1. Laporan Barang Masuk")
    print("2. Laporan Barang Keluar")
    print("3. Buat Notice")
    print("4. Menu Utama")
    program_create = input("Pilih opsi menu : ")
    program_create = cekprogram(program_create)
    if program_create == 1:
        return create("M")
    elif program_create == 2:
        return create("K")
    elif program_create == 3:
        pesan = input("Masukkan pesan : ")
        notice.append(pesan)
        if(pesan == notice[-1]):
            print("Pesan anda telah tersimpan.")
            return menu_create()
        else:
            print("Maaf ada error, coba beberapa saat lagi!")
            return menu_create()
    elif program_create == 4:
        return main_menu()
    else:
        print("Opsi yang anda masukkan tidak ada, kembali ke menu.")
        return menu_create()
    return menu_create()

def menu_read():
    print("\nMenu :")
    print("1. Semua Laporan Gudang")
    print("2. Laporan Masuk")
    print("3. Laporan Keluar")
    print("4. Sort Laporan Gudang")
    print("5. Cari Kode Barang dalam Laporan Gudang")
    print("6. Kembali ke menu utama")
    program_read = input("Pilih opsi menu : ")
    program_read = cekprogram(program_read)
    if program_read == 1:
        read(data_gudang)
    elif program_read == 2:
        data_masuk=[]
        for i in range(len(data_gudang)):
            if(data_gudang[i]["ID"][0]=="M"):
                data_masuk.append(data_gudang[i])
        read(data_masuk)
    elif program_read == 3:
        data_keluar=[]
        for i in range(len(data_gudang)):
            if(data_gudang[i]["ID"][0]=="K"):
                data_keluar.append(data_gudang[i])
        read(data_keluar)
    elif program_read == 4:
        return menu_sort(data_gudang)
    elif program_read == 5:
        cari = input("Masukkan kode barang yang ingin dicari : ")
        cari = list(filter(lambda kode: kode['Kode Barang'] == cari, data_gudang))
        if cari == []:
            print("Tidak ada kode barang tersebut.")
        else:
            read(cari)
    elif program_read == 6:
        return main_menu()
    else:
        print("Opsi yang anda masukkan tidak ada, kembali ke menu.")
        return menu_read()
    return menu_read()

def menu_sort(data_gudang):
    print("\nUrutkan Data berdasarkan Kolom :")
    print("1. Kode Barang")
    print("2. Nama Barang")
    print("3. Tanggal Masuk")
    print("4. Jumlah Barang")
    program_sort = input("Pilih opsi yang tersedia : ")
    program_sort = cekprogram(program_sort)
    urut = []
    if program_sort == 1:
        urut = sorted(data_gudang, key=lambda d: d['Kode Barang'])
        read(urut)
    elif program_sort == 2:
        urut = sorted(data_gudang, key=lambda d: d['Nama'])
        read(urut)
    elif program_sort == 3:
        urut = sorted(data_gudang, key=lambda d: d['Tanggal Masuk'])
        read(urut)
    elif program_sort == 4:
        urut = sorted(data_gudang, key=lambda d: d['Jumlah'])
        read(urut)
    else:
        print("Opsi yang anda masukkan tidak ada, kembali ke menu.")
        return menu_sort(data_gudang)
    return menu_read()

def recovery():
    read(data_hapus)
    recov = input("Pilih ID laporan : ")
    cari = []
    cari = list(filter(lambda kode: kode['ID'] == recov, data_hapus))
    if cari == []:
        print("ID laporan belum terdaftar.")
        return menu_delete()
    else:
        index = data_hapus.index(cari[0])
        read(cari)
        konfirmasi = input(f"Apakah anda yakin ingin mengembalikan laporan {recov} (Y/N) : ")
        if(konfirmasi == "Y"):
            data_gudang.append(data_hapus[index])
            data_hapus.pop(index)
            cari = []
            cari = list(filter(lambda kode: kode['ID'] == recov, data_hapus))
            if(cari==[]):
                print("Laporan telah berhasil dikembalikan.")
                read(data_gudang)
                return menu_delete()
            else:
                print("Maaf terjadi error, coba beberapa saat lagi!")
                return menu_delete()
        elif(konfirmasi =="N"):
            print("Laporan tidak jadi dikembalikan, kembali ke menu.")
            return menu_delete()
        else:
            print("Konfirmasi yang anda masukkan salah, coba lagi!")
            return menu_delete()

def delete():
    read(data_gudang)
    delet = input("Pilih ID laporan : ")
    cari = []
    cari = list(filter(lambda kode: kode['ID'] == delet, data_gudang))
    if cari == []:
        print("ID laporan belum terdaftar.")
        return menu_delete()
    else:
        index = data_gudang.index(cari[0])
        read(cari)
        konfirmasi = input(f"Apakah anda yakin ingin menghapus laporan {delet} (Y/N) : ")
        if(konfirmasi == "Y"):
            data_hapus.append(data_gudang[index])
            data_gudang.pop(index)
            cari = []
            cari = list(filter(lambda kode: kode['ID'] == delet, data_gudang))
            if(cari==[]):
                print("Laporan telah berhasil dihapus.")
                read(data_gudang)
                return menu_delete()
            else:
                print("Maaf terjadi error, coba beberapa saat lagi!")
                return menu_delete()
        elif(konfirmasi =="N"):
            print("Laporan tidak jadi dihapus, kembali ke menu.")
            return menu_delete()
        else:
            print("Konfirmasi yang anda masukkan salah, coba lagi!")
            return menu_delete()

def update():
    read(data_gudang)
    updet = input("Pilih ID laporan : ")
    cari = []
    cari = list(filter(lambda kode: kode['ID'] == updet, data_gudang))
    if cari == []:
        print("ID laporan belum terdaftar.")
        return menu_update()
    else:
        index = data_gudang.index(cari[0])
        read(cari)
        print("Silahkan pilih kolom yang ingin diupdate :")
        for i in data_gudang[0]:
            print(f"-{i}")
        keys = input("Pilih kolom : ")
        flag = False
        for i in data_gudang[index]:
            if(keys == i):
                flag = True
                break
        if(flag == True):
            print(f"Nilai Awal : {data_gudang[index][keys]}")
            value = input("Nilai Baru : ")
            konfirmasi = input(f"Apakah anda yakin mengganti {data_gudang[index][keys]} menjadi {value} (Y/N)? ")
            if(konfirmasi == "Y"):
                data_gudang[index][keys] = value
                if(data_gudang[index][keys]==value):
                    print("Laporan telah berhasil di update.")
                    print(data_gudang[index])
                    return menu_update()
                else:
                    print("Maaf terjadi error, coba beberapa saat lagi!")
                    return menu_update()
            elif(konfirmasi =="N"):
                print("Laporan tidak jadi diupdate, kembali ke menu.")
                return menu_update()
            else:
                print("Konfirmasi yang anda masukkan salah, coba lagi!")
                return menu_update()
        elif(flag == False):
            print("Kolom yang anda masukkan salah, coba lagi!")
            return menu_update()
        else:
            print("Maaf terjadi error, coba beberapa saat lagi!")
            return menu_update()

def create(code):
        masuk = input(f"Masukkan ID Laporan : {code}")
        masuk = code+masuk
        cari = []
        cari = list(filter(lambda kode: kode['ID'] == masuk, data_gudang))
        if cari != []:
            print("ID laporan sudah terdaftar.")
            return menu_create()
        else:
            kode_barang = input("Masukkan kode barang : ")
            nama_barang = input("Masukkan nama barang : ")
            tanggal = input("Masukkan tanggal : ")
            jumlah = input("Masukkan jumlah barang : ")
            satuan = input("Masukkan satuan barang : ")
            data_masuk = [{"ID" : masuk,"Kode Barang":kode_barang,"Nama":nama_barang,"Tanggal Masuk":tanggal,"Jumlah" : jumlah,"Satuan" : satuan}]
            read(data_masuk)
            konfirmasi = input(f"Apakah anda yakin menyimpan laporan di atas (Y/N)? ")
            if(konfirmasi == "Y"):
                data_gudang.append(data_masuk[0])
                if(data_gudang[-1]== data_masuk[0]):
                    print("Laporan telah berhasil disimpan.")
                    read(data_gudang)
                    return menu_create()
                else:
                    print("Maaf terjadi error, coba beberapa saat lagi!")
                    return menu_create()
            elif(konfirmasi =="N"):
                print("Laporan tidak jadi disimpan, kembali ke menu.")
                return menu_create()
            else:
                print("Konfirmasi yang anda masukkan salah, coba lagi!")
                return menu_create()

def read(data_gudang):
    print("\nData Gudang Lumajang Agro Lestari\n")
    print("ID\t\t|Kode Barang\t\t|Nama Barang\t\t|Tanggal Masuk\t\t|Jumlah\t\t|Satuan")
    for i in range(len(data_gudang)):
        for j in data_gudang[i]:
            if(j=="Kode Barang"):
                print(data_gudang[i][j],end="\t\t\t")
            elif(j=="Nama"):
                if(len(data_gudang[i][j])<=7):
                    print(data_gudang[i][j],end="\t\t\t")
                elif(len(data_gudang[i][j])<=14):
                    print(data_gudang[i][j],end="\t\t")
                else:
                    print(data_gudang[i][j],end="\t")
            else:
                print(data_gudang[i][j],end="\t\t")
        print("")

def cekprogram(program):
    while program.isnumeric()==False:
        print("Masukkan opsi menu yang tepat!")
        program = input("Masukkan opsi menu : ")
    program=int(program)
    return program

data_gudang = [
    {"ID" : "K01","Kode Barang":"PD01","Nama":"Sirup Telang","Tanggal Masuk":"04-02-24","Jumlah" : 20,"Satuan" : "Botol"},
    {"ID" : "K02","Kode Barang":"PD02","Nama":"Sirup Lemon","Tanggal Masuk":"05-02-24","Jumlah" : 20,"Satuan" : "Botol"},
    {"ID" : "K03","Kode Barang":"PD03","Nama":"Keripik Tempe Sagu","Tanggal Masuk":"06-02-24","Jumlah" : 50,"Satuan" : "Pcs"},
    {"ID" : "M01","Kode Barang":"BM01","Nama":"Lemon","Tanggal Masuk":"31-01-24","Jumlah" : 10,"Satuan" : "KG"},
    {"ID" : "M02","Kode Barang":"BM02","Nama":"Bunga Telang","Tanggal Masuk":"31-01-24","Jumlah" : 2,"Satuan" : "KG"},
    {"ID" : "M03","Kode Barang":"BB01","Nama":"Botol Plastik","Tanggal Masuk":"08-02-24","Jumlah" : 40,"Satuan" : "Buah"}
]

data_hapus = [
    {"ID" : "K04","Kode Barang":"PD04","Nama":" Air Lemon Sereh","Tanggal Masuk":"10-02-24","Jumlah" : 40,"Satuan" : "Botol"},
    {"ID" : "M04","Kode Barang":"BB02","Nama":"Batang Serai","Tanggal Masuk":"09-02-24","Jumlah" : 5,"Satuan" : "KG"}
]

notice = ["Nanti ada Barang Masuk dari suplier","Stok produk sudah habis","Siapkan Lemon 2 KG untuk produksi"]
log_notice = ["Periksa kembali barang yang masuk dan keluar gudang.","Laporkan data masuk hari ini kepada unit produksi", "Ikuti pelatihan K3 yang diadakan oleh perusahaan."]
main_menu()