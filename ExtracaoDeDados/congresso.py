from bs4 import BeautifulSoup
import requests
import re

url = "https://www.house.gov/representatives"
text = requests.get(url).text
soup = BeautifulSoup(text, "html5lib")

regex = r"^https?://.*\.house\.gov/?$"
all_urls = [a['href']
            for a in soup('a')
            if a.has_attr('href')]

print(len(all_urls))

assert re.match(regex, "http://joel.house.gov")
assert re.match(regex, "https://joel.house.gov")
assert re.match(regex, "http://joel.house.gov/")
assert re.match(regex, "https://joel.house.gov/")
assert not re.match(regex, "joel.house.gov")
assert not re.match(regex, "http://joel.house.com")
assert not re.match(regex, "https://joel.house.com")

good_urls = [url for url in all_urls if re.match(regex, url)]
print(len(good_urls))

good_urls = list(set(good_urls))
print(len(good_urls))

html = requests.get('https://jayapal.house.gov').text
soup = BeautifulSoup(html, 'html5lib')

links = {a['href'] for a in soup('a') if 'press releases' in a.text.lower()}
print(links)