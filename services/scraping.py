from bs4 import BeautifulSoup
import re
import requests

def scraping_categories():
    response = requests.get("https://www.dbs-cardgame.com/fw/jp/cardlist")
    soup = BeautifulSoup(response.content, "html.parser")
    tags = soup.find_all("ul", class_="js-toggle--01 filterListItems js-add--toggleElem js-toggle--selectBox")
    categories = []
    for ul_tags in tags:
        for li in ul_tags.select('li'):
            pattern = r'data-val=\"(.*)' 
            value = str(re.findall(pattern, str(li.find("a")))).split('\"')[0].lstrip('[\'')
            categories.append({"name": li.text, "value": value})
    return {"categories": categories}

def scraping_image_url(url: str, categoryId: str, categoryName: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    uls = soup.find_all("div", class_="cardCol")
    data = []
    for ul in uls:
        for li in ul.select('li'):
            data.append({
                "name": str(li.find("img")['alt']), 
                "url": "https://www.dbs-cardgame.com/fw/" + str(li.find("img")['data-src']).lstrip('../../'),
                "categoryId": categoryId,
                "categoryName": categoryName
            })
    return {"cards": data}