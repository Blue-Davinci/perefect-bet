import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://www.sportpesa.com/?sportId=1"
browser = webdriver.Chrome()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

events = soup.find_all('div', {'class': 'bp-events upcomingmatches'})

for tables in events: #getting the 2 tables
    for matches in tables:
        try:
            firststep = matches.find("ul", {"class": "bet-selector"})
            seconstep = firststep.find("li", {'class': 'pick01'})
            finalstep = seconstep.find("span", {"class": "team"}).get_text()
            print(finalstep)
        except:
            continue


