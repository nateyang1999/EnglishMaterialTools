from matplotlib.pyplot import getp
import requests
from bs4 import BeautifulSoup
from urllib import request
from fake_useragent import UserAgent
import time
import sys

CAMBRIDGE_DICTIONARY_URL = "https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/"
YAHOO_DICTIONARY_URL = "https://tw.dictionary.yahoo.com/dictionary?p="

ua = UserAgent()

def getHTML(url):
    headers = {'User-Agent': ua.random }
    req = request.Request(url, headers=headers)
    return request.urlopen(req).read()

def getPos(w):
    if w == "noun":
        return "n."
    elif w== "adjective":
         return "adj."
    elif w == "adverb":
        return "adv."
    elif w== "verb":
        return "v."
    elif w=="preposition":
        return "prep."
    elif w=="conjunction":
        return "conj."
    elif w=="determiner":
        return "art."
    elif w=="pronoun":
        return "pron."
    else:
        return ""

in_filename = sys.argv[1]
out_filename = "out_"+in_filename
f = open(in_filename,"r",encoding="utf-8")

with open(out_filename, 'w', encoding='utf-8') as f_out:
    for word in f:
        word = word.strip()
        soup = BeautifulSoup(getHTML(CAMBRIDGE_DICTIONARY_URL+word),"html.parser")
        soup_kk = BeautifulSoup(getHTML(YAHOO_DICTIONARY_URL+word),"html.parser")
        
        pos = soup.find("span","pos dpos")
        if pos == None:
            pos_short = "查無詞性"
        else:
            pos_short = getPos(pos.text)
        
        kk=soup_kk.find_all('li',{'class':'d-ib mr-10 va-top'})
        k_str = "[查無音標]"
        for k in kk:
            k_str = k.text[2:]
        
        meaning=soup.find("span",attrs={"class":"trans dtrans dtrans-se break-cj"})
        if meaning == None:
            m_str = "查無中文解釋"
        else:
            m_str = meaning.text
        
        row = word + " ("+pos_short+") "+m_str+" "+k_str+"\n"
        # print(row)
        f_out.write(row)
        

print("完成 輸出檔名:"+out_filename)
print("程式結果僅抓取第一筆解釋，可能有一字多義/同拼法不同詞性等狀況，請務必再次校對")