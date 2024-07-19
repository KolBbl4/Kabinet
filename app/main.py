import requests
from bs4 import BeautifulSoup

def main():
    res = con()
    print(res)

def con():
    url = 'https://ya.ru/'
    reg = requests.get(url)
    return reg.content

if __name__ == "__main__":
    main()