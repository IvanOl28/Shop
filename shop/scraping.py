import requests
from bs4 import BeautifulSoup as BS

from main.settings import URL_SCRAPING_DOMAIN, URL_SCRAPING
from shop.models import Product


class ScrapingError(Exception):
    pass


class ScrapingTimeoutError(ScrapingError):
    pass


class ScrapingHTTPError(ScrapingError):
    pass


class ScrapingOtherError(ScrapingError):
    pass


def scraping():
    try:
        resp = requests.get(URL_SCRAPING, timeout=10.0)
    except requests.exceptions.Timeout:
        raise ScrapingTimeoutError("request timed out")
    except Exception as e:
        raise ScrapingOtherError(f'{e}')

    if resp.status_code != 200:
        raise ScrapingHTTPError(f"HTTP {resp.status_code}: {resp.text}")

    data_list = []
    html = resp.text
    soup = BS(html, 'html.parser')
    blocks = soup.select('.col-6.col-md-3')
    code = 2145678990
    unit = 'за шт'
    for block in blocks:
        data = {}
        brand = block.select_one('.prod__brand').get_text().strip()
        data['brand'] = brand

        name = block.select_one('.prod__title').get_text().strip()
        data['name'] = name

        image_url = URL_SCRAPING_DOMAIN + block.select_one('img')['src']
        data['image_url'] = image_url

        price_raw = block.select_one('.prod__price').text
        price_raw = price_raw.split(' ')
        del price_raw[-1]
        price_raw = "".join(price_raw)
        price = price_raw.replace('\xa0', '')
        data['price'] = price  # 20990

        data['code'] = code
        data['unit'] = unit

        data_list.append(data)

        code = code + 1

    print(data_list)

    for item in data_list:
        if not Product.objects.filter(code=item['code']).exists():
            Product.objects.create(
                name=item['name'],
                code=item['code'],
                price=item['price'],
                unit=item['unit'],
                image_url=item['image_url'],
                brand=item['brand'],

            )


if __name__ == '__main__':
    scraping()
