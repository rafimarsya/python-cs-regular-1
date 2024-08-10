nama_pemesan = []
kode_kereta = []
nama_kereta = []
kode_kelas = []
nama_kelas = []
harga = []

print ('Selamat datang di Stasiun Tawang rute Semarang-Jakarta!')
print ('Kereta yang tersedia Argo Muria(AM) dan Tawang Jaya(TJ)')
print ('Kelas Ekonomi (E)| Bisnis (B)| Eksekutif (X)')
print ('Tarif AM E:Rp250.000, B:Rp350.000, X:Rp450.000')
print ('Tarif TJ E:Rp210.000, B:Rp300.000, X:Rp420.000')
print ('Promo Kemerdekaan 10% setiap pembelian tiket diatas Rp500.000!\n')

jumlah_pesanan = int(input('Masukkan jumlah pesanan tiket: '))
for i in range (jumlah_pesanan):
    print ('Pesanan ke- ', i+1)
    nama_pemesan.append (input('Masukkan nama pemesan: '))
    kode_kereta.append (input('Masukkan kode kereta |AM|TJ|: '))
    kode_kelas.append (input('Masukkan kode kelas |X|B|E|: '))
    if kode_kereta [i] == "AM" or kode_kereta [i] == "am":
        nama_kereta.append ('Argo Muria')
        if kode_kelas [i] == "E" or kode_kelas [i] == "e":
            nama_kelas.append ('Ekonomi')
            harga.append (int(250000))
        elif kode_kelas [i] == "B" or kode_kelas [i] == "b":
            nama_kelas.append ('Bisnis')
            harga.append (int(350000))
        elif kode_kelas [i] ==  "X" or kode_kelas [i] == "x":
            nama_kelas.append ('Eksekutif')
            harga.append (int(450000))
        else:
            nama_kelas.append('Kosong')
            harga.append (int(0))
    elif kode_kereta [i] == "TJ" or kode_kereta [i] == "tj":
        nama_kereta.append ('Tawang Jaya')
        if kode_kelas [i] == "E" or kode_kelas [i] == "e":
            nama_kelas.append ('Ekonomi')
            harga.append (int(210000))
        elif kode_kelas [i] == "B" or kode_kelas [i] == "b":
            nama_kelas.append ('Bisnis')
            harga.append (int(300000))
        elif kode_kelas [i] ==  "X" or kode_kelas [i] == "x":
            nama_kelas.append ('Eksekutif')
            harga.append (int(420000))
        else:
            nama_kelas.append('Kosong')
            harga.append (int(0))
    else:
        nama_kereta.append ('Tidak Ada')
        if kode_kelas [i] == "E" or kode_kelas [i] == "e":
            nama_kelas.append ('Ekonomi')
            harga.append (int(0))
        elif kode_kelas [i] == "B" or kode_kelas [i] == "b":
            nama_kelas.append ('Bisnis')
            harga.append (int(0))
        elif kode_kelas [i] ==  "X" or kode_kelas [i] == "x":
            nama_kelas.append ('Eksekutif')
            harga.append (int(0))
        else:
            nama_kelas.append('Kosong')
            harga.append (int(0))

total = sum(harga)
if total > 500000:
    diskon = 10/100*total
else:
    diskon = 0
bayar = total - diskon


from pprint import pprint
data = {
    'Nama' : nama_pemesan,
    'Kereta' : nama_kereta,
    'Kelas' : nama_kelas,
    'Harga' : harga
}


print('='*100)
print('PEMESANAN TIKET KERETA')
print('='*100)
pprint(data)
print('='*100)
print('Total Pesanan = ', total)
print('Diskon = ', diskon)
print('Total Bayar = ', bayar)
uang_bayar = int(input('Masukkan Uang : '))
kembalian = uang_bayar - bayar
print('Kembalian : ', kembalian)
print('Terima Kasih atas Pesanan Anda')
print('Semoga selamat sampai tujuan')
print('='*100)
