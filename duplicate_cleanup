import pandas as pd

# Assuming you already have a DataFrame containing literature data
# Example DataFrame
df_combined = pd.read_csv('Your Path')

# Remove duplicates, prioritizing literature from Web of Science
# Assuming 'Title' and 'DOI' are used as criteria for duplicate identification
df_combined.sort_values(by=['Database'], ascending=False, inplace=True)
df_deduplicated = df_combined.drop_duplicates(subset=['Title', 'DOI'], keep='first')

# Save the deduplicated DataFrame to a new Excel file
output_file = 'Output Path'
df_deduplicated.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f'\nDeduplicated file saved to {output_file}')
