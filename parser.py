from bs4 import BeautifulSoup
from requests import get
from database import DATABASE_NAME, create_db, session
import os
from city import City


db_exists = os.path.exists(DATABASE_NAME)
if not db_exists:
    create_db()
response = get('https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B8%D0%B5_%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D1%91%D0%BD%D0%BD%D1%8B%D0%B5_%D0%BF%D1%83%D0%BD%D0%BA%D1%82%D1%8B_%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B9_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D0%B8')
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', attrs={'class': 'standard sortable'})
rows = table.find_all('tr')

first_elem = True
for row in rows:
    if first_elem:
        first_elem = False
        continue
    cities = row.find_all('td')

    curr_city = City(name = cities[1].a.get('title'),
                     count=cities[4].get('data-sort-value'),
                     url='https://ru.wikipedia.org/' + cities[1].a.get('href'))
    session.add(curr_city)
session.commit()


