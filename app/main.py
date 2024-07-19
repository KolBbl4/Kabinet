import requests
from bs4 import BeautifulSoup

def main():
    url = 'ya.ru'
    #headers = {};
    reg = requests.get(url)
    print( reg.content)

def con():
    pass

if __name__ == "__main__":
    main()