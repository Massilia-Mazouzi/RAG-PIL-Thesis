 Overview
This repository contains the full source code, data, and evaluation results for my Master's thesis project on an AI assistant for Algerian Patient Information Leaflets (PILs) using a Retrieval-Augmented Generation (RAG) architecture. Two RAG systems were implemented and compared:

- Naive RAG: Basic chunking and semantic retrieval without filtering.

- Enhanced RAG: Metadata-aware retrieval using medication name recognition and targeted filtering.

  ## Repository Structure :

 Enhanced_RAG_system/
 ┣  Enhanced_RAG.ipynb           → Full code notebook for the enhanced RAG system
 ┣  ragas_dataset_enhanced_RAG.csv  → Dataset used in RAGAS evaluation
 ┗  ragas_results.csv             → RAGAS metric results for the enhanced system


 Naive_RAG_system/
 ┣  Naive_RAG.ipynb               → Full code notebook for the naive RAG system
 ┣  ragas_input_data_naive_rag.csv → Input dataset for RAGAS evaluation
 ┗  ragas_naive_results.csv       → RAGAS metric results for the naive system

 data_scraping.ipynb                 → Web scraping notebook used to collect medication leaflets (PDFs) from PharmNet-DZ

 data_preprocessing.ipynb           → Preprocessing pipeline notebook: file classification, OCR, Docling conversion


 test_cases.py                    → Python script with test queries and expected answers
 README.md                        → Project summary, instructions, and structure


## Folder and File Descriptions:
1/ Data Scraping:
This notebook contains the complete scraping pipeline used to collect Algerian medication data from PharmNet-DZ. It automatically loops through all letters A–Z, extracts medicine names, corresponding detail pages, and available leaflets links. The resulting dataset is saved as a CSV file, and all available notice PDFs are downloaded and stored in a local folder. This data serves as the foundation for further preprocessing and implementation of the two RAG systems.

2/ Data Preprocessing:
This notebook handles the full preprocessing pipeline applied to the collected medication leaflets. It begins by classifying PDFs into two categories: those with selectable text and those requiring OCR. All scanned documents are processed using OCRmyPDF or a custom fallback based on Tesseract. Then, all cleaned PDFs are converted into structured Markdown (.md) files using Docling, preserving layout and sectioning. The final result is a unified dataset of clean, readable medication leaflets ready for embedding and retrieval.

3/ Naive_RAG_system/ folder:
Naive_RAG.ipynb — Full implementation of the baseline RAG pipeline using recursive chunking, all-MiniLM-L6-v2 embeddings, and no metadata filtering.

ragas_input_data_naive_rag.csv — Test queries with the system's answers and the retrieved chunks, alongside the reference answers used as ground truth by the RAGAS framework.

ragas_naive_results.csv — Raw RAGAS metric scores for the naïve system, showing its performance on 50 test queries across six metrics: Context Relevance, Context Recall, Faithfulness, Answer Relevance, Answer Correctness, and Semantic Similarity.

4️/ Enhanced_RAG_system/ folder :
Enhanced_RAG.ipynb — Final implementation of the enhanced RAG pipeline with:
Medication name identification
Metadata-based filtering
French-specific embeddings (OrdalieTech/Solon-embeddings-base-0.1)

ragas_dataset_enhanced_RAG.csv — Same test queries and ground truth as the baseline version, used for a fair comparison.

ragas_results.csv — Final RAGAS scores for the enhanced system. For each query, scores are provided for all six metrics: Context Relevance, Context Recall, Faithfulness, Answer Relevance, Answer Correctness, and Semantic Similarity.

5️/test_cases.py:
A Python script containing the 50 test queries used in the evaluation. Can also be used for debugging or batch testing.

