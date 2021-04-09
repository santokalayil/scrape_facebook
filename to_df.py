from bs4 import BeautifulSoup
import os
import pandas as pd
import pyperclip as pc
import pyautogui as pag
import json
import pandas as pd

with open('friends.html','r',encoding="utf8") as f:
    html_doc = f.read()

html_doc
soup = BeautifulSoup(html_doc, 'html.parser')
items = [i for i in soup.find_all("div", {"class":'_55wp _7om2 _5pxa _8yo0'})]

frd = items[4634]

cols = ['linkId','name','mutual','unq_id','gfid']
df = pd.DataFrame(columns= cols)
for i, frd in enumerate(items):
    print(i,'items ..',end='\r')
    div1 = frd.find('div',{'class':'_5s61 _2b4m _8yo0'})
    linkId = div1.a['href']

    div2 = frd.find('div',{'class':'_4g34 _5pxb _5i2i _52we'})
    try:
        name = div2.find('h1').text
        
    except:
        try:
            name = div2.find('h3').text
            #name = div2.find('h1').text # div2.find('h1').text
        except:
            name = 'not found'
    try:
        mutual = int(div2.find('div',{'class':'notice ellipsis'}).text.split(' ')[0])
    except:
        mutual = 0
    div3 = frd.find('div',{'class':'_5s61 _8-j9 _5i2i _52we'})
    d = json.loads(div3.find('a',{'data-sigil':'touchable m-add-friend'})['data-store'])
    unq_id = d['id']
    gfid = (div3.find('a',{'data-sigil':'touchable m-add-friend'})['href']).split('&gfid=')[-1]

    new = pd.DataFrame(pd.Series({'linkId':linkId,'name':name,'mutual':mutual,'unq_id':unq_id, 'gfid':gfid})).T
    df = pd.concat([df,new],sort=False)

df = df.reset_index().drop('index',axis=1)
print(df)

