import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import warnings

warnings.filterwarnings("ignore")
nltk.download('stopwords')
nltk.download('wordnet')

modi = pd.read_csv("dataset/hashtag_narendramodi.csv")
rahul = pd.read_csv("dataset/hashtag_rahulgandhi.csv")

modi['candidate'] = 'Modi'
rahul['candidate'] = 'Rahul Gandhi'
data = pd.concat([modi, rahul], ignore_index=True)

def clean_text(text):
    text = re.sub(r"http\\S+|www\\S+", "", str(text))
    text = re.sub(r"@[A-Za-z0-9_]+", "", text)
    text = re.sub(r"#", "", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = text.lower().split()
    lm = WordNetLemmatizer()
    text = [lm.lemmatize(word) for word in text if word not in stopwords.words("english")]
    return " ".join(text)

data["clean_tweet"] = data["tweet"].apply(clean_text)

def get_polarity(text):
    return TextBlob(text).sentiment.polarity

def get_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def analyze_sentiment(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

data["polarity"] = data["clean_tweet"].apply(get_polarity)

data["subjectivity"] = data["clean_tweet"].apply(get_subjectivity)

data["sentiment"] = data["polarity"].apply(analyze_sentiment)

summary = data.groupby("candidate")["sentiment"].value_counts(normalize=True).unstack().fillna(0) * 100
print("\nSentiment Distribution (%):")
print(summary.round(2))

plt.style.use('dark_background')

summary.plot(kind='bar', figsize=(9, 5), colormap='viridis')
plt.title("Sentiment Comparison between Modi and Rahul Gandhi")
plt.ylabel("Percentage (%)")
plt.xticks(rotation=0)
plt.show()

def create_wordcloud(text, title):
    wordcloud = WordCloud(width=1000, height=600, background_color='black', stopwords=STOPWORDS, colormap='plasma').generate(" ".join(text))
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title(title, fontsize=18)
    plt.show()

create_wordcloud(data[data['candidate'] == 'Modi']['clean_tweet'], "Narendra Modi Word Cloud")

create_wordcloud(data[data['candidate'] == 'Rahul Gandhi']['clean_tweet'], "Rahul Gandhi Word Cloud")

data.to_csv("dataset/final_sentiment_results.csv", index=False)
print("\nAnalysis complete. Results saved to dataset/final_sentiment_results.csv")
