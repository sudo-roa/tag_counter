import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import collections

load_dotenv()
URL = os.environ['URL']

def tag_extraction(text):
    tags = []
    for i in range(len(text)):
        tag = ""
        if(text[i]=='<' and text[i+1]!='/'):
            i+=1
            # htmlのタグで一番長いのがblockquoteなので10
            for j in range(10):
                if(text[i+j]==" " or text[i+j]==">"):
                    break
                tag += text[i+j]
            tags.append(tag)
    return tags

def tag_counter(tags):
    print(collections.Counter(tags))

def main():
    res = requests.get(URL)
    site_source = res.text
    print(tag_extraction(site_source))
    tags = tag_extraction(site_source)
    tag_counter(tags)

if __name__=="__main__":
    main()
