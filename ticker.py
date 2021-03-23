from bs4 import BeautifulSoup
import requests
#source = requests.get("https://merolagani.com/LatestMarket.aspx").text
source = requests.get("http://www.nepalstock.com/todaysprice").text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

table = soup.find('table')
# print(table.prettify())

content = table.find('tr')
#data = content.find('td')
print(content)
