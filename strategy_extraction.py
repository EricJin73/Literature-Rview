import pandas as pd
import winsound

# Load the main CSV file
file_path = 'Path'
df = pd.read_csv(file_path)

# Load mitigation and adaptation keywords from a CSV file
keywords_file_path = r'strategy_keywords_2.0.csv'
keywords_df = pd.read_csv(keywords_file_path)

mitigation_keywords = keywords_df['Mitigation'].dropna().tolist()
adaptation_keywords = keywords_df['Adaptation'].dropna().tolist()

# Function to determine the strategy type based on the presence of keywords in abstract, title, and author keywords
def determine_strategy(abstract, title, author_keywords):
    text = ''
    if not pd.isna(abstract):
        text += abstract.lower()
    if not pd.isna(title):
        text += ' ' + title.lower()
    if not pd.isna(author_keywords):
        text += ' ' + author_keywords.lower()
    
    has_mitigation = any(keyword in text for keyword in mitigation_keywords)
    has_adaptation = any(keyword in text for keyword in adaptation_keywords)
    
    if has_mitigation and has_adaptation:
        return 'both'
    elif has_mitigation:
        return 'mitigation'
    elif has_adaptation:
        return 'adaptation'
    else:
        return ''

# Apply the function to Abstract, Title, and Keywords columns
df['Strategy'] = df.apply(lambda row: determine_strategy(row['Abstract'], row['Title'], row['Keywords']), axis=1)

# Save the updated DataFrame to a new CSV file
output_file_path = 'Path'
df.to_csv(output_file_path, index=False)

print("Strategy extraction and export completed.")
# Play a beep sound when the script finishes
winsound.Beep(440, 800)  # 440 Hz, 800 ms
