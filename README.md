# 🇮🇳 India Election Sentiment Analysis

This project performs **sentiment analysis** on tweets related to **Narendra Modi** and **Rahul Gandhi** using **Natural Language Processing (NLP)**.  
It helps visualize public opinion by analyzing the tone (positive, negative, or neutral) of thousands of tweets.

---

## 🧠 Overview

The project uses:
- **TextBlob** for sentiment polarity and subjectivity.
- **WordCloud** for keyword visualization.
- **Matplotlib** for simple, clean comparison graphs.
- **NLTK** for text cleaning and preprocessing.

It gives a clear, data-driven comparison of how people express opinions about both political figures online.

---

## ✨ Features

 - Cleans tweet text (removes links, hashtags, and special symbols)  
 - Analyzes polarity (Positive, Negative, Neutral)  
 - Generates bar chart comparing both candidates  
 - Creates colorful word clouds for visual insight  
 - Exports results into a clean CSV file  

---

## 📸 Example Output

### Sentiment Comparison
  <img width="1784" height="1148" alt="Screenshot from 2025-11-11 20-19-37" src="https://github.com/user-attachments/assets/39016d8b-53d3-42f2-8793-a421d6445f0e" />



### Word Cloud – Narendra Modi
  <img width="1784" height="1148" alt="Screenshot from 2025-11-11 20-20-55" src="https://github.com/user-attachments/assets/30a5e602-cdca-48c5-bf43-b227cdcf36a1" />


### Word Cloud – Rahul Gandhi

  <img width="1784" height="1148" alt="image" src="https://github.com/user-attachments/assets/f749c291-7482-4771-ad89-43551a2827af" />


---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/india-election-sentiment-analysis.git
cd india-election-sentiment-analysis
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Download NLTK Data (first time only)
Run this once inside a Python shell:
```python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
```

---

## 💻 How to Run (Step-by-Step)

### 🪟 For Windows:
```bash
python sentiment_analysis.py
```

### 🐧 For Linux / Ubuntu:
```bash
python3 sentiment_analysis.py
```

### 🍎 For macOS:
```bash
python3 sentiment_analysis.py
```

After running, the following will happen:
- Console will print **sentiment distribution** (Positive, Negative, Neutral)
- A **bar graph** will open comparing both candidates
- **Word clouds** for Modi and Rahul Gandhi will appear one by one
- A file `final_sentiment_results.csv` will be saved in the `/dataset` folder

---

## 🧾 Folder Structure

```
india-election-sentiment-analysis/
│
├── dataset/
│   ├── hashtag_narendramodi.csv
│   └── hashtag_rahulgandhi.csv
│
├── sentiment_analysis.py
├── requirements.txt
├── README.md
└── images/
    ├── sentiment_comparison.png
    ├── modi_wordcloud.png
    └── rahul_wordcloud.png
```

---

## 📊 Output Example

| Candidate     | Positive | Neutral | Negative |
|----------------|-----------|----------|-----------|
| Narendra Modi  | 49.8%     | 45.1%    | 5.1%      |
| Rahul Gandhi   | 30.1%     | 50.2%    | 19.7%     |

*(Percentages are sample results and vary depending on dataset)*

---

## 📁 Result Files

After execution, you’ll find:
- `dataset/final_sentiment_results.csv` → Detailed sentiment data  
- Visual plots (graphs + word clouds) displayed on screen  

---

## 🧑‍💻 Tech Stack

| Component | Purpose |
|------------|----------|
| **Python** | Core programming language |
| **Pandas / NumPy** | Data handling & analysis |
| **Matplotlib** | Plotting comparison graphs |
| **WordCloud** | Visualizing most frequent words |
| **TextBlob** | Sentiment scoring |
| **NLTK** | Text cleaning & lemmatization |

---

## 💡 Project Purpose

This project aims to show how **data science and NLP** can reveal public perception patterns during elections.  

---

## 🏁 Conclusion

The analysis reveals how public sentiment differs for both leaders based on the tweets dataset.  
You can easily expand this project using **real-time Twitter API data** for deeper, live insights.
---
