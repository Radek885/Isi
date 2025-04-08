import requests
from bs4 import BeautifulSoup
import csv

class Home:
    def __init__(self, header_name, price, price_for_m2):
        self.header_name = header_name
        self.price = price
        self.price_for_m2 = price_for_m2

def get_homes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    homes = []
    for offer in soup.find_all('article', class_='css-136g1q2 eg92do40'):
        header_name = offer.find('p', class_='css-u3orbr e1g5xnx10').text
        price = offer.find('span', class_='css-2bt9f1 evk7nst0').text
        price_for_m2 = offer.find('span', class_='offer-item-price-per-m').text
        homes.append(Home(header_name, price, price_for_m2))
    return homes

def write_to_csv(filename, homes):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['header_name', 'price', 'price_for_m2'])
        for home in homes:
            writer.writerow([home.header_name, home.price, home.price_for_m2])

if __name__ == '__main__':
    url = 'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing'
    homes = get_homes(url)
    write_to_csv('home.csv', homes)
