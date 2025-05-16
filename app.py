import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io

st.set_page_config(page_title="DataSahayak - Thesis Data Helper", layout="wide")
st.title("📊 DataSahayak: Thesis Data Helper")
st.markdown("Upload your CSV file to get quick data insights and visualizations. Ideal for thesis analysis!")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Data Preview")
    st.dataframe(df.head())

    st.subheader("📈 Summary Statistics")
    st.write(df.describe(include='all'))

    st.subheader("🧼 Missing Values")
    st.write(df.isnull().sum())

    st.subheader("📊 Histogram")
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    col = st.selectbox("Select column for histogram", numeric_cols)
    fig, ax = plt.subplots()
    sns.histplot(df[col], kde=True, ax=ax)
    st.pyplot(fig)

    st.subheader("📉 Correlation Heatmap")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax2)
    st.pyplot(fig2)

    st.markdown("---")
    st.markdown("### 🔓 Want a downloadable PDF report of your analysis?")
    st.markdown("[Unlock Now for ₹499](https://rzp.io/l/datasahayak)")
else:
    st.info("Please upload a CSV file to begin.")
