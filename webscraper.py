from bs4 import BeautifulSoup
import requests

url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
news_html = requests.get(url).text
html_text = BeautifulSoup(news_html, 'lxml')
headlines = html_text.find_all('h4')
links = html_text.find_all('a')

#for i in range(10):
    #print(headlines[i+1].text)
    #print(links[i+1].get('href'))
    
for link in links:
    st = link.get('href')
    if st is not None:
        if(st[0] == '.'):
            if 'articles' in st:
                print('https://news.google.com' + st[1:])

