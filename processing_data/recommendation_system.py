import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# Load dataset
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cleaned_books.csv')
data = pd.read_csv(data_path)

# To check whether Description has no NaN/Null values
data['Description'] = data['Description'].fillna('')

# Function to get the recommended books based on book name
def recommend_books(book_name, top_n=5):
    # Apply TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(data['Description'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Finding the index of the book
    matching_books = data[data['Book Name'].str.contains(book_name, case=False, na=False)]
    
    if matching_books.empty:
        return pd.DataFrame(columns=['Book Name', 'Author', 'Rating'])

    idx = matching_books.index[0]
    
    # TO Get the similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]

    # To get the recommended book indices
    book_indices = [i[0] for i in sim_scores]
    return data.iloc[book_indices][['Book Name', 'Author', 'Rating']]


