import streamlit as st
import pandas as pd
from grna import find_grna_targets
from analysis import calculate_gc_content
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="CRISPR gRNA Design Tool",
    layout="wide"
)

# Title
st.title("In Silico CRISPR gRNA Design Tool")
st.write("Analyze DNA sequences and identify CRISPR target sites.")

# DNA Input
sequence = st.text_area(
    "Enter DNA Sequence",
    height=200
)

# Run Analysis
if st.button("Analyze Sequence"):

    if sequence:

        # Clean sequence
        sequence = sequence.upper().replace("\n", "").replace(" ", "")

        # Find gRNA targets
        results = find_grna_targets(sequence)

        if results:

            result_df = pd.DataFrame(results)

            st.subheader("Detected CRISPR Target Sites")
            st.dataframe(result_df)

            # GC Content Plot
            st.subheader("GC Content Analysis")

            fig, ax = plt.subplots(figsize=(10, 5))

            ax.bar(
                result_df["Target"],
                result_df["GC_Content"]
            )

            ax.set_xlabel("gRNA Target")
            ax.set_ylabel("GC %")
            ax.set_title("GC Content of gRNAs")

            plt.xticks(rotation=45)

            st.pyplot(fig)

            # Download Results
            csv = result_df.to_csv(index=False).encode('utf-8')

            st.download_button(
                label="Download Results CSV",
                data=csv,
                file_name="grna_results.csv",
                mime="text/csv"
            )

        else:
            st.warning("No CRISPR target sites found.")

    else:
        st.error("Please enter a DNA sequence.")