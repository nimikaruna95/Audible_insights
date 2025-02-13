import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import os

# Defining relative path
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cleaned_books.csv')

# Load data
data = pd.read_csv(data_path)

# Fill missing data on column-descriptions
data['Description'] = data['Description'].fillna('No description available')

# Appling TF-IDF vectorization
tfidf = TfidfVectorizer(stop_words='english')
X = tfidf.fit_transform(data['Description'])

# Applying K-Means clustering
kmeans = KMeans(n_clusters=5, random_state=42)
data['Cluster'] = kmeans.fit_predict(X)

# Stoting the clustered data
output_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(output_dir, exist_ok=True)
data.to_csv(os.path.join(output_dir, 'clustered_books.csv'), index=False)



