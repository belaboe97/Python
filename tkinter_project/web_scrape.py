from bs4 import BeautifulSoup
import requests
from requests import get
from lib.sitepackages import pypyodbc
import soupsieve


DBfile = '.\\NewsChecker.mdb'
conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ='+DBfile)

myCursor = conn.cursor()    
#SQL = "CREATE TABLE newsChecker"  #IF NOT EXISTS // MS ACCESS DONT SUPPORT CONTROL FLOW :(
#row = myCursor.execute(SQL)
#myCursor.commit()



url = 'https://www.learnlaravel.me/getting-started/'


response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

content = html_soup.find('div',"entry-content")

listelements =  content.findAll('li')

price= content.li
link = price

contentList = []

for i in listelements:
    name = i.prettify().split('"')[3]
    contentList.append(name)

counter = 0
for content in contentList:
    myCursor = conn.cursor()
    print(content)
    SQL_insert = "insert into newsChecker(num1,Header) values ('"+str(counter)+"','"+content+"')"
    row = myCursor.execute(SQL_insert)
    myCursor.commit()
    counter += 1
    


print(len(contentList))

print(response.text)
print(content)
print(contentList)
