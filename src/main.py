from fastapi import FastAPI
from pydantic import BaseModel
from src.fetchers.news_fetcher import fetch_news
from src.analysis.analyzer import analyze_articles

app = FastAPI()

class StockRequest(BaseModel):
    stock_name: str

@app.get("/")
def root():
    return {"message": "Financial News Analyzer API is running"}

@app.post("/analyze")
def analyze(request: StockRequest):
    stock_name = request.stock_name
    articles = fetch_news(stock_name)
    if not articles:
        return {"error": "No articles found for this stock"}
    result = analyze_articles(stock_name, articles)
    return result

