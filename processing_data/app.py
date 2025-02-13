import os
import streamlit as st
import pandas as pd
from processing_data.recommendation_system import recommend_books  # Ensure correct import

# Set up the title for the web app
st.title('Audible Insights: Intelligent Book Recommendations')

# Define the relative path for the dataset
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cleaned_books.csv')

# Check if the file exists
if not os.path.exists(data_path):
    st.error(f"Error: Dataset not found at {data_path}. Please check the file path.")
else:
    # Read data locally
    data = pd.read_csv(r'C:\Users\DELL\Desktop\audible_insights\data\cleaned_books.csv')

    # Check if 'Book Name' column exists
    if 'Book Name' not in data.columns:
        st.error("Error: 'Book Name' column not found in dataset.")
    else:
        # Get list of book names
        book_names = data['Book Name'].dropna().tolist()

        # Use Streamlit's selectbox to let users pick a book
        book_name = st.selectbox('Select a book title to get recommendations:', book_names)

        # Show recommendations if a book is selected
        if book_name:
            recommendations = recommend_books(book_name)

            if isinstance(recommendations, list) and recommendations:
                st.write(f'Recommended Books based on "{book_name}":')
                st.dataframe(pd.DataFrame(recommendations, columns=['Recommended Books']))
            else:
                st.write("No recommendations found.")



