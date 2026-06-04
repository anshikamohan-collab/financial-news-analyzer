# 📈 Financial News Analyzer

An AI-powered financial news analysis tool that fetches the latest news for any stock and provides sentiment analysis and insights.

## What it does
- Fetches real-time news articles for any stock using NewsAPI
- Extracts key entities (companies, people, locations) using spaCy
- Scores basic sentiment using TextBlob
- Generates a professional analyst-style summary using Groq (LLaMA 3.3)

## Tech Stack
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **NLP:** spaCy, TextBlob
- **LLM:** Groq (LLaMA 3.3 70b)
- **Data:** NewsAPI

## How to run locally

1. **Clone the repo**
   git clone https://github.com/anshikamohan-collab/financial-news-analyzer.git
   cd financial-news-analyzer
2. **Create and activate a virtual environment**
   On Windows:
   python -m venv venv
   venv\Scripts\activate
   On Mac/Linux:
   python -m venv venv
   source venv/bin/activate
3. **Install dependencies**
   pip install -r requirements.txt
4. **Create a `.env` file** in the project folder with your API keys
   NEWS_API_KEY=your_newsapi_key
   GROQ_API_KEY=your_groq_key
   Get your free API keys here:
    - NewsAPI: https://newsapi.org
    - Groq: https://console.groq.com
5. **Run the Streamlit app**
   streamlit run app.py
6. **Or run the FastAPI backend**
   uvicorn main:app --reload

