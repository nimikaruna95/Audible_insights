import pandas as pd

def load_data(file_path_1, file_path_2):
    data1 = pd.read_csv(file_path_1)
    data2 = pd.read_csv(file_path_2)
    return data1, data2

def merge_datasets(data1, data2):
    merged_data = pd.merge(data1, data2, on=['Book Name', 'Author'], how='inner')
    return merged_data

def clean_data(data):
    data.columns = data.columns.str.strip()

    print("Columns after merge:", data.columns)

    if 'Rating_x' in data.columns and 'Rating_y' in data.columns:
        data['Rating'] = (data['Rating_x'] + data['Rating_y']) / 2 
        data.drop(columns=['Rating_x', 'Rating_y'], inplace=True)
    elif 'Rating_x' in data.columns:
        data.rename(columns={'Rating_x': 'Rating'}, inplace=True)
        data.drop(columns=['Rating_y'], inplace=True)
    elif 'Rating_y' in data.columns:
        data.rename(columns={'Rating_y': 'Rating'}, inplace=True)
        data.drop(columns=['Rating_x'], inplace=True)
    else:
        print("No 'Rating' column found!")
        return data

    data = data.drop_duplicates()
    data = data.dropna(subset=['Book Name', 'Author', 'Rating'])
    data['Rating'] = data['Rating'].fillna(data['Rating'].mean())
    return data

def save_cleaned_data(data, file_name):
    data.to_csv(file_name, index=False)

if __name__ == "__main__":
    data1, data2 = load_data('data/Audible_Catlog.csv', 'data/Audible_Catlog_Advanced_Features.csv')
    merged_data = merge_datasets(data1, data2)
    cleaned_data = clean_data(merged_data)
    save_cleaned_data(cleaned_data, 'data/cleaned_books.csv')
