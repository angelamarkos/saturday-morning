import requests
import os
from bs4 import BeautifulSoup

from class_20_03_21.helpers import get_session, send_email_for
from class_20_03_21.models import Restaurant, DB_NAME
from sqlalchemy import engine_from_config



ENDPOINT = 'https://buy.am/hy/food-court?p={}'

# page = 1
# while page<18:
#     response = requests.get(ENDPOINT.format(page))
#
#     if response.status_code == 200:
#         with open(f'buyam_{page}.html', 'w+b') as file:
#             file.write(response.content)
#         page += 1
#
#     else:
#         print(response, page)

with open('buyam.html', 'r') as html_file:
    data = html_file.read()

soup = BeautifulSoup(data, 'html.parser')
div = soup.find('div', attrs={'class': "listing im-manufacturers-listing"})
session = get_session()
new_restaurants = []
if div:
    all_restaurants = div.find_all('a')
    for restaurant in all_restaurants:
        infos = restaurant.find('div', attrs={"class": "manufacturer-info"}).stripped_strings
        img = restaurant.find('img')['src']
        name_id = os.path.basename(img).split('.')[0]
        existing_restaurant = session.query(Restaurant).filter(
            Restaurant.name_id==name_id).one_or_none()
        if not existing_restaurant:
            restaurant_ = Restaurant(**{
                "name": next(infos),
                "open_hours": next(infos),
                "image_url": img,
                "name_id": name_id,
                "service_id": 1
            })
            session.add(restaurant_)
            new_restaurants.append(name_id)
        else:
            existing_restaurant.name = next(infos)
            existing_restaurant.open_hours = next(infos)
            session.add(existing_restaurant)

        session.commit()

send_email_for(new_restaurants)

print(*((restaurant.name_id, restaurant.name, restaurant.restauran_id) for restaurant in session.query(Restaurant).all()), sep='\n')
# soup = BeautifulSoup(data, 'xml')
# data_2 = "<html> string <a href='href' /> <new_tag> string  </new_tag> </html>"
# soup_2 = BeautifulSoup(data_2, 'html.parser')
# print(soup_2.html.contents)

# print(soup.find_all('div', attrs={'class': "listing im-manufacturers-listing"}))



