# -*- coding: utf-8 -*-
"""Python Group 8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kiTb0eq9NhGiknd5_nxARGSgO_qtk53E
"""

import numpy as np
import pandas as pd
import random

data_mobil = [[1,  "Toyota Avanza",  1,  2,  "Jl. Thamrin No. 3, Jakarta Pusat",  101],
     [2,  "Honda CR-V",  2,  3,  "Jl. Raya Cawang No. 10, Jakarta Timur",  102],
     [3,  "Suzuki Ertiga",  1,  1,  "Jl. Raya Kebayoran Baru No. 5, Jakarta Selatan",  None],
     [4,  "Honda Civic",  3,  1,  "Jl. Raya Kebayoran Baru No. 5, Jakarta Selatan",  None],
     [5,  "Toyota Fortuner",  2,  4,  "Jl. Merdeka No. 15, Jakarta Barat",  None],
     [6,  "Mitsubishi Xpander",  1,  2,  "Jl. Sunter Agung No. 12, Jakarta Utara",  103],
     [7,  "Nissan Livina",  1,  1,  "Jl. Raya Kebayoran Baru No. 5, Jakarta Selatan",  None],
     [8,  "Toyota Innova",  1,  4,  "Jl. Raya Cawang No. 10, Jakarta Timur",  104],
     [9,  "Honda HR-V",  2,  1,  "Jl. Raya Kebayoran Baru No. 5, Jakarta Selatan",  None],
     [10,  "Honda Jazz",  3,  4,  "Jl. Merdeka No. 15, Jakarta Barat",  None]]

df = pd.DataFrame(data_mobil, columns=['ID_Mobil', 'Nama_Mobil', 'Tipe_Mobil', 'Status_Mobil', 'Lokasi', 'Customer_ID'])
print(df)

df.to_csv('data_mobil.csv', index=False)

lokasi_mapping = {
    1: "Jl. Raya Kebayoran Baru No. 5, Jakarta Selatan",
    2: [
        "Jl. Sunter Agung No. 12, Jakarta Utara",
        "Jl. Thamrin No. 3, Jakarta Pusat",
        "Jl. Raya Kebayoran Baru No. 5, Jakarta Selatan",
    ],
    3: [
        "Jl. Raya Cawang No. 10, Jakarta Timur",
    ],
    4: [
        "Jl. Merdeka No. 15, Jakarta Barat",
    ]
}

tipe_mobil_mapping = {
    1: "MPV",
    2: "SUV",
    3: "Sedan"
}

status_mapping = {
    1: "Stand by",
    2: "Tersewa",
    3: "Rusak",
    4: "Sedang Mekanik"
}

from prettytable import PrettyTable
tabelMobil = PrettyTable(["ID", "Nama Mobil", "Tipe Mobil", "Status Mobil", "Customer ID"])
for index, row in df.iterrows():
     tabelMobil.add_row([row['ID_Mobil'], row['Nama_Mobil'], tipe_mobil_mapping[row['Tipe_Mobil']], status_mapping[row['Status_Mobil']], row['Customer_ID']])
print(tabelMobil)

mobil_rusak = [mobil for mobil in data_mobil if mobil[3] == 3]  # Use index 3 to access 'Status_Mobil'


def gantikan_mobil_rusak():
 for rusak in mobil_rusak:

        tipe_mobil_rusak = rusak[2]
        customer_id = rusak[5]

        # Use numerical indices for 'Status_Mobil' and 'Tipe_Mobil' in the generator expression
        mobil_gantian = next((mobil for mobil in data_mobil if mobil[3] == 1 and mobil[2] == tipe_mobil_rusak), None)

        if mobil_gantian != None:
            print(f"Mobil yang akan diganti: {rusak[1]} (ID: {rusak[0]}), Customer ID: {customer_id}, Status: Rusak")
            print(f"Mobil pengganti: {mobil_gantian[1]} (ID: {mobil_gantian[0]}), Status: Standby\n")
            df.loc[df['ID_Mobil'] == mobil_gantian[0], ['Status_Mobil', 'Customer_ID']] = [2, customer_id]
            df.loc[df['ID_Mobil'] == rusak[0],['Status_Mobil', 'Customer_ID']] = [4, None]

        else:
            print("tidak ada mobil pengganti")

gantikan_mobil_rusak()

print(df)

def tabelData():
  tabelMobil = PrettyTable(["ID", "Nama Mobil", "Tipe Mobil", "Status Mobil", "Customer ID"])
  for index, row in df.iterrows():
     tabelMobil.add_row([row['ID_Mobil'], row['Nama_Mobil'], tipe_mobil_mapping[row['Tipe_Mobil']], status_mapping[row['Status_Mobil']], row['Customer_ID']])
  print(tabelMobil)

tabelData()

import pandas as pd

# Membaca dataset dari file CSV
data_mobil = [[1,  "Toyota Avanza",  1,  2,  "Jl. Thamrin No. 3, Jakarta Pusat",  101],
     [2,  "Honda CR-V",  2,  3,  "Jl. Raya Cawang No. 10, Jakarta Timur",  102],
     [3,  "Suzuki Ertiga",  1,  1,  "Jl. Raya Kebayoran Baru No. 5, Jakarta Selatan",  None],
     [4,  "Honda Civic",  3,  1,  "Jl. Raya Kebayoran Baru No. 5, Jakarta Selatan",  None],
     [5,  "Toyota Fortuner",  2,  4,  "Jl. Merdeka No. 15, Jakarta Barat",  None],
     [6,  "Mitsubishi Xpander",  1,  2,  "Jl. Sunter Agung No. 12, Jakarta Utara",  103],
     [7,  "Nissan Livina",  1,  1,  "Jl. Raya Kebayoran Baru No. 5, Jakarta Selatan",  None],
     [8,  "Toyota Innova",  1,  4,  "Jl. Raya Cawang No. 10, Jakarta Timur",  104],
     [9,  "Honda HR-V",  2,  1,  "Jl. Raya Kebayoran Baru No. 5, Jakarta Selatan",  None],
     [10,  "Honda Jazz",  3,  4,  "Jl. Merdeka No. 15, Jakarta Barat",  None]]


# Fungsi untuk menampilkan data mobil
def display_data():
    print("\n=== DATA MOBIL ===")
    print(data_mobil)

# Fungsi untuk menambahkan data baru
def insert_data():
    print("\n=== MENAMBAHKAN DATA MOBIL BARU ===")
    id_mobil = int(input("Masukkan ID Mobil: "))
    nama_mobil = input("Masukkan Nama Mobil: ")
    tipe_mobil = int(input("Masukkan Tipe Mobil (1=MPV, 2=SUV, 3=Sedan): "))
    status_mobil = int(input("Masukkan Status Mobil (1=Standby, 2=Tersewa, 3=Rusak, 4=Sedang Mekanik): "))
    lokasi = input("Masukkan Lokasi Mobil: ")
    customer_id = input("Masukkan Customer ID (kosongkan jika tidak ada): ")

    # Menambahkan data ke dataset
    new_data = {
        "ID_Mobil": id_mobil,
        "Nama_Mobil": nama_mobil,
        "Tipe_Mobil": tipe_mobil,
        "Status_Mobil": status_mobil,
        "Lokasi": lokasi,
        "Customer_ID": customer_id if customer_id else None
    }
    global data_mobil
    data_mobil = pd.concat([data_mobil, pd.DataFrame([new_data])], ignore_index=True)
    print("Data berhasil ditambahkan!")

# Fungsi untuk mengupdate data

def update_data():
    print("\n=== MENGUPDATE DATA MOBIL ===")
    id_mobil = int(input("Masukkan ID Mobil yang akan diupdate: "))

    # Mencari data berdasarkan ID_Mobil
    global data_mobil
    index = data_mobil[data_mobil['ID_Mobil'] == id_mobil].index

    if len(index) == 0:
        print("Data tidak ditemukan!")
        return

    # Meminta data baru
    print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")
    nama_mobil = input("Nama Mobil: ")
    tipe_mobil = input("Tipe Mobil (1=MPV, 2=SUV, 3=Sedan): ")
    status_mobil = input("Status Mobil (1=Standby, 2=Tersewa, 3=Rusak, 4=Sedang Mekanik): ")
    lokasi = input("Lokasi: ")
    customer_id = input("Customer ID: ")

    # Memperbarui data
    if nama_mobil:
        data_mobil.loc[index, 'Nama_Mobil'] = nama_mobil
    if tipe_mobil:
        data_mobil.loc[index, 'Tipe_Mobil'] = int(tipe_mobil)
    if status_mobil:
        data_mobil.loc[index, 'Status_Mobil'] = int(status_mobil)
    if lokasi:
        data_mobil.loc[index, 'Lokasi'] = lokasi
    if customer_id:
        data_mobil.loc[index, 'Customer_ID'] = customer_id if customer_id else None

    print("Data berhasil diupdate!")

# Fungsi untuk menghapus data
def delete_data():
    print("\n=== MENGHAPUS DATA MOBIL ===")
    id_mobil = int(input("Masukkan ID Mobil yang akan dihapus: "))

    # Mencari data berdasarkan ID_Mobil
    global data_mobil
    index = data_mobil[data_mobil['ID_Mobil'] == id_mobil].index

    if len(index) == 0:
        print("Data tidak ditemukan!")
        return

    # Menghapus data
    data_mobil = data_mobil.drop(index).reset_index(drop=True)
    print("Data berhasil dihapus!")

# Menu utama
def main():
    while True:
        print("\n=== MENU ===")
        print("1. Display Data")
        print("2. Insert Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Exit")

        choice = input("Masukkan pilihan Anda: ")

        if choice == '1':
            display_data()
        elif choice == '2':
            insert_data()
        elif choice == '3':
            update_data()
        elif choice == '4':
            delete_data()
        elif choice == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program jika diinginkan
# main()

!pip install streamlit
!pip install pyngrok

code = '''
import streamlit as st

st.title("Aplikasi Streamlit di Google Colab")
st.write("Ini adalah contoh aplikasi Streamlit yang berjalan di Google Colab.")

# Input sederhana
nama = st.text_input("Masukkan nama Anda:")
if nama:
    st.write(f"Hallo, {nama}!")
'''

with open("streamlit_app.py", "w") as file:
    file.write(code)

'''from pyngrok import ngrok

# Jalankan Streamlit di latar belakang
!streamlit run streamlit_app.py &

# Buat tunneling dengan ngrok
public_url = ngrok.connect(port=8501)
print(f"URL publik untuk aplikasi Streamlit Anda: {public_url}")'''