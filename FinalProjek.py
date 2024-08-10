#Class untuk mahasiswa
class Mahasiswa:
    def __init__(self, nama, npm_mahasiswa): #Inisialisasi objek mahasiswa dengan nama, NPM, dan nilai.
        self.nama = nama #menyimpan nama mahasiswa
        self.npm_mahasiswa = npm_mahasiswa #menyimpan npm mahasiswa
        self.nilai = {} #Ini dictonary untuk nyimpan nilai

    def tambah_nilai(self, matakuliah, nilai):
        self.nilai[matakuliah] = nilai
    
    def rata_rata_nilai(self):
        if not self.nilai:
            return 0
        return sum(self.nilai.values()) / len(self.nilai)
    
    def __str__(self):
        return f"Mahasiswa: {self.nama} NPM: {self.npm_mahasiswa}"
    
#Nampilin semua mahasiswa
def semua_mahasiswa(daftar_mahasiswa):
    if not daftar_mahasiswa:
        print("Nama mahasiswa belum terdaftar.")
    else:
        for mahasiswa in daftar_mahasiswa:
            print(mahasiswa)

#Menambah mahasiswa baru
def tambah_mahasiswa(daftar_mahasiswa, npm_mahasiswa_baru, nama, npm_mahasiswa):
    if npm_mahasiswa in npm_mahasiswa_baru:
        print(f"NPM Anda {npm_mahasiswa} sudah tersedia!")
    else:
        mahasiswa_baru = Mahasiswa(nama, npm_mahasiswa)
        daftar_mahasiswa.append(mahasiswa_baru)
        npm_mahasiswa_baru.add(npm_mahasiswa)
        print(f"Mahasiswa {nama} dengan NPM '{npm_mahasiswa}' telah ditambahkan.")

#Menambah/memperbarui nilai siswa
def tambah_nilai(daftar_mahasiswa, npm_mahasiswa, matakuliah, nilai):
    for mahasiswa in daftar_mahasiswa:
        if mahasiswa.npm_mahasiswa == npm_mahasiswa:
            mahasiswa.tambah_nilai(matakuliah, nilai)
            print(f"Nilai ditambahkan: {matakuliah} - {nilai} untuk {mahasiswa.nama}.")
            return
    print(f"NPM mahasiswa '{npm_mahasiswa}' tidak ditemukan.")

#Menampilkan nilai-nilai siswa dan rata-rata nilainya
def tampilkan_nilai_mahasiswa(daftar_mahasiswa, npm_mahasiswa):
    for mahasiswa in daftar_mahasiswa:
        if mahasiswa.npm_mahasiswa == npm_mahasiswa:
            print(f"\nNilai untuk {mahasiswa.nama}:")
            for matakuliah, nilai in mahasiswa.nilai.items():
                print(f"{matakuliah}: {nilai}")
            print(f"Rata-rata Nilai: {mahasiswa.rata_rata_nilai():.2f}")
            return
    print(f"NPM mahasiswa '{npm_mahasiswa}' tidak ditemukan.")

#Pengaturan nilai siswa
def pengaturan_nilai_mahasiswa():
    daftar_mahasiswa = []  # List untuk menyimpan objek yaitu mahasiswa
    npm_mahasiswa_baru = set()  # Set untuk memastikan Npm mahasiswa yg baru

    while True: #Ini buat main menu
        print("\nMenu Pengaturan Nilai Siswa")
        print("1. Tampilkan Mahasiswa")
        print("2. Tambah Mahasiswa")
        print("3. Tambah/Perbarui Nilai")
        print("4. Tampilkan Nilai Mahasiswa")
        print("5. Keluar")

        pilihan = input("Masukan angka yang Anda ingin cari: ")

        if pilihan == '1':
            semua_mahasiswa(daftar_mahasiswa)
        
        elif pilihan == '2':
            nama = input("Masukkan nama mahasiswa: ")
            npm_mahasiswa = input("Masukkan NPM mahasiswa: ")
            tambah_mahasiswa(daftar_mahasiswa, npm_mahasiswa_baru, nama, npm_mahasiswa)
        
        elif pilihan == '3':
            npm_mahasiswa = input("Masukkan NPM mahasiswa: ")
            matakuliah = input("Masukkan matakuliah: ")
            nilai = float(input("Masukkan nilai: "))
            tambah_nilai(daftar_mahasiswa, npm_mahasiswa, matakuliah, nilai)
        
        elif pilihan == '4':
            npm_mahasiswa = input("Masukkan NPM mahasiswa: ")
            tampilkan_nilai_mahasiswa(daftar_mahasiswa, npm_mahasiswa)
        
        elif pilihan == '5':
            print("Keluar dari Pengelola Nilai Mahasiswa. Sampai jumpa!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan masukkan angka yang sudah tertera.")

#Buat di jalananin menu nya
pengaturan_nilai_mahasiswa()
