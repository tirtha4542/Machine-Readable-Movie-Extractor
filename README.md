
# 🎬 Machine-Readable Movie Extractor

A high-performance NLP application that transforms unstructured movie descriptions and reviews into validated, machine-readable **JSON** data. This tool utilizes **Large Language Models (LLMs)** to parse complex text and extract specific metadata with high precision.

---

## ✨ Features

* **Intelligent Extraction:** Uses `mistral-small-latest` to identify key movie details from raw paragraphs.
* **Structured Data Validation:** Implements **Pydantic** schemas to ensure the output is always consistent and type-safe.
* **Dual-Pane UI:** A modern **Streamlit** interface featuring side-by-side input and output sections.
* **Interactive JSON Viewer:** View, expand, and collapse extracted data points directly in the browser.
* **One-Click Export:** Download the generated results as a `.json` file for integration with other applications or databases.

## 🛠️ Tech Stack

* **Framework:** [LangChain](https://www.langchain.com/) (Orchestration & Output Parsing)
* **LLM:** [Mistral AI](https://mistral.ai/)
* **Frontend:** [Streamlit](https://streamlit.io/)
* **Validation:** [Pydantic](https://docs.pydantic.dev/)
* **Environment:** Python 3.9+

## 🚀 Installation & Setup

### 1. Clone the Project
```bash
git clone https://github.com/YOUR_USERNAME/movie-extractor-json.git
cd movie-extractor-json
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install streamlit langchain-mistralai python-dotenv pydantic langchain
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
MISTRAL_API_KEY=your_actual_api_key_here
```

### 5. Run the App
To ensure there are no CLI conflicts (especially in Anaconda environments), use the module run command:
```bash
python -m streamlit run app.py
```

## 📋 Extraction Schema
The tool is designed to capture the following specific fields:
* **Movie Title**
* **Release Year** (Integer)
* **Genre** (List)
* **Director**
* **Main Cast** (List)
* **Themes & Notable Features**
* **Short Summary** (2-3 lines)

## 🤝 Contributing
Contributions are welcome! If you have suggestions for new extraction fields or UI improvements, please open an issue or submit a pull request.

---
**Developed by [Tirtha Bepary](https://github.com/YOUR_USERNAME)**
*Computer Science & Engineering Graduate*










