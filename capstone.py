from datetime import date
import time
def main_menu ():
    print("\nSelamat Datang di Gudang Lumajang Agro Lestari")
    print("Main Menu :")
    print("1. Melihat laporan gudang")
    print("2. Menambah laporan gudang")
    print("3. Update laporan gudang")
    print("4. Menghapus laporan gudang")
    print(f"5. Pesan ({len(notice)})")
    print("6. Keluar menu")
    program = input("Pilih opsi menu : ")
    program = cekprogram(program)
    if program == 6:
        print("Terima Kasih")
        time.sleep(3)
        return exit()
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
    print("2. Selesaikan Pesan")
    print("3. Riwayat Pesan")
    print("4. Menu Utama")
    program_pesan = input("Pilih opsi menu : ")
    program_pesan = cekprogram(program_pesan)
    if program_pesan == 1:
        print("\nPesan Belum Terselesaikan :")
        for i in range(len(notice)):
            print(f"{i+1}. {notice[i]}")
    elif program_pesan == 2:
        print("\nPesan Belum Terselesaikan :")
        for i in range(len(notice)):
            print(f"{i+1}. {notice[i]}")
        pesan = input("Pilih nomor pesan yang telah terselesaikan : ")
        pesan = cekprogram(pesan)
        print(f"\n{pesan}. {notice[pesan-1]}")
        konfirmasi = input("Apakah pesan ini sudah terselesaikan (Y/N)? ").upper()
        konfirmasi = cekkonfirmasi(konfirmasi)
        if(konfirmasi == "Y"):
            log_notice.append(notice[pesan-1])
            notice.pop(pesan-1)
            print("Pesan terselesaikan sudah dipindah ke riwayat pesan!")
            return menu_pesan()
        elif(konfirmasi =="N"):
            print("Pesan tidak jadi terselesaikan, kembali ke menu.")
            return menu_pesan()
    elif program_pesan == 3:
        print("\nRiwayat Pesan :")
        for i in range(len(log_notice)):
            print(f"{i+1}. {log_notice[i]}")
    elif program_pesan == 4:
        return main_menu()
    else:
        print("Opsi yang anda masukkan tidak ada, kembali ke menu.")
        return menu_pesan()
    return menu_pesan()

def menu_delete():
    print("\nMenu :")
    print("1. Delete Laporan Gudang")
    print("2. Recovery Laporan Gudang")
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

def menu_update():
    print("\nMenu :")
    print("1. Update Laporan Gudang")
    print("2. Menu Utama")
    program_update = input("Pilih opsi menu : ")
    program_update = cekprogram(program_update)
    if program_update == 1:
        return update()
    elif program_update == 2:
        return main_menu()
    else:
        print("Opsi yang anda masukkan tidak ada, kembali ke menu.")
        return menu_update()

def menu_create():
    print("\nMenu :")
    print("1. Laporan Barang Masuk")
    print("2. Laporan Barang Keluar")
    print("3. Buat Pesan")
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
        read(data_masuk,"NA")
    elif program_read == 3:
        data_keluar=[]
        for i in range(len(data_gudang)):
            if(data_gudang[i]["ID"][0]=="K"):
                data_keluar.append(data_gudang[i])
        read(data_keluar,"NA")
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
    print("3. Tanggal")
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
        urut = sorted(data_gudang, key=lambda d: d['Tanggal'])
        read(urut)
    elif program_sort == 4:
        urut = sorted(data_gudang, key=lambda d: d['Jumlah'])
        read(urut)
    else:
        print("Opsi yang anda masukkan tidak ada, kembali ke menu.")
        return menu_sort(data_gudang)
    return menu_read()

def recovery():
    read(data_hapus,"Recov")
    recov = input("Pilih NO laporan : ")
    recov = cekprogram(recov)
    cari = []
    cari = list(filter(lambda kode: kode['NO'] == recov, data_hapus))
    if cari == []:
        print("NO laporan belum terdaftar.")
        return menu_delete()
    else:
        index = data_hapus.index(cari[0])
        read(cari,"Recov")
        konfirmasi = input(f"Apakah anda yakin ingin mengembalikan laporan {recov} (Y/N) : ").upper()
        konfirmasi = cekkonfirmasi(konfirmasi)
        if(konfirmasi == "Y"):
            data_hapus[index].pop("NO")
            data_hapus[index].pop("Tanggal Hapus")
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

def delete():
    read(data_gudang)
    delet = input("Pilih ID laporan : ")
    cari = []
    cari = list(filter(lambda kode: kode['ID'] == delet, data_gudang))
    if cari == []:
        print("ID laporan belum terdaftar.")
        return menu_delete()
    else:
        recov = [{}]
        index = data_gudang.index(cari[0])
        recov[0]["NO"]=data_hapus[-1]["NO"]+1
        recov[0]["Tanggal Hapus"]= date.today()
        read(cari)
        konfirmasi = input(f"Apakah anda yakin ingin menghapus laporan {delet} (Y/N) : ").upper()
        konfirmasi = cekkonfirmasi(konfirmasi)
        if(konfirmasi == "Y"):
            recov[0].update(data_gudang[index])
            data_hapus.append(recov[0])
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
            if i == "ID":
                continue
            print(f"-{i}")
        keys = input("Pilih kolom : ")
        flag = False
        for i in data_gudang[index]:
            if(keys == i):
                flag = True
                break
        if(flag == True):
            if(keys == "Kode Barang"):
                print(f"Nilai Awal : {data_gudang[index][keys]}")
                value = input("Nilai Baru : ")
                barang = []
                barang = list(filter(lambda kode: kode['Kode Barang'] == value, data_produk))
                if(barang == []):
                    print("Kode barang belum terdaftar, silahkan isi informasi berikut :")
                    nama_barang = input("Masukkan nama barang : ")
                    satuan = input("Masukkan satuan barang : ")
                elif(barang != []):
                    nama_barang = barang[0]["Nama"]
                    satuan = barang[0]["Satuan"]
                konfirmasi = input(f"Apakah anda yakin mengganti {data_gudang[index][keys]} menjadi {value} (Y/N)? ").upper()
                konfirmasi = cekkonfirmasi(konfirmasi)
                if(konfirmasi == "Y"):
                    data_gudang[index]["Kode Barang"] = value
                    data_gudang[index]["Nama"] = nama_barang
                    data_gudang[index]["Satuan"] = satuan
                    if(data_gudang[index][keys]==value):
                        print("Laporan telah berhasil di update.")
                        read([data_gudang[index]])
                        return menu_update()
                    else:
                        print("Maaf terjadi error, coba beberapa saat lagi!")
                        return menu_update()
                elif(konfirmasi =="N"):
                    print("Laporan tidak jadi diupdate, kembali ke menu.")
                    return menu_update()
            elif(keys == "Tanggal"):
                print(f"Nilai Awal : {data_gudang[index][keys]}")
                tahun = input("Tahun (yyyy) : ")
                tahun = cekprogram(tahun)
                bulan = input("Bulan (mm): ")
                bulan = cekprogram(bulan)
                hari = input("Hari (dd): ")
                hari = cekprogram(hari)
                value = date(tahun,bulan,hari)
                konfirmasi = input(f"Apakah anda yakin mengganti {data_gudang[index][keys]} menjadi {value} (Y/N)? ").upper()
                konfirmasi = cekkonfirmasi(konfirmasi)
                if(konfirmasi == "Y"):
                    data_gudang[index][keys] = value
                    if(data_gudang[index][keys]==value):
                        print("Laporan telah berhasil di update.")
                        read([data_gudang[index]])
                        return menu_update()
                    else:
                        print("Maaf terjadi error, coba beberapa saat lagi!")
                        return menu_update()
                elif(konfirmasi =="N"):
                    print("Laporan tidak jadi diupdate, kembali ke menu.")
                    return menu_update()
            elif(keys != "Tanggal" or keys != "Kode Barang"):
                print(f"Nilai Awal : {data_gudang[index][keys]}")
                value = input("Nilai Baru : ")
                konfirmasi = input(f"Apakah anda yakin mengganti {data_gudang[index][keys]} menjadi {value} (Y/N)? ").upper()
                konfirmasi = cekkonfirmasi(konfirmasi)
                if(konfirmasi == "Y"):
                    data_gudang[index][keys] = value
                    if(data_gudang[index][keys]==value):
                        print("Laporan telah berhasil di update.")
                        read([data_gudang[index]])
                        return menu_update()
                    else:
                        print("Maaf terjadi error, coba beberapa saat lagi!")
                        return menu_update()
                elif(konfirmasi =="N"):
                    print("Laporan tidak jadi diupdate, kembali ke menu.")
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
        tindih="N"
        if cari != []:
            print("ID laporan sudah terdaftar.")
            tindih = input("Apakah anda ingin menimpa laporan yang ada (Y/N)? ").upper()
            tindih = cekkonfirmasi(tindih)
            if(tindih == "N"):
                print("Laporan tidak jadi ditambah, kembali ke menu.")
                return menu_create()
            elif(tindih == "Y"):
                index = data_gudang.index(cari[0])
            else:
                print("Konfirmasi yang anda masukkan salah, coba lagi!")
                return create(code)
        kode_barang = input("Masukkan kode barang : ")
        barang = []
        barang = list(filter(lambda kode: kode['Kode Barang'] == kode_barang, data_produk))
        if(barang == []):
            print("Kode barang belum terdaftar, silahkan isi informasi berikut :")
            nama_barang = input("Masukkan nama barang : ")
            jumlah = input("Masukkan jumlah barang : ")
            satuan = input("Masukkan satuan barang : ")
        elif(barang != []):
            nama_barang = barang[0]["Nama"]
            jumlah = input("Masukkan jumlah barang : ")
            satuan = barang[0]["Satuan"]
        data_masuk = [{"ID" : masuk,"Kode Barang":kode_barang,"Nama":nama_barang,"Tanggal":date.today(),"Jumlah" : jumlah,"Satuan" : satuan}]
        read(data_masuk)
        konfirmasi = input(f"Apakah anda yakin menyimpan laporan di atas (Y/N)? ").upper()
        konfirmasi = cekkonfirmasi(konfirmasi)
        if(konfirmasi == "Y" and tindih == "Y"):
            data_gudang[index]=data_masuk[0]
            read(data_gudang)
            return menu_create()
        elif(konfirmasi == "Y"):
            data_gudang.append(data_masuk[0])
            if(data_gudang[-1]== data_masuk[0]):
                print("Laporan telah berhasil disimpan.")
                read(data_gudang)
                return menu_create()
            else:
                print("Maaf terjadi error, coba beberapa saat lagi!")
                return create(code)
        elif(konfirmasi =="N"):
            print("Laporan tidak jadi disimpan, kembali ke menu.")
            return menu_create()

def read(data_gudang,kode = "ALL"):
    if kode == "ALL":
        print("\nData Gudang Lumajang Agro Lestari\n")
        print("ID\t|Kode Barang\t|Nama Barang\t\t|Tanggal\t|Jumlah\t|Satuan\t|Kategori")
        for i in range(len(data_gudang)):
            for j in data_gudang[i]:
                if(j=="Kode Barang"):
                    print(data_gudang[i][j],end="\t\t")
                elif(j=="ID" or j=="Tanggal" or j=="Jumlah" or j=="Satuan"):
                    print(data_gudang[i][j],end="\t")
                elif(j=="Nama"):
                    if(len(data_gudang[i][j])<=7):
                        print(data_gudang[i][j],end="\t\t\t")
                    elif(len(data_gudang[i][j])<=15):
                        print(data_gudang[i][j],end="\t\t")
                    else:
                        print(data_gudang[i][j],end="\t")
            if(data_gudang[i]["ID"][0]=="K"):
                print("Keluar")
            if(data_gudang[i]["ID"][0]=="M"):
                print("Masuk")
            print("")
    elif kode == "Recov":
        print("\nData Gudang Lumajang Agro Lestari\n")
        print("NO\t|Tanggal Hapus\t|ID\t|Kode Barang\t|Nama Barang\t\t|Tanggal\t|Jumlah\t|Satuan\t|Kategori")
        for i in range(len(data_gudang)):
            for j in data_gudang[i]:
                if(j=="Kode Barang"):
                    print(data_gudang[i][j],end="\t\t")
                elif(j=="ID" or j=="Tanggal" or j=="Jumlah" or j=="Satuan" or j=="NO" or j=="Tanggal Hapus"):
                    print(data_gudang[i][j],end="\t")
                elif(j=="Nama"):
                    if(len(data_gudang[i][j])<=7):
                        print(data_gudang[i][j],end="\t\t\t")
                    elif(len(data_gudang[i][j])<=15):
                        print(data_gudang[i][j],end="\t\t")
                    else:
                        print(data_gudang[i][j],end="\t")
            if(data_gudang[i]["ID"][0]=="K"):
                print("Keluar")
            if(data_gudang[i]["ID"][0]=="M"):
                print("Masuk")
            print("")
    elif kode != "ALL":
        print("\nData Gudang Lumajang Agro Lestari\n")
        print("ID\t|Kode Barang\t|Nama Barang\t\t|Tanggal\t|Jumlah\t|Satuan")
        for i in range(len(data_gudang)):
            for j in data_gudang[i]:
                if(j=="Kode Barang"):
                    print(data_gudang[i][j],end="\t\t")
                elif(j=="ID" or j=="Tanggal" or j=="Jumlah"):
                    print(data_gudang[i][j],end="\t")
                elif(j=="Nama"):
                    if(len(data_gudang[i][j])<=7):
                        print(data_gudang[i][j],end="\t\t\t")
                    elif(len(data_gudang[i][j])<=15):
                        print(data_gudang[i][j],end="\t\t")
                    else:
                        print(data_gudang[i][j],end="\t")
                else:
                    print(data_gudang[i][j],end="\t\t")
            print("")

def cekkonfirmasi (konfirmasi):
    while konfirmasi != "Y" and konfirmasi != "N":
        print("Masukkan opsi menu yang tepat! (Y/N)")
        konfirmasi = input("Masukkan konfirmasi (Y/N) : ").upper()
    return konfirmasi


def cekprogram(program): #Bisa ditambahin validasi lain
    while program.isnumeric()==False:
        print("Masukkan opsi menu yang tepat!")
        program = input("Masukkan opsi menu : ")
    program=int(program)
    return program

data_gudang = [
    {"ID" : "K01","Kode Barang":"PD01","Nama":"Sirup Telang","Tanggal": date(2024,2,4),"Jumlah" : 20,"Satuan" : "Botol"},
    {"ID" : "K02","Kode Barang":"PD02","Nama":"Sirup Lemon","Tanggal":date(2024,2,5),"Jumlah" : 20,"Satuan" : "Botol"},
    {"ID" : "K03","Kode Barang":"PD03","Nama":"Keripik Tempe Sagu","Tanggal":date(2024,2,6),"Jumlah" : 50,"Satuan" : "Pcs"},
    {"ID" : "M01","Kode Barang":"BM01","Nama":"Lemon","Tanggal":date(2024,1,24),"Jumlah" : 10,"Satuan" : "KG"},
    {"ID" : "M02","Kode Barang":"BM02","Nama":"Bunga Telang","Tanggal":date(2024,1,31),"Jumlah" : 2,"Satuan" : "KG"},
    {"ID" : "M03","Kode Barang":"BB01","Nama":"Botol Plastik","Tanggal":date(2024,2,8),"Jumlah" : 40,"Satuan" : "Buah"}
]

data_produk = [
    {"Kode Barang":"PD01","Nama":"Sirup Telang","Kategori" : "Produk", "Satuan" : "Botol", "Harga" : 20000, "Stok" : 30 },
    {"Kode Barang":"PD02","Nama":"Sirup Lemon","Kategori" : "Produk", "Satuan" : "Botol", "Harga" : 25000, "Stok" : 30 },
    {"Kode Barang":"PD03","Nama":"Keripik Tempe Sagu","Kategori" : "Produk", "Satuan" : "Pcs", "Harga" : 10000, "Stok" : 50 },
    {"Kode Barang":"BM01","Nama":"Lemon","Kategori" : "Bahan Mentah", "Satuan" : "KG", "Harga" : 10000, "Stok" : 5 },
    {"Kode Barang":"BM02","Nama":"Bunga Telang","Kategori" : "Bahan Mentah", "Satuan" : "KG", "Harga" : 20000, "Stok" : 10 },
    {"Kode Barang":"BB01","Nama":"Botol Plastik","Kategori" : "Bahan Baku", "Satuan" : "Buah", "Harga" : 500, "Stok" : 100 }
]

data_hapus = [
    {"NO":1,"Tanggal Hapus" : date(2024,2,25),"ID" : "K04","Kode Barang":"PD04","Nama":"Air Lemon Sereh","Tanggal":"10-02-24","Jumlah" : 40,"Satuan" : "Botol"},
    {"NO":2,"Tanggal Hapus" : date(2024,2,25),"ID" : "M04","Kode Barang":"BB02","Nama":"Batang Serai","Tanggal":"09-02-24","Jumlah" : 5,"Satuan" : "KG"}
]

notice = ["Nanti ada Barang Masuk dari suplier","Stok produk sudah habis","Siapkan Lemon 2 KG untuk produksi"]
log_notice = ["Periksa kembali barang yang masuk dan keluar gudang.","Laporkan data masuk hari ini kepada unit produksi", "Ikuti pelatihan K3 yang diadakan oleh perusahaan."]
main_menu()
