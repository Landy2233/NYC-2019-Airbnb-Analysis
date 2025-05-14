
import pandas as pd

def clean_data():
    # Load the data
    df = pd.read_csv('AB_NYC_2019.csv')

    # Keep relevant columns
    df = df[['id', 'name', 'host_name', 'neighbourhood_group', 'neighbourhood',
             'room_type', 'price', 'minimum_nights', 'availability_365']]

    # Clean price (should already be numeric, but check anyway)
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

    # Remove rows with missing or invalid data
    df = df[df['price'] > 0]
    df = df[df['price'] <= 1000]  # Remove high outliers
    df = df[df['minimum_nights'] <= 365]  # Valid minimum_nights

    return df

# Clean data and save it to a new CSV file for later use in Dash
if __name__ == '__main__':
    df_cleaned = clean_data()
    df_cleaned.to_csv('cleaned_airbnb_data.csv', index=False)
    print("Data cleaned and saved to 'cleaned_airbnb_data.csv'")
