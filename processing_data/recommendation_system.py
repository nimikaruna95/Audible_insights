import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv(r'C:\Users\DELL\Desktop\audible_insights\data\cleaned_books.csv')

print("First few book names:")
print(data['Book Name'].head())

if data['Description'].isnull().any():
    print("\nFound NaN values in 'Description'. Filling them with empty strings.")
    data['Description'] = data['Description'].fillna('')

def recommend_books(book_name, top_n=5):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(data['Description'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    matching_books = data[data['Book Name'].str.contains(book_name, case=False, na=False)]
    
    if matching_books.empty:
        print(f"'{book_name}' not found in the dataset.")
        return None
    else:
        idx = matching_books.index[0]
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]
    book_indices = [i[0] for i in sim_scores]
    return data.iloc[book_indices][['Book Name', 'Author', 'Rating']]

book_name_to_search = "Think and Grow Rich"
matching_books = data[data['Book Name'].str.contains(book_name_to_search, case=False, na=False)]

if matching_books.empty:
    print(f"'{book_name_to_search}' not found in the dataset.")
else:
    print(f"Found the following books matching '{book_name_to_search}':")
    print(matching_books[['Book Name', 'Author']])

recommended_books = recommend_books(book_name_to_search)

if recommended_books is not None:
    print(f"\nRecommended books based on '{book_name_to_search}':")
    print(recommended_books)


