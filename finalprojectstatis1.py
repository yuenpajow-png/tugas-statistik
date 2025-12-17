import streamlit as st
import pandas as pd
from scipy import stats

st.set_page_config(page_title="Analisis Statistika", layout="wide")
st.title("📊 Aplikasi Analisis Survei Final Project")

# Fitur Upload File di Web
uploaded_file = st.file_uploader("Unggah file data_survei.csv di sini", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Data Berhasil Dimuat!")

    # Mengambil semua nama kolom dari file kamu
    all_columns = df.columns.tolist()
    
    st.info("Silakan pilih kolom mana yang termasuk Variabel X dan Y di bawah ini:")
    
    col1, col2 = st.columns(2)
    with col1:
        selected_x = st.multiselect("Pilih kolom untuk Variabel X:", all_columns)
    with col2:
        selected_y = st.multiselect("Pilih kolom untuk Variabel Y:", all_columns)

    if selected_x and selected_y:
        # Hitung Skor (Poin 20%)
        df['X_total'] = df[selected_x].mean(axis=1)
        df['Y_total'] = df[selected_y].mean(axis=1)
        
        st.subheader("1. Statistik Deskriptif")
        st.write(df[['X_total', 'Y_total']].describe().T)

        # Hitung Korelasi Pearson (Poin 20%)
        r, p = stats.pearsonr(df['X_total'], df['Y_total'])
        st.subheader("2. Hasil Analisis Asosiasi")
        st.metric("Nilai Korelasi (r)", round(r, 3))
        st.metric("P-Value (Signifikansi)", round(p, 4))
        
        if p < 0.05:
            st.success("Kesimpulan: Ada hubungan signifikan.")
        else:
            st.warning("Kesimpulan: Tidak ada hubungan signifikan.")
else:
    st.warning("Menunggu kamu mengunggah file data_survei.csv...")