import os
import requests
from dotenv import load_dotenv
import collections
import time

load_dotenv()
URLS = os.environ['URLS'].split(',')


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
                if(tag=="!--"):
                    break
#            if(tag!="line" and tag!="rect" and tag!="circle" and tag!="ellipse" and tag!="polygon" and tag!="text" and tag!="polyline" and tag!="path"):
            tags.append(tag)
    return tags

def tag_counter(tags):
    counts = collections.Counter(tags)
    print(counts)

def main():
    print(URLS)
    for URL in URLS:
        res = requests.get(URL)
        site_source = res.text
        tags = tag_extraction(site_source)
        tag_counter(tags)
        time.sleep(1)

if __name__=="__main__":
    main()


