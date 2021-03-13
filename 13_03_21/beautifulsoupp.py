import requests
from bs4 import BeautifulSoup

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
rest_dict = []
if div:
    all_restaurants = div.find_all('a')
    for restaurant in all_restaurants:
        infos = restaurant.find('div', attrs={"class": "manufacturer-info"}).stripped_strings
        img = restaurant.find('img')
        rest_dict.append({
            "name": next(infos),
            "open_hours": next(infos),
            "image_url": restaurant.find('img')['src']
        })
print(rest_dict)
# soup = BeautifulSoup(data, 'xml')
# data_2 = "<html> string <a href='href' /> <new_tag> string  </new_tag> </html>"
# soup_2 = BeautifulSoup(data_2, 'html.parser')
# print(soup_2.html.contents)

# print(soup.find_all('div', attrs={'class': "listing im-manufacturers-listing"}))



