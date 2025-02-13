import os
import streamlit as st
import pandas as pd
from recommendation_system import recommend_books  # Ensure correct import

#Title
st.title('Audible Insights: Intelligent Book Recommendations')

# Defining relative path-dataset
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cleaned_books.csv')

# Check whether the file present or not
if not os.path.exists(data_path):
    st.error(f"Error: Dataset not found at {data_path}. Please check the file path.")
else:
    # Getting data from correct path
    data = pd.read_csv(data_path)

    # Check whether the column(Book Name) present or not
    if 'Book Name' not in data.columns:
        st.error("Error: 'Book Name' column not found in dataset.")
    else:
        # Gettinf list of book names
        book_names = data['Book Name'].dropna().tolist()

        # Selectbox to pick a book
        book_name = st.selectbox('Select a book title to get recommendations:', book_names)

        # Recommended books are shown if selected book present
        if book_name:
            recommendations = recommend_books(book_name)

            if isinstance(recommendations, pd.DataFrame) and not recommendations.empty:
                st.write(f'Recommended Books based on "{book_name}":')
                st.dataframe(recommendations)
            else:
                st.write("No recommendations found.")




