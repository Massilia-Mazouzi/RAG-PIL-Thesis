# RAG-PIL-Thesis
Supplementary code, data, and results for my Master's thesis on an AI assistant for Algerian Patient Information Leaflets.
# An AI Assistant for Algerian Patient Information Leaflets using Retrieval-Augmented Generation

This repository contains the supplementary data, results, and source code for the Master's thesis by [Your Name], submitted to the [Your University Name] in June 2025.

## Project Abstract

Access to clear and understandable medication information is crucial for patient safety, yet official Patient Information Leaflets (PILs) are often dense and difficult for the public to comprehend. In the Algerian context, where French-language PILs are widely used, there is a significant gap in digital tools capable of providing patients with reliable and easy-to-understand answers to their medication-related questions. This thesis addresses this gap by designing, implementing, and evaluating an intelligent assistant built on a Retrieval-Augmented Generation (RAG) architecture to serve as a trustworthy information gateway to these documents.

The core of this work is an enhanced RAG pipeline that introduces a dynamic metadata filtering strategy based on medication names to significantly improve the relevance and precision of the retrieved context. A quantitative evaluation using the RAGAS framework demonstrates that this approach yields substantial improvements in answer correctness (+203.7%) and context recall (+50.7%) compared to a naïve RAG baseline.

## Repository Contents

This repository is organized as follows:

### `/results`

This directory contains the raw data from the RAGAS evaluation, comparing the performance of the Naïve RAG system against the Enhanced RAG system across 45 test queries.

* `naive_results.csv`: The complete, row-by-row RAGAS evaluation scores for the baseline Naïve RAG system.
* `enhanced_results.csv`: The complete, row-by-row RAGAS evaluation scores for the final Enhanced RAG system with metadata filtering.

Each CSV file contains the following columns:
* `question`: The input query.
* `answer`: The generated answer from the RAG system.
* `contexts`: The retrieved document chunks provided to the language model.
* `ground_truth`: The manually created reference answer.
* `answer_relevance`, `faithfulness`, `answer_correctness`, `context_recall`, `context_precision`, `answer_similarity`: The scores for each RAGAS metric.

### `/code`

This directory contains the Python source code used to build and evaluate the RAG system.

* `data_preprocessing.py`: Scripts for cleaning and chunking the source PIL documents.
* `rag_pipeline.py`: The core implementation of the Naïve and Enhanced RAG pipelines using LangChain.
* `evaluation.py`: The script used to run the RAGAS evaluation and generate the results CSV files.
* `app.py`: The Streamlit application for the user interface.
* `requirements.txt`: A list of all the required Python packages to run the code.

## How to Cite

If you use the code or data from this repository in your work, please cite the following thesis:

```bibtex
@mastersthesis{,
  author  = {},
  title   = {An AI Assistant for Algerian Patient Information Leaflets using Retrieval-Augmented Generation},
  school  = {},
  year    = {2025},
  month   = {June}
}
