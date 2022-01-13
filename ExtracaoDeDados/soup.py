from bs4 import BeautifulSoup
import requests

url = ("https://raw.githubusercontent.com/joelgrus/data/master/getting-data.html")
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p')
first_paragraph_text = soup.p.text
first_paragraph.word = soup.p.text.split()

first_paragraph_id = soup.p['id']
first_paragraph_id2 = soup.p.get('id') 

all_paragraphs = soup.find.all('p')
paragraphs_with_ids = [p for p in soup('p') if p.get('id')]