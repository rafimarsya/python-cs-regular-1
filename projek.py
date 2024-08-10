def tampilkan_menu():
    """Menampilkan menu operasi kalkulator."""
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Lihat History")
    print("6. Keluar")

def kalkulator():
    "Fungsi utama kalkulator dengan operasi dasar dan histori."
    histori = []
    
    while True:
        tampilkan_menu()
        
        pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ")
        
        if pilihan in ['1', '2', '3', '4']:
            angka1 = int(input("Masukkan angka pertama: "))
            angka2 = int(input("Masukkan angka kedua: "))

            if pilihan == '1':
                hasil = angka1 + angka2
                operasi = f"{angka1} + {angka2} = {hasil}"
            elif pilihan == '2':
                hasil = angka1 - angka2
                operasi = f"{angka1} - {angka2} = {hasil}"
            elif pilihan == '3':
                hasil = angka1 * angka2
                operasi = f"{angka1} * {angka2} = {hasil}"
            elif pilihan == '4':
                if angka2 != 0:
                    hasil = angka1 / angka2
                    operasi = f"{angka1} / {angka2} = {hasil}"
                else:
                    hasil = "Error: Pembagian dengan nol!"
                    operasi = hasil

            print(f"Hasil: {hasil}")
            histori.append(operasi)

        elif pilihan == '5':
            if histori:
                print("History Operasi:")
                for operasi in histori:
                    print(operasi)
            else:
                print("History kosong.")

        elif pilihan == '6':
            print("Keluar dari kalkulator.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    kalkulator()
