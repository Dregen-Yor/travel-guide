import requests
from bs4 import BeautifulSoup
from components.Scene import scene

url="https://zwfw.mct.gov.cn/scenicspot?type=gb&pageNum="

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
}

def getList():    
    list=[]
    for i in range(1,24):
        response = requests.get(url+str(i), headers=headers)
        soup=BeautifulSoup(response.text,'html.parser')
        item=soup.find('div',class_="right-page-list")
        for j in item.find_all('tr'):
            items=j.find_all('td')
            if(items==[]):
                continue
            name=items[0].find('a').text
            location=items[1].text
            list.append(scene(name,location))


    return list
    
