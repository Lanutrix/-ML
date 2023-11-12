import requests
from bs4 import BeautifulSoup

cookies = {
    '_ym_uid': '169979368067221227',
    '_ym_d': '1699793680',
    '_ym_isad': '2',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': '_ym_uid=169979368067221227; _ym_d=1699793680; _ym_isad=2',
    'DNT': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://health-diet.ru/base_of_food/sostav/16017.php', cookies=cookies, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Найти все строки в таблице
rows = soup.select('table.mzr-table tbody tr')[1:9]

# Пройтись по каждой строке и извлечь данные
for row in rows:
    nutrient_cell = row.select_one('td')
    if nutrient_cell:
        nutrient = nutrient_cell.get_text(strip=True)
        amounts = row.select('td')[1].get_text(strip=True)
        print(f'{nutrient}: {amounts}')