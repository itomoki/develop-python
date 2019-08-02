from bs4 import BeautifulSoup
import urllib.request as req

url = "https://su-gi-rx.com/2017/07/16/python_4/"

res = req.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')

title1 = soup.find("h1").string
print("title = ", title1)

p_list = soup.find_all("p")
print("text = ", p_list)

