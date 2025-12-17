import streamlit as st
import pandas as pd
import scipy.stats as stats

# Konfigurasi Halaman
st.set_page_config(page_title="Survey Analysis App", page_icon="📊")

# --- SIDEBAR NAVIGASI ---
with st.sidebar:
    st.title("Main Menu 📋")
    # Ini yang bikin menu navigasi bulet-bulet seperti kelompok sebelah
    selected = st.radio("Go to:", ["Home", "App", "Developer Team"])
    st.markdown("---")
    st.write("Language: EN/ID")

# --- HALAMAN 1: HOME ---
if selected == "Home":
    st.title("🏠 Home")
    st.write("Welcome to Survey Data Analysis App! This app allows you to analyze survey data with descriptive statistics, frequency tables, visualizations, and correlation analysis. Let's dive into the world of data insights! ✨")
    
    st.markdown("---")
    st.markdown("## 🌟 Features")
    st.markdown("""
    * **Descriptive Statistics**: Calculate means, medians, and more.
    * **Frequency Tables**: View frequency and percentage distributions.
    * **Correlation Analysis**: Find relationships between your variables.
    """)

# --- HALAMAN 2: APP (Tempat Upload & Hitung) ---
elif selected == "App":
    st.title("🚀 Data Analysis App")
    st.info("Upload file data_survei.csv di bawah ini untuk memulai.")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("Data loaded successfully!")
        
        tab1, tab2 = st.tabs(["📊 Statistics", "🔗 Correlation"])
        
        with tab1:
            st.subheader("Descriptive Statistics")
            st.write(df.describe())
            
        with tab2:
            st.subheader("Correlation Analysis")
            cols = df.columns.tolist()
            x_col = st.selectbox("Select Variable X", cols, key="x_var")
            y_col = st.selectbox("Select Variable Y", cols, key="y_var")
            
            if st.button("Calculate"):
                r_val, p_val = stats.pearsonr(df[x_col], df[y_col])
                c1, c2 = st.columns(2)
                c1.metric("Correlation (r)", f"{r_val:.2f}")
                c2.metric("P-Value", f"{p_val:.3f}")

# --- HALAMAN 3: DEVELOPER TEAM ---
elif selected == "Developer Team":
    st.title("👥 Developer Team")
    st.write("Aplikasi ini dikembangkan oleh:")
    st.markdown("""
    ### **Group 3**
    1. **yuen keysi** (Lead Developer)
    2. Member 2
    3. Member 3
    """)
    st.info("Final Project Statistika - President University")
