import requests,json
from bs4 import BeautifulSoup
from pprint import pprint
url="https://www.collegedekho.com/btech-mechanical_engineering-colleges-in-india/"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
rr=soup.find("div",class_="row collegeBlock")
ff=rr.find_all("div",class_="title")
list1=[]
list2=[]
for i in ff:
    pp="https://www.collegedekho.com"+i.find("a")["href"]
    list1.append(pp)
print(list1)
for i in list1:
    dict1={}
    r=requests.get(i)
    soup=BeautifulSoup(r.text,"html.parser")
    dd=soup.find("div",class_="collegeInfo").text
    dict1["name"]=(dd.split("\n")[0])
    ss=soup.find("td",class_="data") 
    dict1["type"]=(ss.text)
    ad=soup.find("span",class_="location")
    dict1["address"]=(ad.text)
    addd=soup.find("ul",class_="addressList")
    asd=addd.text.split("\n")
    a=0
    for i in asd:
        if a==3:
            dict1["content"]=(i.replace("         ",""))
        if "@" in i:
            dict1["email"]=(i.replace("         ",""))
        a+=1
    dict1["Facilities"]=soup.find("div",class_="block facilitiesBlock").find("div",class_="box").text
    fff=soup.find_all("div",class_="rating-per")
    for i in fff:
        a=(i.find("div",class_="star-ratings-sprite"))
        b=(str(a).split("=")[-1][7:11])
        dict1["Rating"]=(float(b)/20)
    list2.append(dict1)
pprint(list2)
r=open("collage.json","w")
json.dump(list2,r,indent=4)