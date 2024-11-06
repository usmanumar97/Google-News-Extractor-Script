from pygooglenews import GoogleNews
from datetime import datetime, timedelta
from dateparser.conf import settings

# Explicitly set settings if needed
settings.DATE_ORDER = 'YMD'  # Specify the order

gn = GoogleNews()

# Define the start and end dates
start_date = datetime(2024, 1, 1)  # Starting from August 1, 2024
end_date = datetime(2024, 9, 3)    # Up until August 28, 2024

# List to store all retrieved entries
all_entries = []

# Keywords to filter out entries related to the Amazon rainforest
exclude_keywords = ['rainforest', 'forest', 'deforestation', 'wildfire', 'jungle', 'amazonas', 'brazil', 'environment', 'climate']

# Loop through each day in the date range
current_date = start_date
while current_date < end_date:
    next_date = current_date + timedelta(days=1)

    # Search for news related to Amazon on this particular day
    news = gn.search('Amazon', from_=current_date.strftime('%Y-%m-%d'), to_=next_date.strftime('%Y-%m-%d'))

    # Filter out entries related to the Amazon rainforest
    for entry in news['entries']:
        title_lower = entry.title.lower()
        if not any(keyword in title_lower for keyword in exclude_keywords):
            all_entries.append(entry)
    
    # Move to the next day
    current_date = next_date

# Specify the file path
file_path = r"C:\Users\Usman\Desktop\EasyInvest\GoogleNews\amazon_news.txt"

# Output the number of entries and the details of each entry with numbering to the file
with open(file_path, "w", encoding="utf-8") as f:
    for i, entry in enumerate(all_entries, start=1):
        f.write(f"{i}. Title: {entry.title}\n")
        f.write(f"   Link: {entry.link}\n")
        f.write(f"   Published Date: {entry.published}\n")
        f.write("\n")

print(f"Filtered entries have been written to {file_path}")
