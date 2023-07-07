import os

# Penampungan data karyawan akan memakai list, dimana setiap karyawan mempunyai index tertentu mulai dari 0
namaKaryawan = []
idKaryawan = []
jenisKelaminKaryawan = []
umurKaryawan =  []
tempatLahirKaryawan = []
tanggalLahirKaryawan = []
bulanLahirKaryawan = []
tahunLahirKaryawan = []
statusKaryawan = []
jumlahAnakKaryawan = []
jabatanKaryawan = []
tipeKaryawan = []
jamLemburKaryawan = []

# Fungsi ini mengambil data (angka, huruf, blank), lalu mengembalikan jabatan sesuai data yang dimasukkan
def penentuJabatan(jab):
    if jab == 1:
        return "Direktur"
    elif jab == 2:
        return "Manajer"
    elif jab == 3:
        return "Supervisor"
    elif jab == 4:
        return "HRD"
    elif jab == 5:
        return "Karyawan"
    else:
        return "Invalid"

# Fungsi ini mengambil data (angka, huruf, blank), lalu mengembalikan gaji sesuai data yang dimasukkan
def penentugajiJabatan(jab):
    if jab == "Direktur":
        return 20000000
    elif jab == "Manajer":
        return 15000000
    elif jab == "Supervisor":
        return 12000000
    elif jab == "HRD":
        return 10000000
    elif jab == "Karyawan":
        return 5000000
    else:
        return 0

# Fungsi ini menampilkan seluruh karyawan yang diinput, tidak ada pengecualian
def tampilSeluruhKaryawan():
    print("Menampilkan Seluruh Karyawan")
    print("""
-----------------------------------------------------------------------------------------------------------------------------------------------
| No | Nama      | ID    | Jenis Kelamin | Umur | Tempat Lahir | Tgl/Bln/Thn Lahir | Status   | Jml Anak | Jabatan    | Tipe     | Jam Lembur |
-----------------------------------------------------------------------------------------------------------------------------------------------""")
    for i in range(len(namaKaryawan)):
        kolomNo = str(i+1)
        kolomNama = str(namaKaryawan[i])
        kolomID = str(idKaryawan[i])
        kolomJenisKelamin = str(jenisKelaminKaryawan[i])
        kolomUmur = str(umurKaryawan[i])
        kolomtempatLahir = str(tempatLahirKaryawan[i])
        kolomTanggal = str(tanggalLahirKaryawan[i])
        kolomBulan = str(bulanLahirKaryawan[i])
        kolomTahun = str(tahunLahirKaryawan[i])
        kolomStatus = str(statusKaryawan[i])
        kolomjumlahAnak = str(jumlahAnakKaryawan[i])
        kolomjabatanKaryawan = str(penentuJabatan(jabatanKaryawan[i]))
        kolomtipeKaryawan = str(tipeKaryawan[i])
        kolomjamLemburKaryawan = str(jamLemburKaryawan[i])
        print('| ' + kolomNo + (2-len(kolomNo))*' '
            + ' | ' + kolomNama + (9-len(kolomNama))*' '
            + ' | ' + kolomID + (5-len(kolomID))*' '
            + ' | ' + kolomJenisKelamin + (13-len(kolomJenisKelamin))*' '
            + ' | ' + kolomUmur + (4-len(kolomUmur))*' '
            + ' | ' + kolomtempatLahir + (12-len(kolomtempatLahir))*' '
            + ' | ' + kolomTanggal + "/" + kolomBulan + "/" + kolomTahun + (15-len(kolomTanggal + kolomBulan + kolomTahun))*' '
            + ' | ' + kolomStatus + (8-len(kolomStatus))*' '
            + ' | ' + kolomjumlahAnak + (8-len(kolomjumlahAnak))*' '
            + ' | ' + kolomjabatanKaryawan + (10-len(kolomjabatanKaryawan))*' '
            + ' | ' + kolomtipeKaryawan + (8-len(kolomtipeKaryawan))*' '
            + ' | ' + kolomjamLemburKaryawan + (10-len(kolomjamLemburKaryawan))*' ' + ' | ' )
    print("""
-----------------------------------------------------------------------------------------------------------------------------------------------""")

# Fungsi ini mengambil data berupa jabatan, tahun, atau ID, lalu mengembalikan tabel sesuai dengan salah satu variabel tersebut
def printTabel(jab = 0, pilihanTahun = 0, pilihanID = 0):
    print("""
-----------------------------------------------------------------------------------------------------------------------------------------------
| No | Nama      | ID    | Jenis Kelamin | Umur | Tempat Lahir | Tgl/Bln/Thn Lahir | Status   | Jml Anak | Jabatan    | Tipe     | Jam Lembur |
-----------------------------------------------------------------------------------------------------------------------------------------------""")
    for i in range(len(namaKaryawan)):
        if int(jabatanKaryawan[i]) == jab or int(tahunLahirKaryawan[i]) == pilihanTahun or int(idKaryawan[i]) == pilihanID:
            kolomNo = str(i+1)
            kolomNama = str(namaKaryawan[i])
            kolomID = str(idKaryawan[i])
            kolomJenisKelamin = str(jenisKelaminKaryawan[i])
            kolomUmur = str(umurKaryawan[i])
            kolomtempatLahir = str(tempatLahirKaryawan[i])
            kolomTanggal = str(tanggalLahirKaryawan[i])
            kolomBulan = str(bulanLahirKaryawan[i])
            kolomTahun = str(tahunLahirKaryawan[i])
            kolomStatus = str(statusKaryawan[i])
            kolomjumlahAnak = str(jumlahAnakKaryawan[i])
            kolomjabatanKaryawan = str(penentuJabatan(jabatanKaryawan[i]))
            kolomtipeKaryawan = str(tipeKaryawan[i])
            kolomjamLemburKaryawan = str(jamLemburKaryawan[i])
            print('| ' + kolomNo + (2-len(kolomNo))*' '
                + ' | ' + kolomNama + (9-len(kolomNama))*' '
                + ' | ' + kolomID + (5-len(kolomID))*' '
                + ' | ' + kolomJenisKelamin + (13-len(kolomJenisKelamin))*' '
                + ' | ' + kolomUmur + (4-len(kolomUmur))*' '
                + ' | ' + kolomtempatLahir + (12-len(kolomtempatLahir))*' '
                + ' | ' + kolomTanggal + "/" + kolomBulan + "/" + kolomTahun + (15-len(kolomTanggal + kolomBulan + kolomTahun))*' '
                + ' | ' + kolomStatus + (8-len(kolomStatus))*' '
                + ' | ' + kolomjumlahAnak + (8-len(kolomjumlahAnak))*' '
                + ' | ' + kolomjabatanKaryawan + (10-len(kolomjabatanKaryawan))*' '
                + ' | ' + kolomtipeKaryawan + (8-len(kolomtipeKaryawan))*' '
                + ' | ' + kolomjamLemburKaryawan + (10-len(kolomjamLemburKaryawan))*' ' + ' | ' )
    print("""
-----------------------------------------------------------------------------------------------------------------------------------------------""")

# Fungsi ini menampilkan pilihan menu utama
def pilihanMenu():
    print("------------------------------")
    print("Menu: ")
    print("1. Input data karyawan")
    print("2. Menampilkan Data Karyawan")
    print("3. Edit Data Karyawan")
    print("4. Cari Data Karyawan")
    print("5. Mencetak Slip Gaji Karyawan")
    print("6. Exit")
    print("------------------------------")

# Fungsi ini mengambil data-data karyawan
def inputDataKaryawan():
    print("Menu Input Data")
    print("------------------------------")
    namaKaryawan.append(input("Masukkan Nama: "))
    idKaryawan.append(input("Masukkan ID: "))
    jenisKelaminKaryawan.append(input("Masukkan Jenis Kelamin: "))
    umurKaryawan.append(input("Masukkan Umur: "))
    tempatLahirKaryawan.append(input("Masukkan Tempat Lahir: "))
    tanggalLahirKaryawan.append(input("Masukkan Tanggal Lahir: "))
    bulanLahirKaryawan.append(input("Masukkan Bulan Lahir (01-12): "))
    tahunLahirKaryawan.append(input("Masukkan Tahun Lahir: "))
    statusKaryawan.append(input("Masukkan Status (Menikah/Belum): "))
    jumlahAnakKaryawan.append(input("Masukkan Jumlah Anak: "))
    while True:
        try:
            jabatanKaryawan.append(int(input("Masukkan Jabatan (1. Direktur, 2. Manajer, 3. Supervisor, 4. HRD, 5. Karyawan): ")))
            
        except ValueError:
            os.system('cls')
            print("Pilihan anda salah, mohon masukkan pilihan angka (1-5) yang benar")

        else:
            tipeKaryawan.append(input("Masukkan Tipe (1. Tetap/2. Kontrak): "))
            jamLemburKaryawan.append(input("Masukkan Jam Lembur: "))
            print("------------------------------")
            input("Masukkan Enter untuk kembali ke menu")
            os.system('cls')
            break

# Fungsi ini menampilkan menu tampilan data karyawan, dan mengambil data (huruf, angka, blank) lalu mengembalikan validasi atau tabel
def tampilkanDataKaryawan():
    while True:
        if not namaKaryawan:
            print("Data Karyawan belum ada, mohon input dulu")
            input("Masukkan Enter untuk kembali ke menu")
            break
        
        else:
            print("Menu Tampilan Data Karyawan:")
            print("------------------------------")
            print("1. Tampilkan Seluruh Karyawan")
            print("2. Tampilkan Direktur")
            print("3. Tampilkan Manajer")
            print("4. Tampilkan Supervisor")
            print("5. Tampilkan HRD")
            print("6. Tampilkan Karyawan")
            print("7. Menu Utama")
            print("------------------------------")
            try:
                pilihanTampilan = int(input("Masukkan pilihan Anda: "))
            
            except ValueError:
                os.system('cls')
                print("Pilihan anda salah, mohon masukkan angka (1-6)")
            
            else:
                if pilihanTampilan == 1:
                    os.system('cls')
                    tampilSeluruhKaryawan()
                    input("Masukkan Enter untuk kembali ke menu")
                    break

                elif pilihanTampilan == 2:
                    for i in range (len(namaKaryawan)):
                        if jabatanKaryawan[i] == 1:
                            os.system('cls')
                            print("Menampilkan Direktur")
                            printTabel(1)
                            input("Masukkan Enter untuk kembali ke menu")
                            break
                        else:
                            print("Data Karyawan belum ada, mohon input dulu")
                            input("Masukkan Enter untuk kembali ke menu")
                    break
                
                elif pilihanTampilan == 3:
                    for i in range (len(namaKaryawan)):
                        if jabatanKaryawan[i] == 2:
                            os.system('cls')
                            print("Menampilkan Manajer")
                            printTabel(2)
                            input("Masukkan Enter untuk kembali ke menu")
                            break
                        else:
                            print("Data Karyawan belum ada, mohon input dulu")
                            input("Masukkan Enter untuk kembali ke menu")
                    break

                
                elif pilihanTampilan == 4:
                    for i in range (len(namaKaryawan)):
                        if jabatanKaryawan[i] == 3:
                            os.system('cls')
                            print("Menampilkan Supervisor")
                            printTabel(3)
                            input("Masukkan Enter untuk kembali ke menu")
                            break
                        else:
                            print("Data Karyawan belum ada, mohon input dulu")
                            input("Masukkan Enter untuk kembali ke menu")
                    break
                    

                elif pilihanTampilan == 5:
                    for i in range (len(namaKaryawan)):
                        if jabatanKaryawan[i] == 4:
                            os.system('cls')
                            print("Menampilkan HRD")
                            printTabel(4)
                            input("Masukkan Enter untuk kembali ke menu")
                            break
                        else:
                            print("Data Karyawan belum ada, mohon input dulu")
                            input("Masukkan Enter untuk kembali ke menu")
                    break

                elif pilihanTampilan == 6:
                    for i in range (len(namaKaryawan)):
                        if jabatanKaryawan[i] == 5:
                            os.system('cls')
                            print("Menampilkan Karyawan")
                            printTabel(5)
                            input("Masukkan Enter untuk kembali ke menu")
                            break
                        else:
                            print("Data Karyawan belum ada, mohon input dulu")
                            input("Masukkan Enter untuk kembali ke menu")
                    break

                elif pilihanTampilan == 7:
                    os.system('cls')
                    break

                else:
                    os.system('cls')
                    print("Pilihan anda salah, mohon masukkan angka (1-6)")

# Fungsi ini untuk edit data karyawan
def editDataKaryawan():
    if not namaKaryawan:
        print("Data Karyawan belum ada, mohon input dulu")
    else:
        tampilSeluruhKaryawan()
        print('\n')
        
        while True:
            try: 
                nomorEdit = int(input("Masukkan nomor yang ingin diedit: ")) - 1
                
            except ValueError:
                os.system('cls')
                print("Pilihan anda salah, mohon masukkan pilihan angka yang benar")
                tampilSeluruhKaryawan()
                print('\n')

            else:
                if nomorEdit >= len(namaKaryawan):
                    os.system('cls')
                    print("Pilihan anda salah, mohon masukkan pilihan angka yang benar")
                    tampilSeluruhKaryawan()
                    print('\n')
                else:

                    os.system('cls')
                    print("Mengedit data karyawan nomor " +  str(nomorEdit + 1))
                    print("------------------------------")
                    namaKaryawan[nomorEdit] = input("Masukkan nama baru: ")
                    idKaryawan[nomorEdit] = input("Masukkan id baru: ")
                    jenisKelaminKaryawan[nomorEdit] = input("Masukkan jenis kelamin baru: ")
                    umurKaryawan[nomorEdit] = input("Masukkan umur baru: ")
                    tempatLahirKaryawan[nomorEdit] = input("Masukkan tempat lahir baru: ")
                    tanggalLahirKaryawan[nomorEdit] = input("Masukkan tanggal lahir baru: ")
                    bulanLahirKaryawan[nomorEdit] = input("Masukkan bulan lahir baru (01-12): ")
                    tahunLahirKaryawan[nomorEdit] = input("Masukkan tahun lahir baru: ")
                    statusKaryawan[nomorEdit] = input("Masukkan status baru (Menikah/Belum): ")
                    jumlahAnakKaryawan[nomorEdit] = input("Masukkan jumlah anak baru: ")
                    
                    while True:
                        try:
                            jabatanKaryawan[nomorEdit] = int(input("Masukkan jabatan baru (1. Direktur, 2. Manajer, 3. Supervisor, 4. HRD, 5. Karyawan): "))
                            
                        except ValueError:
                            os.system('cls')
                            print("Pilihan anda salah, mohon masukkan pilihan angka (1-5) yang benar")

                        else:
                            tipeKaryawan[nomorEdit] = input("Masukkan tipe baru: ")
                            jamLemburKaryawan[nomorEdit] = input("Masukkan jam lembur baru: ")
                            print("------------------------------")
                            break
                break
    
# Fungsi ini mencari data karyawan
def cariDataKaryawan():
    if not namaKaryawan:
        print("Data Karyawan belum ada, mohon input dulu")
        input("Masukkan Enter untuk kembali ke menu")
    else:
        while True:
            print("Menu Cari Data Karyawan")
            print("------------------------------")
            print("1. Berdasarkan Tahun lahir")
            print("2. Berdasarkan ID")
            print("3. Menu Utama")
            print("------------------------------")
            try:
                pilihanCari = int(input("Masukkan pilihan Anda: "))

            except ValueError:
                os.system('cls')
                print("Pilihan anda salah, mohon masukkan angka (1-2)")

            else:
                if pilihanCari == 1:
                    os.system('cls')
                    pilihanTahun = int(input("Masukkan tahun lahir karyawan yang ingin dicari: "))
                    print("Pilihan tahun Anda: " + str(pilihanTahun))
                    printTabel(0, pilihanTahun)
                    print('\n')
                    input("Masukkan Enter untuk kembali ke menu")
                    break

                elif pilihanCari == 2:
                    os.system('cls')
                    pilihanID = int(input("Masukkan ID karyawan yang ingin dicari: "))
                    print("Pilihan tahun Anda: " + str(pilihanID))
                    printTabel(0, 0, pilihanID)
                    print('\n')
                    input("Masukkan Enter untuk kembali ke menu")
                    break
                
                elif pilihanCari == 3:
                    os.system('cls')
                    break

                else:
                    print("Pilihan anda salah, mohon masukkan angka (1-3)")

# Fungsi ini mengambil nama lalu mencetak slip gaji dalam bentuk txt
def cetakSlipGaji():
    if not namaKaryawan:
        print("Data Karyawan belum ada, mohon input dulu")
    else:
        while True:
            print("Menu Cetak Slip Gaji")
            print("------------------------------")
            print("1. Cetak Berdasarkan Nama")
            print("2. Cetak Seluruh Karyawan")
            print("------------------------------")
            try:
                pilihanCetak = int(input("Masukkan Menu yang diinginkan: "))

            except ValueError:
                os.system('cls')
                print("Pilihan anda invalid, mohon masukkan angka (1-2)")
            
            else:
                if pilihanCetak == 1:
                    while True:
                        try:
                            namaCetak = input("Masukkan Nama yang ingin dicetak gajinya: ")

                        except ValueError:
                            os.system('cls')
                            print("Mohon masukkan nama yang benar")
                        
                        else:
                            for i in range(len(namaKaryawan)):
                                if namaCetak == namaKaryawan[i]:
                                    file = open(namaKaryawan[i].lower() + "_" + "slip_gaji.txt", "w")
                                    gajiJabatan = penentugajiJabatan(str(penentuJabatan(jabatanKaryawan[i])))
                                    tunjanganStatus = 1000000 if statusKaryawan[i] == "Menikah" else 0
                                    tunjanganAnak = int(jumlahAnakKaryawan[i]) * 500000
                                    gajiLembur = 100000 * int(jamLemburKaryawan[i])
                                    bonusGaji = 0
                                    if tipeKaryawan[i] == "Tetap":
                                        bonusGaji = 3000000
                                    elif tipeKaryawan[i] == "Kontrak":
                                        bonusGaji = 1000000
                                    gajiKotor = gajiJabatan + tunjanganStatus + tunjanganAnak + gajiLembur + bonusGaji
                                    potonganPajak = gajiKotor * 0.1
                                    gajiSetelahPajak = gajiKotor - potonganPajak
                                    bpjs = gajiSetelahPajak * 0.25
                                    gajiBersih = gajiSetelahPajak - bpjs
                                    file.write("PT XYZ" + '\n')
                                    file.write("----------------------------------------------------------------------------------------------------------------" + '\n')
                                    file.write("Slip Gaji Karyawan" + '\n')
                                    file.write("    (2022/2023)    " + '\n')
                                    file.write("Nama: ".ljust(20) + str(namaKaryawan[i]) + '\n')
                                    file.write("ID: ".ljust(20) + str(idKaryawan[i]) + '\n')
                                    file.write("Jabatan: ".ljust(20) + str(penentuJabatan(jabatanKaryawan[i])) + '\n')
                                    file.write("Status: ".ljust(20) + str(statusKaryawan[i]) + '\n')
                                    file.write("Jumlah anak: ".ljust(20) + str(jumlahAnakKaryawan[i]) + '\n')
                                    file.write("Tipe karyawan: ".ljust(20) + str(tipeKaryawan[i]) + '\n')
                                    file.write("----------------------------------------------------------------------------------------------------------------" + '\n')
                                    file.write("Penghasilan".ljust(50) + "Potongan" + '\n')
                                    file.write("Tunjangan Status:".ljust(20) + str(int(tunjanganStatus)).ljust(30) + "Gaji Kotor:".ljust(25) + str(int(gajiKotor)) + '\n')
                                    file.write("Tunjangan Anak:".ljust(20) + str(int(tunjanganAnak)).ljust(30) + "Gaji Setelah Pajak:".ljust(25) + str(int(gajiSetelahPajak)) + '\n')
                                    file.write("Gaji Lembur:".ljust(20) + str(int(gajiLembur)).ljust(30) + "BPJS:".ljust(25) + str(int(bpjs)) + '\n')
                                    file.write("Bonus Gaji:".ljust(20) + str(int(bonusGaji)).ljust(30) + '\n')
                                    file.write("----------------------------------------------------------------------------------------------------------------" + '\n')
                                    file.write("Gaji Bersih:".ljust(20) + str(int(gajiBersih)) + '\n')
                                    file.write("----------------------------------------------------------------------------------------------------------------")
                                    
                                    file.close()
                                    input("Slip gaji berhasil di cetak dengan nama slipgaji.txt, klik enter untuk kembali ke menu utama")
                            break

                elif pilihanCetak == 2:
                    for i in range(len(namaKaryawan)):
                        file = open(namaKaryawan[i].lower() + "_" + "slip_gaji.txt", "w")
                        gajiJabatan = penentugajiJabatan(str(penentuJabatan(jabatanKaryawan[i])))
                        tunjanganStatus = 1000000 if statusKaryawan[i] == "Menikah" else 0
                        tunjanganAnak = int(jumlahAnakKaryawan[i]) * 500000
                        gajiLembur = 100000 * int(jamLemburKaryawan[i])
                        bonusGaji = 0
                        if tipeKaryawan[i] == "Tetap":
                            bonusGaji = 3000000
                        elif tipeKaryawan[i] == "Kontrak":
                            bonusGaji = 1000000
                        gajiKotor = gajiJabatan + tunjanganStatus + tunjanganAnak + gajiLembur + bonusGaji
                        potonganPajak = gajiKotor * 0.1
                        gajiSetelahPajak = gajiKotor - potonganPajak
                        bpjs = gajiSetelahPajak * 0.25
                        gajiBersih = gajiSetelahPajak - bpjs
                        file.write("PT XYZ" + '\n')
                        file.write("----------------------------------------------------------------------------------------------------------------" + '\n')
                        file.write("Slip Gaji Karyawan" + '\n')
                        file.write("    (2022/2023)    " + '\n')
                        file.write("Nama: ".ljust(20) + str(namaKaryawan[i]) + '\n')
                        file.write("ID: ".ljust(20) + str(idKaryawan[i]) + '\n')
                        file.write("Jabatan: ".ljust(20) + str(penentuJabatan(jabatanKaryawan[i])) + '\n')
                        file.write("Status: ".ljust(20) + str(statusKaryawan[i]) + '\n')
                        file.write("Jumlah anak: ".ljust(20) + str(jumlahAnakKaryawan[i]) + '\n')
                        file.write("Tipe karyawan: ".ljust(20) + str(tipeKaryawan[i]) + '\n')
                        file.write("----------------------------------------------------------------------------------------------------------------" + '\n')
                        file.write("Penghasilan".ljust(50) + "Potongan" + '\n')
                        file.write("Tunjangan Status:".ljust(20) + str(int(tunjanganStatus)).ljust(30) + "Gaji Kotor:".ljust(25) + str(int(gajiKotor)) + '\n')
                        file.write("Tunjangan Anak:".ljust(20) + str(int(tunjanganAnak)).ljust(30) + "Gaji Setelah Pajak:".ljust(25) + str(int(gajiSetelahPajak)) + '\n')
                        file.write("Gaji Lembur:".ljust(20) + str(int(gajiLembur)).ljust(30) + "BPJS:".ljust(25) + str(int(bpjs)) + '\n')
                        file.write("Bonus Gaji:".ljust(20) + str(int(bonusGaji)).ljust(30) + '\n')
                        file.write("----------------------------------------------------------------------------------------------------------------" + '\n')
                        file.write("Gaji Bersih:".ljust(20) + str(int(gajiBersih)) + '\n')
                        file.write("----------------------------------------------------------------------------------------------------------------")
                                    
                        
                    file.close()  
                    input("Slip gaji berhasil di cetak dengan nama slipgaji.txt, klik enter untuk kembali ke menu utama")
                    break

                else:
                    print("Pilihan anda invalid, mohon masukkan angka (1-2)")
            



# Looping menu dengan validasi, akan selalu ada hingga user menginput 6 untuk exit
while True:
    pilihanMenu()
    try:
        pilihanUser = int((input("Masukkan menu yang diinginkan: ")))
        
    except ValueError:
        os.system('cls')
        print("Pilihan anda salah, mohon masukkan pilihan angka (1-6) yang benar")

    else:
        if pilihanUser == 1:
            os.system('cls')
            inputDataKaryawan()

        elif pilihanUser == 2:
            os.system('cls')
            tampilkanDataKaryawan()
            os.system('cls')

        elif pilihanUser == 3:
            os.system('cls')
            editDataKaryawan()
            print('\n')
            input("Masukkan Enter untuk kembali ke menu")
            os.system('cls')

        elif pilihanUser == 4:
            os.system('cls')
            cariDataKaryawan()
            os.system('cls')

        elif pilihanUser == 5:
            os.system('cls')
            cetakSlipGaji()
            input("Masukkan Enter untuk kembali ke menu")
            os.system('cls')

        elif pilihanUser == 6:
            print("Terima kasih telah menggunakan program kami. Program akan keluar.")
            break

        else:
            os.system('cls')
            print("Pilihan anda salah, mohon masukkan pilihan angka (1-6) yang benar")