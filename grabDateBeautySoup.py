# load additional packages
from bs4 import BeautifulSoup
import requests

# get HTML content / BeautifulSoup object
resp = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
soup = BeautifulSoup(resp.content, "lxml")

# search for all paragraphs on the webpage
paragraphs = soup.find_all("p")

# get the text for each paragraph
text = [x.text for x in paragraphs]

# scrape any dates from each paragraph
results = []
for paragraph in text:
    try:
        results.append(search_dates(paragraph))
    except Exception:
        pass

counts = [0 if result is None else len(result) for result in results]

sum(counts)

results
