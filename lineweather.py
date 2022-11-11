import requests
import requests
from bs4 import BeautifulSoup

# 取得したTokenを代入
line_notify_token = 'D1HxJWuaLSiW92TTxnmPWVz6SDj8iYoAzHCfQDrP7dX'
line_notify_api = 'https://notify-api.line.me/api/notify'
headers = {'Authorization': f'Bearer {line_notify_token}'}

# 天気取得
hujiidera = 'https://tenki.jp/forecast/6/30/6200/27226/'
katano = 'https://tenki.jp/forecast/6/30/6200/27230/'

url2 = hujiidera
res = requests.get(url2)
soup = BeautifulSoup(res.content, 'html.parser')

hiduke = soup.find(class_="left-style").text
telop = soup.find("p", class_="weather-telop").text
highlists = soup.find("dd",class_="high-temp temp").text
lowlists = soup.find("dd",class_="low-temp temp").text

if url2 in hujiidera:
    place = '藤井寺市'
elif url2 in katano:
    place = '交野市'
else:
    place = ''

message = place + '\n' + hiduke + '\n' + '今日の天気' + telop + '\n' + '最高気温' + highlists + '\n' + '最低気温' + lowlists

data = {'message': f'{message}'}
requests.post(line_notify_api, headers=headers, data=data)