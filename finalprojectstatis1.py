import streamlit as st
import pandas as pd
import scipy.stats as stats

# Konfigurasi Halaman
st.set_page_config(page_title="Survey Analysis App", page_icon="📊")

# --- SIDEBAR ---
with st.sidebar:
    st.title("Settings ⚙️")
    uploaded_file = st.file_uploader("Unggah file data_survei.csv di sini", type=["csv"])

# --- HALAMAN UTAMA ---
st.markdown("<h1 style='text-align: center;'>🏠 Home</h1>", unsafe_allow_status=True)

st.write("Welcome to Survey Data Analysis App! This app allows you to analyze survey data with descriptive statistics, frequency tables, visualizations, and correlation analysis. Let's dive into the world of data insights! ✨")

st.markdown("---")

st.markdown("## 🌟 Features")
st.markdown("""
* **Descriptive Statistics**: Calculate means, medians, and more for your data.
* **Frequency Tables**: View frequency and percentage distributions.
* **Correlation Analysis**: Find relationships between your variables (X and Y).
* **Created by**: yuen keysi & Group 3
""")

st.markdown("---")

# --- LOGIKA ANALISIS ---
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.success("Data berhasil diunggah!")
    
    tab1, tab2 = st.tabs(["📊 Statistik Deskriptif", "🔗 Analisis Korelasi"])
    
    with tab1:
        st.subheader("Tabel Statistik Deskriptif")
        st.write(df.describe())
        
    with tab2:
        st.subheader("Hasil Analisis Asosiasi")
        
        # Otomatis deteksi kolom (asumsi kolom terakhir dan kedua terakhir)
        cols = df.columns.tolist()
        if len(cols) >= 2:
            x_col = st.selectbox("Pilih Variabel X", cols)
            y_col = st.selectbox("Pilih Variabel Y", cols)
            
            if st.button("Hitung Korelasi"):
                r_val, p_val = stats.pearsonr(df[x_col], df[y_col])
                
                col1, col2 = st.columns(2)
                col1.metric("Nilai Korelasi (r)", f"{r_val:.2f}")
                col2.metric("P-Value", f"{p_val:.3f}")
                
                if p_val < 0.05:
                    st.success("Kesimpulan: Ada hubungan signifikan.")
                else:
                    st.warning("Kesimpulan: Tidak ada hubungan signifikan.")
else:
    st.info("Silakan unggah file CSV di sidebar untuk memulai analisis.")
