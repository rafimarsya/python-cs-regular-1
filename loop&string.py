#menggunakan looping&string


products ={
    "sayur": ['kol', 'buncis', 'pakcoy','sawi'], 
    "buah": ['Apel', 'Nanas', 'Pir', 'Anggur'],
    'susu': ['UHT', 'OatSide', 'Frisianflag', 'Cimory'],
    'softdrink': ['Sprite', 'Coca-cola', 'Fanta', 'Pepsi']
}

#welcome message
print("Selamat Datang")
print("Produk yang tersedia ada: ")

for product in products:
    print(product)

while True:

    produkDicari = input("Produk apa yang sedang dicari?, \n(ketik 'keluar' untuk berhenti): ")
    if produkDicari == 'keluar':
        print("Terimakasih telah menggunakan layanan kami")
        break
    elif produkDicari in products:
        print(f"Produk yang tersedia untuk {produkDicari}: {', ' .join(products[produkDicari])}")
    
    else: 
        print("Produk tidak tersedia, silahkan cari produk yang lain")

        