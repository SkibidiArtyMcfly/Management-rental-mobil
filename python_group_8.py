# -*- coding: utf-8 -*-
"""Python Group 8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kiTb0eq9NhGiknd5_nxARGSgO_qtk53E
"""

import streamlit as st
import numpy as np
import pandas as pd
import random

if 'data_table' not in st.session_state:
    st.session_state['data_table'] = 10

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
df["Tipe Mobil"] = df.Tipe_Mobil.map(tipe_mobil_mapping)

status_mapping = {
    1: "Stand by",
    2: "Tersewa",
    3: "Rusak",
    4: "Sedang Mekanik"
}
df["Status"] = df.Status_Mobil.map(status_mapping)
myConfig={
    'ID_Mobil' : 'ID',
    'Nama_Mobil' : 'Nama',  
    'Lokasi' : 'Lokasi', 
    'Customer_ID' : 'Customer ID'
}
mobil_rusak = [mobil for mobil in data_mobil if mobil[3] == 3]  # Use index 3 to access 'Status_Mobil'


def gantikan_mobil_rusak():
    for rusak in mobil_rusak:

        tipe_mobil_rusak = rusak[2]
        customer_id = rusak[5]

        # Use numerical indices for 'Status_Mobil' and 'Tipe_Mobil' in the generator expression
        mobil_gantian = next((mobil for mobil in data_mobil if mobil[3] == 1 and mobil[2] == tipe_mobil_rusak), None)

        if mobil_gantian != None:
            st.write(f"Mobil yang akan diganti: {rusak[1]} (ID: {rusak[0]}), Customer ID: {customer_id}, Status: Rusak")
            st.write(f"Mobil pengganti: {mobil_gantian[1]} (ID: {mobil_gantian[0]}), Status: Standby\n")
            df.loc[df['ID_Mobil'] == mobil_gantian[0], ['Status_Mobil', 'Customer_ID', 'Status']] = [2, customer_id, 'Tersewa']
            df.loc[df['ID_Mobil'] == rusak[0],['Status_Mobil', 'Customer_ID', 'Status']] = [4, None, "Sedang Mekanik"]

        else:
            print("tidak ada mobil pengganti")
# Fungsi untuk menampilkan antarmuka Streamlit
def reset():
    st.session_state.df = data_mobil   
st.title("Aplikasi Penggantian Mobil Rusak")
col1, col2 =st.columns(2)
with col1:
    gantiMobil = st.button("Gantikan mobil rusak")
with col2: 
    test = st.button("Input Data Baru")
    # Tombol untuk menjalankan fungsi
if gantiMobil:
    gantikan_mobil_rusak()
if test:
    st.write('test')
st.dataframe(df, column_config = myConfig, column_order=['Nama_Mobil','Tipe Mobil', 'Status', 'Customer_ID'])

