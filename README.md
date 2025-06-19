 Overview
This repository contains the full source code, data, and evaluation results for my Master's thesis project on an AI assistant for Algerian Patient Information Leaflets (PILs) using a Retrieval-Augmented Generation (RAG) architecture. Two RAG systems were implemented and compared:

- Naive RAG: Basic chunking and semantic retrieval without filtering.

- Enhanced RAG: Metadata-aware retrieval using medication name recognition and targeted filtering.

## Repository Structure:
.
├── Enhanced_RAG_system/
│   ├── Enhanced_RAG.ipynb
│   ├── ragas_dataset_enhanced_RAG.csv
│   └── ragas_results.csv          
│
├── Naive_RAG_system/
│   ├── Naive_RAG.ipynb
│   ├── ragas_input_data_naive_rag.csv
│   └── ragas_naive_results.csv
│
├── test_cases.py
└── README.md

## Folder and File Descriptions:

1/Naive_RAG_system/
Naive_RAG.ipynb — Full implementation of the baseline RAG pipeline using MiniLM embeddings and no metadata filtering.

ragas_input_data_naive_rag.csv — Test queries with reference answers and expected documents used for RAGAS evaluation.

ragas_naive_results.csv — Raw RAGAS metric scores for the naive system.

2/Enhanced_RAG_system/
Enhanced_RAG.ipynb — Final implementation of the enhanced RAG pipeline with:

Medication name identification

Metadata filtering

French-specific embeddings (Solon-base)

ragas_dataset_enhanced_RAG.csv — The same test queries used for fair comparison.

ragas_results.csv — Final RAGAS scores for the enhanced system.


3/test_cases.py
Python script that defines test queries used in the evaluation (e.g., for debugging or batch testing).





