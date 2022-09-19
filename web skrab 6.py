import requests
import bs4 
import fake_useragent as f

KEYWORDS = ['Figma', 'Adobe', 'Apple', 'Plastic']

ua = f.UserAgent()
HEADERS = {'accept':'*/*', 'user-agent': ua.firefox}
url = "https://habr.com/ru/all/"
responce = requests.get(url,headers=HEADERS)
text = responce.text
soup = bs4.BeautifulSoup(text,features = "html.parser")

articles = soup.find_all("article")

for article in articles:
    art_s = article.find_all(class_="article-formatted-body")
#действия над списком art_s
    art_s = [art.text.strip() for art in art_s]
    title = article.find("h2").find("span").text
    href = 'https://habr.com'+article.find(class_="tm-article-snippet__title-link").attrs["href"]
    time_ = article.find(class_="tm-article-snippet__datetime-published").find("time")
    if (KEYWORDS[0]  in art_s[0]) or (KEYWORDS[1] in art_s[0]) or (KEYWORDS[2] in art_s[0]) or (KEYWORDS[3] in art_s[0]):      
        print(time_)
        print(title)
        print(href)
#        print(art_s)  
        print()






