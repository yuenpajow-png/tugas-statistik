import streamlit as st
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi Halaman
st.set_page_config(page_title="Survey Analysis App - Group 3", page_icon="📊")

# --- SIDEBAR NAVIGASI ---
with st.sidebar:
    st.title("Main Menu 📋")
    selected = st.radio("Go to:", ["Home", "App (Analysis)", "Developer Team"])
    st.markdown("---")
    st.write("Project: Statistika Final Project")

# --- HALAMAN 1: HOME ---
if selected == "Home":
    st.title("🏠 Home")
    st.write("Selamat datang di Survey Data Analysis App! Aplikasi ini dirancang untuk memudahkan analisis data survei secara otomatis, mulai dari statistik deskriptif hingga analisis korelasi antar variabel. ✨")
    
    st.markdown("---")
    st.markdown("## 🌟 Features")
    st.markdown("""
    * **Descriptive Statistics**: Menghitung rata-rata, median, dan standar deviasi secara otomatis.
    * **Visualisasi Data**: Menampilkan Scatter Plot untuk melihat sebaran data.
    * **Correlation Analysis**: Menghitung nilai korelasi (r) dan P-Value untuk menguji hipotesis.
    """)

# --- HALAMAN 2: APP (Analisis Data) ---
elif selected == "App (Analysis)":
    st.title("🚀 Data Analysis App")
    st.info("Silakan unggah file 'data_survei.csv' untuk memulai analisis.")
    
    uploaded_file = st.file_uploader("Unggah file CSV", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("Data berhasil dimuat!")
        
        tab1, tab2 = st.tabs(["📊 Statistics", "🔗 Correlation & Chart"])
        
        with tab1:
            st.subheader("Descriptive Statistics")
            st.write(df.describe())
            
        with tab2:
            st.subheader("Correlation Analysis & Visualization")
            cols = df.columns.tolist()
            x_col = st.selectbox("Pilih Variabel X (Influencer)", cols, key="x_var")
            y_col = st.selectbox("Pilih Variabel Y (Keputusan Pembelian)", cols, key="y_var")
            
            if st.button("Jalankan Analisis"):
                # Hitung Korelasi
                r_val, p_val = stats.pearsonr(df[x_col], df[y_col])
                
                # Tampilkan Metrik
                c1, c2 = st.columns(2)
                c1.metric("Correlation (r)", f"{r_val:.2f}")
                c2.metric("P-Value", f"{p_val:.3f}")
                
                # Grafik Scatter Plot
                st.write("### Scatter Plot")
                fig, ax = plt.subplots()
                sns.regplot(x=df[x_col], y=df[y_col], ax=ax, scatter_kws={'color':'blue'}, line_kws={'color':'red'})
                plt.xlabel(x_col)
                plt.ylabel(y_col)
                st.pyplot(fig)
                
                # Interpretasi
                if p_val < 0.05:
                    st.success(f"Kesimpulan: Ada hubungan signifikan antara {x_col} dan {y_col}.")
                else:
                    st.warning("Kesimpulan: Tidak ada hubungan signifikan.")

# --- HALAMAN 3: DEVELOPER TEAM ---
elif selected == "Developer Team":
    st.title("👥 Developer Team")
    st.write("Aplikasi ini dikembangkan oleh Group 3 dengan peran sebagai berikut:")
    
    # Sesuai dengan tabel yang kamu kirim
    st.markdown("""
    ### **Group 3 Members:**
    1. **Yuen Keysi Pajow** *Role: Lead Developer, Designed the app concept and overall workflow.*
    2. **Keirra Venesha Rondonuwu** *Role: Project Manager, Histogram Module, and UI/UX Design.*
    3. **Meilina** *Role: Implemented geometric transforms, Filters, and Language Section.*
    4. **Roslyn Putri Silambi** *Role: Designed the interface and documentation.*
    """)
    st.markdown("---")
    st.info("Final Project Statistika - President University")
