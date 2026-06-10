# import spacy
# from textblob import TextBlob
# from groq import Groq
# import os
# from dotenv import load_dotenv

# load_dotenv()

# nlp = spacy.load("en_core_web_sm")
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# def extract_entities(text):
#     doc = nlp(text)
#     entities = [(ent.text, ent.label_) for ent in doc.ents]
#     return entities

# def get_sentiment(text):
#     blob = TextBlob(text)
#     score = blob.sentiment.polarity
#     if score > 0.1:
#         return "Positive", score
#     elif score < -0.1:
#         return "Negative", score
#     else:
#         return "Neutral", score
    
# def analyze_with_groq(stock_name, articles_text):
#     prompt = f"""
#     You are a financial analyst. Analyze the following news articles about {stock_name} and provide:
#     1. Overall market sentiment: Bullish, Bearish, or Neutral
#     2. Key themes and risks in 3 bullet points
#     3. A short analyst summary in 3-4 sentences

#     Articles:
#     {articles_text}

#     Respond in this exact format:
#     SENTIMENT: [Bullish/Bearish/Neutral]
#     KEY THEMES:
#     - [theme 1]
#     - [theme 2]
#     - [theme 3]
#     SUMMARY: [your summary]
#     """
#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response.choices[0].message.content

# def analyze_articles(stock_name, articles):

#     all_text = " ".join([
#         f"{a['title']}. {a['description']}. {a['content']}"
#         for a in articles
#     ])

#     entities = extract_entities(all_text)
#     unique_entities = list(set(entities))[:10]

#     sentiment_label, sentiment_score = get_sentiment(all_text)

#     groq_analysis = analyze_with_groq(stock_name, all_text[:3000])
    
#     return {
#         "stock": stock_name,
#         "entities": [{"text": e[0], "type": e[1]} for e in unique_entities],
#         "textblob_sentiment": {
#             "label": sentiment_label,
#             "score": round(sentiment_score, 3)
#         },
#         "groq_analysis": groq_analysis
#     }
