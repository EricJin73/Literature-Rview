import pandas as pd

# Assume you already have a DataFrame containing literature data
# Example DataFrame
df = pd.read_csv(r'Path')

# Remove non-English literature
df_clean = df[df['Language'] == 'English']

# Save the deduplicated DataFrame to a new Excel file
output_file = 'Path'
df_clean.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f'\nThe file after filtering English has been saved to {output_file}')
