from bs4 import BeautifulSoup
import requests

url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
news_html = requests.get(url).text
html_text = BeautifulSoup(news_html, 'lxml')
articles = html_text.find_all('article')
i = 1
for article in articles: #Lists top headlines, need to remove things that don't belong to headline
    print(f'{i} : {article.text}')
    i += 1



