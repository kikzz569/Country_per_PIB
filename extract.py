import pandas as pd 
from datetime import datetime
from bs4 import BeautifulSoup
import requests

url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
table = soup.find_all('tbody')
rows = table[2].find_all('tr')

def extract():
    data = []
    for row in rows:
        col = row.find_all('td')
        if len(col)!=0:
            if col[0].find('a') is not None and '—' not in col[2]:
                country = col[0].text.strip()
                PIB_FMI = col[2].text.strip()
                year = col[3].text.strip()
                data.append({'country': country, 'PIB_FMI': PIB_FMI, 'year': year})
    df = pd.DataFrame(data, columns=['country', 'PIB_FMI', 'year'])
    return df
