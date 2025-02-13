# Audible Insights: Intelligent Book Recommendations

## Overview
Audible Insights is a book recommendation system that leverages Natural Language Processing (NLP) and machine learning techniques to suggest books based on user preferences. The project is built with Python and Streamlit and is deployed on AWS for scalability and accessibility.

## Features
- **Data Cleaning & Preprocessing**: Handles missing values, duplicates, and inconsistencies.
- **Exploratory Data Analysis (EDA)**: Visualizations to understand book ratings, genres, and trends.
- **NLP & Clustering**: Extracts meaningful insights from book descriptions and clusters books based on similarities.
- **Recommendation Models**:
  - Content-Based Filtering
  - Clustering-Based Recommendations
  - Hybrid Approach
- **Interactive UI**: Built with Streamlit for user-friendly book recommendations.
- **AWS Deployment**: Hosted on an AWS EC2 instance for global access.

## Tech Stack
- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn, NLTK, Streamlit
- **Cloud Services**: AWS EC2, S3
- **Version Control**: Git & GitHub

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Audible-insights.git
   cd Audible-insights
   ```
2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app locally:
   ```bash
   streamlit run processing_data/app.py
   ```

## Project Structure
```
├── data/                    # Raw dataset files
├── cleaning_data/           # Data cleaning scripts & notebooks
├── processing_data/         # Data processing & model scripts
│   ├── app.py               # Streamlit app script
├── config/                  # Configuration files
├── streamlit/               # Streamlit UI configurations
├── requirements.txt         # Required dependencies
├── README.md                # Project documentation
```

## Deployment on AWS
1. Set up an EC2 instance and SSH into it.
2. Transfer project files using SCP or Git.
3. Install dependencies on the EC2 instance.
4. Run the Streamlit app and configure it to be accessible online.

## Future Improvements
- Integrate collaborative filtering techniques.
- Enhance NLP feature extraction.
- Improve UI design and user experience.


