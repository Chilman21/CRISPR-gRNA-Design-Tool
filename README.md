# CRISPR gRNA Design Tool

## Overview
The CRISPR gRNA Design Tool is a Streamlit-based bioinformatics web application that helps users identify potential CRISPR-Cas9 guide RNA (gRNA) target sites from DNA sequences.

The application:
- Detects possible CRISPR target regions
- Checks PAM sequences (NGG)
- Calculates GC content
- Classifies gRNA efficiency
- Displays results in tables and charts
- Allows CSV result download

## Features

- DNA sequence input
- Automatic CRISPR target detection
- PAM sequence validation
- GC content analysis
- Efficiency prediction (High / Medium / Low)
- Interactive Streamlit interface
- Download results as CSV
- Data visualization using Matplotlib

## Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib

## Project Structure

CRISPR-gRNA-Design-Tool/
│
├── app.py
├── grna.py
├── analysis.py
├── requirements.txt
└── README.md


## Requirements

Create a `requirements.txt` file with:

streamlit
pandas
matplotlib

## Run Application

```bash
streamlit run app.py
```

## Example DNA Sequence

ATGCGTACCGGATCGTAGCTAGGCTAGCTAGGCTAGCGG

## Output

The tool provides:
- gRNA target sequence
- PAM sequence
- GC content percentage
- Efficiency classification
- GC content bar graph

## Efficiency Classification

| GC Content | Efficiency |
|------------|------------|
| 40% - 60%  | High |
| 30% - 39%  | Medium |
| Below 30%  | Low |


## Future Improvements

- Off-target prediction
- Support for multiple PAM sequences
- FASTA file upload
- Machine learning-based efficiency prediction
- Export results as PDF

## Author

Developed using Python and Streamlit for bioinformatics research and educational purposes.