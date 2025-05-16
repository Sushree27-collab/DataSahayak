# datasahayak/app.py
import streamlit as st
from modules import stats_analyzer, plot_generator, abstract_writer, formatter

st.set_page_config(page_title="DataSahayak", layout="wide")
st.title("📊 DataSahayak: Thesis & Data Helper")

uploaded_file = st.file_uploader("Upload your Excel data", type=["xlsx"])

if uploaded_file:
    df = stats_analyzer.load_and_clean(uploaded_file)
    st.subheader("Data Preview")
    st.dataframe(df)

    anova_res, tukey_res = stats_analyzer.run_anova_tukey(df)
    st.subheader("ANOVA Table")
    st.dataframe(anova_res)

    st.subheader("Tukey HSD Results")
    st.text(str(tukey_res))

    st.subheader("Boxplot")
    fig = plot_generator.make_boxplot(df)
    st.pyplot(fig)

    if st.button("Generate Abstract"):
        summary = stats_analyzer.summarize_stats(anova_res, tukey_res)
        abstract = abstract_writer.generate_abstract(summary)
        st.text_area("Generated Abstract", abstract, height=300)
        formatter.save_to_docx("abstract.docx", abstract)
        with open("output/abstract.docx", "rb") as file:
            st.download_button("Download Abstract (Word)", file, file_name="Abstract.docx")

    if st.button("Download ICAR Format"):
        formatter.build_formatted_doc(df, template="templates/icar_template.docx")
        with open("output/icar_output.docx", "rb") as file:
            st.download_button("Download ICAR Paper", file, file_name="ICAR_Paper.docx")
