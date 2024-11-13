import requests
from datetime import date
import pyodbc 
con = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};Server=tcp:newsserver.database.windows.net,1433;Database=news;Uid=harry;Pwd=Paper11Duck;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
today = str(date.today().strftime('%Y-%m-%d'))
print (today)
cursor = con.cursor()
cursor.execute("select keyword from keywords")
row = cursor.fetchone()
row = cursor.fetchone()
print(row[0])
url = ('https://newsapi.org/v2/top-headlines?'
       'q='+row[0]+'&'
       'from='+today+'&'
       'to='+today+'&'
       'sortBy=publishedAt&'
       'apiKey=7d24d15d79ea4d2496d5b74b2741d12e')
print(url)
response = requests.get(url)
print (response)
for article in response.json()["articles"]:
    print (article['url'])


con.close()