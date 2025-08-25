# Web Scraping + Word Cloud Assignment
# Author: Fernando Ian Patricio
# Date: August 25, 2025
# Purpose: Scrape python.org, clean text, remove stopwords, and generate a word cloud.

import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import re

# Download webpage
url = "https://www.python.org"
response = requests.get(url)
html_content = response.text

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Remove scripts and styles
for script in soup(["script", "style"]):
    script.extract()

# Extract visible text
text = soup.get_text(separator=" ")

# Clean text
text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
text = text.lower()

# Remove stopwords
stopwords = set(STOPWORDS)
words = [word for word in text.split() if word not in stopwords]

cleaned_text = " ".join(words)

# Generate WordCloud
wordcloud = WordCloud(
    width=1000,
    height=600,
    background_color="white",
    stopwords=stopwords,
    colormap="viridis"
).generate(cleaned_text)

# Display WordCloud
plt.figure(figsize=(12, 8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud from python.org", fontsize=18)
plt.show()

# Save to file
wordcloud.to_file("python_org_wordcloud.png")
