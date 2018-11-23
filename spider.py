import urllib.request
from bs4 import BeautifulSoup


def get_data(phone, page):
    url = f'https://www.pdflibr.com/SMSContent/{phone}?page={page}'
    print(url)

    try:
        response = urllib.request.urlopen(url).read()
    except:
        response = get_data(phone, phone)

    return response


phone = 3
pages = list(range(1, 101))
tables = []
for page in pages:
    res = get_data(phone, page)
    soup = BeautifulSoup(res.decode(), 'lxml')
    table = soup.findAll('table')[1]
    tables.append(table)
with open(f'phone_{phone}.txt', 'wb') as f:
    for table in tables:
        f.write(table.get_text().encode('utf-8'))