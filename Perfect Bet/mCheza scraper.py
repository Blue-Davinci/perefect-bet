'''
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

file = "C:\\Users\\Blue_Davinci\\Downloads\\Sites\\mCHEZA1.html"

with open(file,'rb') as fp:
    soup = BeautifulSoup(fp,'html.parser')

url = "https://www.mcheza.co.ke/sports"
browser = webdriver.Chrome()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

games = soup.find_all("div",{"class":"matches-set"})
team1Names = []
team1Odds = []
teamDraw = []
team2Names = []
team2Odds =[]
for elem in games[1]:
    y = elem.find("div",{"class":"match-teams"}).get_text()
    if y != None:
        team1Names.append(y.split(" v ")[0])
        team2Names.append(y.split(" v ")[1])
    draw = elem.find("div",{"class":"selection-button selection-button-X"}).get_text()
    if draw != None:
        teamDraw.append(draw.replace("X",""))
    odd1 = elem.find("div",{"class":"selection-button selection-button-1"}).find("div",{"class":"sel-odds"}).get_text()
    if odd1 != None:
        team1Odds.append(odd1)

    odd2 =elem.find("div",{"class":"selection-button selection-button-2"}).get_text()
    if odd2 != None:
        team2Odds.append(odd2[1:])

teamTable = pd.DataFrame({
    "Team 1": team1Names,
    "| Team 1 odd": team1Odds,
    "| Match Draw": teamDraw,
    "| Team 2": team2Names,
    "| Team 2 Odd": team2Odds
})
teamTable = teamTable[['Team 1','| Team 1 odd','| Match Draw','| Team 2','| Team 2 Odd']]
pd.set_option('display.expand_frame_repr', False)
print("\t ================================ M-Cheza ==============================")
print(teamTable)

y = input("Enter any key to exit: ")
