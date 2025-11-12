# amazone.py
import pandas as pd

# Load file
df = pd.read_csv("amazon.csv", encoding='utf-8')

# Clean numeric columns
for col in ['discounted_price', 'actual_price', 'discount_percentage', 'rating', 'rating_count']:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace('[^0-9.]', '', regex=True)
        .replace('', '0')
        .astype(float)
    )

# Fill missing text with empty strings
df = df.fillna('')

# Save cleaned version
df.to_csv("cleaned_amazon_sales.csv", index=False, encoding='utf-8')
print("✅ Cleaned CSV saved successfully!")
