import requests
from bs4 import BeautifulSoup
result= requests.get("https://en.wikipedia.org/wiki/Kerala_State_Film_Award_for_Best_Actor")
soup=BeautifulSoup(result.content,'lxml')


table=soup.find_all('table',{"class":"wikitable sortable plainrowheaders"})[0]

#print(table)
rows=table.find_all('tr')
for row in rows:
   cols=row.find_all(['td','th'])
   print(cols)