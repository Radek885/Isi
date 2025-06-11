import requests
from bs4 import BeautifulSoup
import csv

class Home:
    def __init__(self, header_name, price, price_for_m2):
        self.header_name = header_name
        self.price = price
        self.price_for_m2 = price_for_m2

def get_homes(url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    homes = []

    for offer in soup.find_all('article'):
        try:
            header_elem = offer.find('p', attrs={'data-cy': 'listing-item-title'})
            price_elem = offer.find('span', class_='css-2bt9f1')
            price_m2_elem = offer.find('dd', attrs={'data-sentry-component': 'PricePerMeterDefinition'})

            if header_elem and price_elem and price_m2_elem:
                price_m2_span = price_m2_elem.find('span')
                home = Home(
                    header_name=header_elem.text.strip(),
                    price=price_elem.text.strip(),
                    price_for_m2=price_m2_span.text.strip() if price_m2_span else 'brak danych'
                )
                homes.append(home)
        except Exception as e:
            print(f"Błąd przy przetwarzaniu oferty: {e}")

    return homes

def write_to_csv(filename, homes):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['header_name', 'price', 'price_for_m2'])
        for home in homes:
            writer.writerow([home.header_name, home.price, home.price_for_m2])

if __name__ == '__main__':
    url = 'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing'
    homes = get_homes(url)
    write_to_csv('home.csv', homes)
    print(f"Zapisano {len(homes)} ofert do pliku home.csv.")
