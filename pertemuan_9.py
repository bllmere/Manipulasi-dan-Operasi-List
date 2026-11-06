# Program 9.1 List

# Kumpulan data numbers
data_angka = [1,5,2,3]
print (data_angka)

# Kumpulan data string
data_sting = ["hasyima,maoll,gabriell"]
print (data_sting)

# Kumpulan data_boolean
data_boolean = [True, False, True, False]
print (data_boolean)

# Kumpulan campuran
data_campuran = [7,"gabb",8,"ndutt",9,True,10]
print (data_campuran)

## Cara alternatif membuat list
data_range = range (0,10,2) # range (start,stop,step)
print (data_range)
data_list = list (data_range)
print (data_list)

# Membuat list dengan for loop, list comprehensiaon

list_for = [i **2 for i in range (0,10)]
print (list_for)

# Membuat list dengan for dengan if
list_for_if = [i for i in range (0,10) if i != 5]
print (list_for_if)

list_for_if = [i for i in range (0,10) if i % 2 == 0]
print (list_for_if)

list_for_if = [i for i in range (0,10) if i % 2 != 0]
print (list_for_if)


# Program 9.2 Manipulasi List

## ---Operasi List---

# Index 0(-3) 1(-2) 2(-1)
data = ["hasyima","maoll","gabriell"]

# mengambil data dari list
data_pertama = data[0]
print (f"data pertama (index 0) = {data_pertama}")

data_terakhir = data[-1]
print (f"data terakhir (index 2)= {data_terakhir}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print (f"panjang data = {panjang_data}")

# menambahkan item pada list sesuai posisi
print (f"data sebelum ditambah = \n{data}")

# data.insert (posisi,item)
data.insert (1,"uta")
print (f"data sesudah ditambah = \n{data}")

# data.append (item)
data.append ("gita")
print (f"data sesudah ditambah lagi = \n{data}")

# data.extend (menambahkan list dengan list)
data_baru = ["luffy","zoro","nami"]
data.extend (data_baru)
print (f"data gabungan = \n{data}")

# merubah data
# kita ubah data 2 menjadi kaido
data[2] = "kaido"
print (f"data rubah = \n{data}")

# menghapus data
data.remove ("hasyima")
print (f"data hapus = \n{data}")

# menghapus data paling belakang
data.pop()
print (f"data akhir = \n{data}")


# Program 9.3 Operasi List

# index 0(-3) 1(-2) 2(-3)
data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
print (f"data angka = \n{data_angka}")

# count data

jumlah_data_4 = data_angka.count (4)
jumlah_data_3 = data_angka.count (3)
print (f"jumlah angka 4 = {jumlah_data_4}")
print (f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data

data = ["ical","ray","winaldy","pras"]
print (f"data = {data}")

index_ical = data.index("ical")
index_ray = data.index("ray")
print (f"index si ical = {index_ical}")
print (f"index si ray = {index_ray}")

# mengurutkan list
print (f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print (f"data angka sort = \n{data_angka}")

print (f"data = {data}")
data.sort()
print (f"data sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print (f"data di reserve = \n{data_angka}")
print (f"data di reserve = \n{data}")


# Program 9.4 Nested List

## ---Nested List---

data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]

print (f"list biasa = {data_list_biasa}")

list_2D = [data_0, data_1, 6,7]
print (f"list 2D = {list_2D}")

# contoh penggunaan

peserta_0 = ["hasyimaa", 7, "Laki-laki"]
peserta_1 = ["gabb", 18, "Laki-laki"]
peserta_2 = ["namii", 16, "Perempuan"]

list_peserta = [peserta_0,peserta_1,peserta_2]
print (f"peserta = {list_peserta}\n")

for peserta in list_peserta :
    print (f"nama\t : {peserta_0}")
    print (f"umur\t : {peserta_1}")
    print (f"gender\t : {peserta_2}\n")