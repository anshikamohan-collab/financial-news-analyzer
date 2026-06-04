import streamlit as st
from news_fetcher import fetch_news
from analyzer import analyze_articles

st.set_page_config(page_title="Financial News Analyzer", page_icon="📈")

st.title("📈 Financial News Analyzer")
st.write("Enter a stock name to get an AI-powered analysis of the latest news.")

stock_name = st.text_input("Stock Name", placeholder="e.g. Tesla, Apple, Google")

if st.button("Analyze"):
    if not stock_name:
        st.warning("Please enter a stock name.")
    else:
        with st.spinner("Fetching news and analyzing..."):
            articles = fetch_news(stock_name)
            if not articles:
                st.error("No articles found for this stock.")
            else:
                result = analyze_articles(stock_name, articles)
                st.subheader(f"Analysis for {result['stock']}")

                st.markdown("### 🏷️ Entities Found")
                for entity in result["entities"]:
                    st.write(f"**{entity['text']}** → {entity['type']}")

                st.markdown("### 💬 TextBlob Sentiment")
                st.write(f"**{result['textblob_sentiment']['label']}** (score: {result['textblob_sentiment']['score']})")

                st.markdown("### 🤖 Groq LLM Analysis")
                st.write(result["groq_analysis"])