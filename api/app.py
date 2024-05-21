from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import spacy
import re
from gensim import corpora
from gensim.models import LdaModel
import numpy as np
from typing import List

app = FastAPI()
nlp = spacy.load('en_core_web_sm')
stopwords = set(spacy.lang.en.stop_words.STOP_WORDS)

class FilePaths(BaseModel):
    file_paths: List[str]

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    tokens = nlp(text)
    tokens = [token.lemma_ for token in tokens if token.is_alpha and token.lemma_ not in stopwords]
    return tokens

def convert_numpy_types(data):
    if isinstance(data, np.float32):
        return float(data)
    elif isinstance(data, np.integer):
        return int(data)
    elif isinstance(data, np.ndarray):
        return data.tolist()
    elif isinstance(data, dict):
        return {key: convert_numpy_types(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_numpy_types(item) for item in data]
    return data

def label_topic(words):
    labels = {
        "technology": ["tech", "computer", "internet", "device", "software"],
        "machine learning": ["algorithm", "data", "model", "learning", "prediction"],
        "api": ["api", "endpoint", "request", "response", "server"],
        "pandas": ["dataframe", "pandas", "row", "column", "index"],
        "python": ["python", "code", "script", "programming", "library"]
    }

    for label, keywords in labels.items():
        if any(word in words for word in keywords):
            return label
    return "miscellaneous"

@app.post("/categorize")
async def categorize_text(file_paths: FilePaths):
    try:
        documents = []
        for file_path in file_paths.file_paths:
            with open(file_path, 'r', encoding="utf-8") as file:
                text = file.read()
                
            documents.append(preprocess(text))

        dictionary = corpora.Dictionary(documents)
        dtm = [dictionary.doc2bow(doc) for doc in documents]

        model = LdaModel(dtm, id2word=dictionary, num_topics=5)

        topics = []
        for i, topic in model.show_topics(formatted=False):
            top_words = [word for word, prob in topic[:5]]
            label = label_topic(top_words)
            topic_str = f"Topic {i + 1} ({label}): " + " ".join([f"{word} ({convert_numpy_types(prob):.2f})" for word, prob in topic[:5]])
            topics.append(topic_str)

        return {"topics": topics}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

