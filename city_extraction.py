import spacy
import pandas as pd
import pycountry
import geonamescache

# Load the CSV file
file_path = r'D:\Master\Data\Topic_modeling\Cleaned_with_area\total_plain_data.csv'
df = pd.read_csv(file_path)

# Concatenate Title, Abstract, and Keywords into a single column separated by commas
df['Words'] = df[['Title', 'Abstract', 'Keywords']].apply(lambda x: ', '.join(x.dropna()), axis=1)

# Load the pretrained English NLP model
nlp = spacy.load("en_core_web_sm")

# Create sets of country and city names
countries_list = {country.name for country in pycountry.countries}
cities_list = {city['name'] for city in geonamescache.GeonamesCache().get_cities().values()}

# Function to extract city and country names from text
def extract_cities_countries(text):
    doc = nlp(text)
    cities, countries = [], []
    for ent in doc.ents:
        if ent.label_ == "GPE":
            if ent.text in cities_list:
                cities.append(ent.text)
            elif ent.text in countries_list:
                countries.append(ent.text)
    return {"Cities": cities, "Countries": countries}

# Ensure all text values are strings
df['Words'] = df['Words'].astype(str)

# Extract location information
df['Cities_Countries'] = df['Words'].apply(extract_cities_countries)
df['Cities'] = df['Cities_Countries'].apply(lambda x: ', '.join(set(x['Cities'])))
df['Countries'] = df['Cities_Countries'].apply(lambda x: ', '.join(set(x['Countries'])))

# Remove intermediate columns
df_processed = df.drop(columns=['Cities_Countries', 'Words'])

# Save the processed data
output_path = r'D:\Master\Data\Topic_modeling\Cleaned_with_area\total_city_reextra_2.0.csv'
df_processed.to_csv(output_path, index=False)

print("Location extraction and export completed.")
