# htmlのソースを取ってくる(動的に)
# タグを抽出する
# タグを出現頻度とa-z順に並び替える
# グラフ化する

from selenium import webdriver
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import os
import time

load_dotenv()
URLS = os.environ['URLS'].split(',')
HTML_ALL_TAGS = ["<--", "a", "abbr", "acronym", "address", "area", "article", "aside", "audio", "b", "bdi", "bdo", "blockquote", "br", "button", "canvas", "cite", "code", "data", "datalist", "del", "details", "dfn", "dialog", "div", "dl", "em", "embed", "fieldset", "figure", "footer", "form", "h1", "h2", "h3", "h4", "h5", "h6", "header", "hgroup", "hr", "i", "iframe", "img", "input", "ins", "kbd", "label", "link", "main", "map", "mark", "math", "menu", "meta", "meter", "nav", "noscript", "object", "ol", "output", "p", "picture", "pre", "progress", "q", "ruby", "s", "samp", "script", "section", "select", "slot", "small", "span", "strong", "sub", "sup", "svg", "table", "template", "textarea", "time", "u", "ul", "var", "video", "wbr"]

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


# tagのリストからmatplotlibでグラフを作成できるように辞書形式で整形する()
# 複数サイトのtagリストから出現したかどうかを判定して辞書へ
# この関数を使うなら、mainで集計用の辞書を初期化して引数として渡す必要あり
def check_appearance_tag(tag_dict, tag_list):
    # 重複判定、重複したタグを消す
    tag_list = list(set(tag_list))
    print(tag_list)    
    
    # 辞書に追加
    for tag in tag_list:
        if tag not in tag_dict.keys():
            continue
        else:
            tag_dict[tag]  += 1
    return tag_dict

# matplotlibで棒グラフの作成前のデータ整形
# 出現頻度の降順に且つa-z順に辞書を並べ直す
def align_appearance_tag(tag_dict):
    x_axis = [i for i in range(len(tag_dict))]
    y_axis = [value for value in tag_dict.values()]
    label = [key for key in tag_dict.keys()]
    plt.bar(x_axis, y_axis, tick_label=label, align="center")
    plt.xticks(rotation=90)
    plt.show()

# matplotlibへの描画処理
def make_bargraph():
    pass


def main():
    tag_dict = {}
    #辞書の初期化
    for html_all_tag in HTML_ALL_TAGS:
        tag_dict[html_all_tag] = 0
    print(URLS)
    for url in URLS:
        driver = webdriver.Firefox()
        time.sleep(1)
        driver.get(url)
        time.sleep(5)
        site_source = driver.page_source
        tag_list = tag_extraction(site_source)
        check_appearance_tag(tag_dict, tag_list)
        #print(driver.page_source)
        driver.close()
        driver.quit()
    
    # 全サイト検索後、タグの統計を取る
    align_appearance_tag(tag_dict)
    
    #     tags = tag_extraction(site_source)
    #     tag_counter(tags)
    #     time.sleep(1)
    # driver = webdriver.Chrome('/usr/bin/google-chrome-stable')
    

if __name__=="__main__":
    main()                                                                  
