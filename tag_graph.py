import os
import requests
from dotenv import load_dotenv
# ↓あんま使わんほうが良さげ？
import collections
import time
import matplotlib.pyplot as plt

load_dotenv()
URL = os.environ['URL']

########## 関数
# URLからtagを抽出してリストで返す(["body", "ol", "li", ...])
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
            # if(tag!="line" and tag!="rect" and tag!="circle" and tag!="ellipse" and tag!="polygon" and tag!="text" and tag!="polyline" and tag!="path"):
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
            tag_dict[tag] = 1
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
    plt.xticks(rotation=45)
    plt.show()

# matplotlibへの描画処理
def make_bargraph():
    pass


# tagのリストを受け取って、タグの数を集計する
# formatが良くないのでmatplotlibには使いづらい？ので自作のカウンターが正確なことを証明するために使う
def tag_counter(tags):
    counts = collections.Counter(tags)
    print(counts)

def main():
    tag_dict = {}
    print(URL)
    # access to site and extract tags
    res = requests.get(URL)
    site_source = res.text
    tag_list = tag_extraction(site_source)
    print(tag_list)
    check_appearance_tag(tag_dict, tag_list)
    tag_counter(tag_list)
    print(tag_dict)
    print(len(tag_dict))
    align_appearance_tag(tag_dict)


if __name__=="__main__":
    main()
    