import pandas as pd

df_datasampah = pd.read_csv('Data_Sampah_PerHari.csv')

print(df_datasampah)

# Nomor 1
datakota_sampah = pd.DataFrame(df_datasampah,columns=['nama_kabupaten_kota','jumlah_produksi_sampah','satuan','tahun'])

print(datakota_sampah)

# Nomor 2
jumlah_sampah_pertahun = int(input("Masukan Tahun Dari 2015 - 2023 :"))

total_perthn = 0

for i,row in datakota_sampah.iterrows():
    if row['tahun'] == jumlah_sampah_pertahun:
        total_perthn += row['jumlah_produksi_sampah']

if total_perthn > 0:
    print(f"Total Produksi sampah pada tahun {jumlah_sampah_pertahun} adalah sebanyak {total_perthn:.2f} Ton")
else:
    print(f"Tahun {jumlah_sampah_pertahun} Tidak Ditemukan")

# Nomor 3
no_thn = {}

for index,row in df_datasampah.iterrows():
    tahun = row['tahun']    
    produksi_sampah_Perthn = row['jumlah_produksi_sampah']

    if tahun in no_thn:
        no_thn[tahun] += produksi_sampah_Perthn
    else:
        no_thn[tahun] = produksi_sampah_Perthn

print("Jumlah Produksi sampah Pertahunnya")
for tahun,jumlah in no_thn.items():
    print(f"Tahun {tahun}: {jumlah:.2f} Ton")

# Nomor 4

kota_Kabupaten = {}

for index,row in df_datasampah.iterrows():
    kab_kota = row['nama_kabupaten_kota']
    tahun = row['tahun']
    produksi_sampah_kota_kab = row['jumlah_produksi_sampah']

    if kab_kota not in kota_Kabupaten:
        kota_Kabupaten[kab_kota] = {}
    if tahun not in kota_Kabupaten[kab_kota]:
        kota_Kabupaten[kab_kota][tahun] = 0

    kota_Kabupaten[kab_kota][tahun] += produksi_sampah_kota_kab

for kab_kota,tahun_data in kota_Kabupaten.items():
    print(f"Produksi Sampah Di {kab_kota}: ")
    for tahun,jumlah_sampah in tahun_data.items():
        print(f"Tahun {tahun}: {jumlah_sampah:.2f} Ton")

# Mengeksport Ke CSV Dan Excel

datakota_sampah.to_csv('Datasampah.csv',index=False)
datakota_sampah.to_excel('Datasampah.xlsx',index=False)
