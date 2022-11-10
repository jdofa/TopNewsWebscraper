from bs4 import BeautifulSoup
import requests


url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
news_html = requests.get(url).text
html_text = BeautifulSoup(news_html, 'lxml')
articles = html_text.find_all('article')

print("- TOP 10 HEADLINES ON GOOGLE NEWS - ")
i = 1
amount = 10
for article in articles: 
    if(i <= amount):
        headline = article.h4
        if headline is not None:
            print(f'{i} : {headline.text}')
            i += 1
    else:
        break
