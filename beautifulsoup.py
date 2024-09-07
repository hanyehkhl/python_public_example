from bs4 import BeautifulSoup
import requests
#bs4
url2="https://www.khabaronline.ir/news/1954691/%D8%B4%D8%B1%D8%A7%DB%8C%D8%B7-%D8%A7%D9%88%D9%84%DB%8C%D9%86-%D8%B1%D9%82%D8%A8%D8%A7%DB%8C-%D8%A7%D8%B3%D8%AA%D9%82%D9%84%D8%A7%D9%84-%D9%88-%D9%BE%D8%B1%D8%B3%D9%BE%D9%88%D9%84%DB%8C%D8%B3-%D8%AF%D8%B1-%D8%A2%D8%B3%DB%8C%D8%A7"
soup = BeautifulSoup(requests.get(url2).features="html.parser".content)
summary=soup.find("div",{"class":"item-summary"})
f=soup.find("p",{"class":"summary introtext"})
print(summary.get_text())
