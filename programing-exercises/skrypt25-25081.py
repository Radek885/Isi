import requests
from bs4 import BeautifulSoup

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return [a['href'] for a in soup.find_all('a', href=True)]

if __name__ == '__main__':
    url = 'https://wp.pl'
    links = get_links(url)
    print("Hiperlacza:", links)
