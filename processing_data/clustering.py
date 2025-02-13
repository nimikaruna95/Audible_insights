import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import os

data = pd.read_csv(r'C:\Users\DELL\Desktop\audible_insights\data\cleaned_books.csv')

data['Description'] = data['Description'].fillna('No description available')

tfidf = TfidfVectorizer(stop_words='english')
X = tfidf.fit_transform(data['Description'])

kmeans = KMeans(n_clusters=5, random_state=42)
data['Cluster'] = kmeans.fit_predict(X)

output_dir = r'C:\Users\DELL\Desktop\audible_insights\data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

data.to_csv(os.path.join(output_dir, 'clustered_books.csv'), index=False)


