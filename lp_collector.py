import requests
from bs4 import BeautifulSoup
import time
# http://lp-web.com/food/index_2.html

def main():
    link = []
    res = requests.get('http://lp-web.com/food')
    res.raise_for_status()
    site_source = res.text
    
    soup = BeautifulSoup(site_source, "html.parser")
    links = (soup.find_all(class_="asset-image"))
    print(links)
    for link in links:
        print(link.get("href"))
    # print(links.get("href"))
    # print(soup)
    
    
if __name__=="__main__":
    main()

