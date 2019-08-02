# crawl.py

# モジュールのインポート
import urllib.request as req
from bs4 import BeautifulSoup
import time

# 任意のURLからデータを取得
url = "https://su-gi-rx.com/"
res = req.urlopen(url)

"""
特定URL内にあるリンクを抽出
抽出データのHTML解析を行い、リンクをリスト化
"""
soup = BeautifulSoup(res, 'html.parser')
links = soup.select("a[href]")
result = []
for a in links:
	href = a.attrs["href"]
	title = a.string
	result.append((title, href))

"""
リンク先の<p>タグ内のテキストを抽出
抽出データを記事タイトルごとにtxtファイルに書き込み作成
"""
for title, url in result:
	print("link = " + url)
	time.sleep(1)
	res_1 = req.urlopen(url)
	soup_1 = BeautifulSoup(res_1, 'html.parser')
	p_list = soup_1.find_all("p")
	for p in p_list:
		print(p.get_text())
		with open("{}.txt".format(title), mode="a") as f:
			f.write(p.get_text())
