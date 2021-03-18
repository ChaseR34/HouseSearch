from requests_html import HTMLSession
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'HouseSearch.settings')

django.setup()

from houses.models import CraigsList


session = HTMLSession()


url = "https://flagstaff.craigslist.org/search/apa"

search_params = {
    "sort": "date",
    "min_bedrooms": 2,
    "availabilityMode": 2,
    "postedToday": 1,
    "search_distance": 20,
    "sale_date": "all+dates"

}

r = session.get(url, params=search_params)

r.html.render()

li = r.html.find('.result-row')
# title = li[0].find('.result-heading', first=True)
# print(title)

for i in li:
    title = i.find('.result-title', first=True).text
    time = i.find('.result-date', first=True).attrs['datetime']
    link_url = i.find(".result-image", first=True).attrs['href']
    try:
        price = i.find('.result-price', first=True).text
    except:
        price = 0

    try:
        housing = i.find('.housing', first=True).text
        bedrooms = housing.split(' -')[0].strip().lower().replace('br')
        sq_ft = housing.split(' -')[1].strip().lower().replace('ft2')



    except:
        housing = "Unknown"
    try:
        hood = i.find('.result-hood', first=True).text
    except:
        hood = "unknown"




    print(title)
    print(price)
    print(housing.split(' -')[0].strip())
    print(housing.split(' -')[1].strip().replace('ft2',''))
    print(hood)
    print(time)
    print(link_url)
    img = i.find('img')
    for j in img:
        print(j.attrs['src'])
