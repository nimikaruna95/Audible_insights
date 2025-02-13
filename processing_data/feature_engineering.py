import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

def extract_text_features(data):
    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_features=100)
    tfidf_matrix = tfidf_vectorizer.fit_transform(data['Description'].fillna(''))
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
    data = pd.concat([data, tfidf_df], axis=1)
    return data

def encode_genre(data):
    if 'Ranks and Genre' in data.columns:
        data['Genre'] = data['Ranks and Genre'].apply(lambda x: x.split(',')[0] if isinstance(x, str) else '')
        genre_encoder = LabelEncoder()
        data['Genre_encoded'] = genre_encoder.fit_transform(data['Genre'])
    
    return data

def create_additional_features(data):
    data['Popularity_Score'] = data['Rating'] * data['Number of Reviews_x'].fillna(0)
    data['Price_to_Rating'] = data['Price_x'] / data['Rating']
    data['Price_to_Rating'] = data['Price_to_Rating'].replace([np.inf, -np.inf], np.nan)  # Handle infinities
    return data

def feature_engineering(data):
    data = extract_text_features(data)
    data = encode_genre(data)
    data = create_additional_features(data)
    return data

if __name__ == "__main__":
    cleaned_data = pd.read_csv('data/cleaned_books.csv')
    engineered_data = feature_engineering(cleaned_data)
    engineered_data.to_csv('data/engineered_books.csv', index=False)
    print("Feature engineering completed and saved to 'data/engineered_books.csv'.")

