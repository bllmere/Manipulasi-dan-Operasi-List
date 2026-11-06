# A. Tambahkan 'truk' diakhir list

data = ["motor","mobil","sepeda","bus"]
print (f"data sebelum ditambah = \n{data}")

data.append ("truk")
print (f"data sesudah ditambah truk= \n{data}")

# B. Sisipkan 'becak' pada index ke -1

data.insert (1,"becak")
print (f"data sesudah ditambah becak = \n{data}")

# C. Hapus data yang berada paling belakang dari list tersebut

data.pop()
print (f"hapus data paling belakang = \n{data}")

# D. Ubah elemen 'sepeda' menjadi 'skuter'

data[3] = "skuter"
print (f"mengubah sepeda menjadi skuter = \n{data}")

# Tampilkan informasi jumlah total data di dlaam list tersebut

jumlah_data = len(data)
print (f"jumlah total data = {jumlah_data}")


# A. Cari tahu di index ke berapa skor 100 berada

angka = [75,80,90,75,85,100,65]
print (f"angka = {angka}")

index_100 = angka.index(100)
print (f"index si 100 = {index_100}")

# B. Hitung ada berapa banyak siswa yang mendapatkan skor 75

jumlah_skor_75 = angka.count (75)
print (f"jumlah skor 75 = {jumlah_skor_75}")

# C. Urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar

print (f"skor ujian sebelum sort = \n{angka}")
angka.sort()
print (f"skor ujian setelah sort = \n{angka}")

# D. Balikkan urutan list yang sudah diurutkan tersebut sehingga menjadi dari terbesar ke terkecil

angka.reverse()
print (f"angka di reserve = \n{angka}")


# Gabungkan menu tambahan ke dalam menu utama menggunakan fungsi, kemudian tampilkan hasil dari data gabungan tersebut

menu_utama = ["Nasi Goreng","Mie Ayam"]
print (f" menu utama = {menu_utama}")
menu_tambahan = ["Kerupuk","Es Teh"]
print (f" menu tambahan = {menu_tambahan}")

menu_utama.extend (menu_tambahan)
print (f"menu gabungan = \n{menu_utama}")


# Tampilkan harga dari "Pensil" (2000) dengan memanggil index baris dan kolom yang spesifik dar  list tersebut

data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]
harga_Pensil = data_barang[1][1]
print (f"harga Pensil = {harga_Pensil}")

# Gunakan perulangan untuk membaca data satu persatu, lalu tampilkan output dengan format "Nama:[nama barang], Harga[harga barang]" untuk setiap elemen didalamnya

for i, u in data_barang :
    print (f"nama barang\t : {i}")
    print (f"harga barang\t : {u}\n")