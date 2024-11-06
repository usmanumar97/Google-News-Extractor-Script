# 📰 Google News Extractor Script

This repository contains a Python script that extracts news articles using Google News, excluding those related to specific topics. 🚫🌳 This is especially useful if you're interested in extracting news on specific topics while avoiding unrelated articles.


## ⚙️ Prerequisites

- 🐍 Python 3.7 or above
- 📚 Libraries: `pygooglenews`, `datetime`, `dateparser`

To install the required libraries, run:

```sh
pip install pygooglenews dateparser
```

## 📖 How the Script Works

1. **📥 Import Libraries**:

   - The script imports necessary libraries like `GoogleNews` from `pygooglenews`, `datetime`, and `dateparser`.

2. **🗓️ Setting Date Parsing Configuration**:

   - It explicitly sets date parsing order (`settings.DATE_ORDER = 'YMD'`).

3. **🔍 Initialize Google News**:

   - Creates an instance of `GoogleNews` to retrieve news articles.

4. **📅 Define Date Range**:

   - The script defines a start date (`2024-01-01`) and an end date (`2024-09-03`) to set the time window for which news should be retrieved.

5. **🔄 Loop Through Dates**:

   - It loops through each day within the date range to gather news articles.

6. **📝 Filter by Keyword**:

   - The script searches for news articles related to a specific topic and filters out articles that contain specific keywords related to irrelevant topics. Keywords include `rainforest`, `forest`, `deforestation`, `wildfire`, etc.

7. **📊 Store Filtered News Entries**:

   - The filtered news articles are stored in a list called `all_entries`.

8. **💾 Save Results to a File**:

   - Finally, the script writes the filtered entries, including title, link, and published date, to a text file located at `C:\Users\Usman\Desktop\EasyInvest\GoogleNews\filtered_news.txt`.

## 🚀 Google News Limit Bypass

- This script is also capable of bypassing certain limits set by Google News, allowing you to retrieve more articles than typically allowed through the standard Google News interface.

## ▶️ How to Run

1. **🔗 Clone this repository**:

   ```sh
   git clone https://github.com/your-username/Google-News-Extractor-Script.git
   ```

2. **📂 Navigate to the repository directory**:

   ```sh
   cd Google-News-Extractor-Script
   ```

3. **⚙️ Run the script**:

   ```sh
   python google_news_extractor.py
   ```

4. **📄 The filtered news entries will be saved in a text file** as specified in the script.

## 📝 Notes

- Adjust the date range (`start_date` and `end_date`) to your desired period.
- Update `exclude_keywords` to add or remove keywords based on your filtering requirements.
- Make sure the output path (`file_path`) is accessi
