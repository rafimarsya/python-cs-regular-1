def kalkulator():
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan in ['1', '2', '3', '4', '5', '6']:
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))

        if pilihan == '1':
            print(f"Hasil: {angka1 + angka2}")
        elif pilihan == '2':
            print(f"Hasil: {angka1 - angka2}")
        elif pilihan == '3':
            print(f"Hasil: {angka1 * angka2}")
        elif pilihan == '4':
            if angka2 != 0:
                print(f"Hasil: {angka1 / angka2}")
            else:
                print("Error: Pembagian dengan nol!")
    else:
        print("Pilihan tidak valid.")

kalkulator()
