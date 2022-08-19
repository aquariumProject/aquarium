import os 
import re
from unittest import result
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

# import json
# from collections import OrderedDict

os.environ.setdefault('DJANGO_SETTINGS_MODULE','aquarium.settings')
import django
django.setup()
from store.models import Item

def store_search_data():
    result=[]
    web_root="https://www.coupang.com"
    url="https://www.coupang.com/np/search?component=&q=%EA%B5%AC%ED%94%BC%EB%B0%A5&channel=user"
    #url="https://www.coupang.com/np/search?q=%EA%B5%AC%ED%94%BC%EB%B0%A5&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
    headers={   'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,zh;q=0.5',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
                    'Accept-Encoding': 'gzip'
                    }   
    #url="https://www.coupang.com/np/search?q="+searchWord+"&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
    res=requests.get(url, headers=headers)
    res.raise_for_status()

    soup=BeautifulSoup(res.text,"html.parser")

    items=soup.find_all("li",attrs={"class":re.compile("search-product")})

    #print(items[0].find("div",attrs={"class":"name"}).get_text())
    for item in items:
        #광고 제품은 제외 
        ad_badge=item.find("span",attrs={"class":"ad-badge-text"})
        if ad_badge:
            continue

        #상품명
        item_name=item.find("div",attrs={"class":"name"}).get_text()

        #가격
        item_price=item.find("strong",attrs={"class":"price-value"}).get_text()

        #할인율 
        item_rate=item.find("span",attrs={"class":"instant-discount-rate"}) #할인율
        if item_rate:
            item_rate=item_rate.get_text()
        else:
            item_rate="할인 없음"

        #링크
        link = web_root+item.find("a",attrs={"class":"search-product-link"})["href"]
        link_parts=urlparse(link) #출력예시:ParseResult(scheme='https', netloc='www.coupang.com', path='/vp/products/9351169', params='', query='itemId=41043188&vendorItemId=3062715608&pickType=COU_PICK', fragment='')
        item_link=link_parts.scheme + '://' + link_parts.hostname + link_parts.path

        #itemID
        item_code=link_parts.path.split('/')[-1]

        #list 저장
        item_obj={
            'item_code':item_code,
            'item_name':item_name,
            'item_price':item_price,
            'item_rate':item_rate,
            'item_link':item_link,
        } 
        result.append(item_obj)

    return result
        #print(item_name,item_price,item_rate,item_link,item_code)

# store_search_data()

def add_items(crawled_items):
    #json_data=OrderedDict()
    last_inseted_items=Item.objects.last()
    print(last_inseted_items)
    if last_inseted_items is None:
        last_inseted_item_id=""
    else:
        last_inseted_item_id=getattr(last_inseted_items,'item_code')

    item_insert_into_db=[]
    for item in crawled_items:
        if item['item_code']==last_inseted_item_id:
            break
        item_insert_into_db.append(item)
    item_insert_into_db.reverse()
    for item in item_insert_into_db:
        print("item add!!"+ item['item_name'])
        #print(json.dumps(item,ensure_ascii=False,indent="\t"))

        Item(item_code=item['item_code'],
        item_name=item['item_name'],
        item_price=item['item_price'],
        item_rate=item['item_rate'],
        item_link=item['item_link']).save()

result_items=store_search_data()
#print(Item.objects.last())
#print(result_items)
add_items(result_items)



    



