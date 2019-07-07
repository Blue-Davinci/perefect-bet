import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import  webdriver

file = "C:\\Users\\Blue_Davinci\\Downloads\\Sites\\mCHEZA1.html"
#req = requests.get('https://www.mcheza.co.ke/sports')
soup = ''
with open(file,'rb') as fp:
    soup = BeautifulSoup(fp,'html.parser')
#url = 'https://www.mcheza.co.ke/sports'
#browser = webdriver.Chrome()
#browser.get(url)
#html = browser.page_source
#soup = BeautifulSoup(html,'html.parser')

team1Names = []
team1Odds = []
teamDraw = []
team2Names = []
team2Odds =[]
#sport-section selected
game = soup.find_all("div",{"class":"match-section-sport-content"})
pop = game[0].find_all("div",{"class":"sport-section selected"})
for elem in pop:
    #print(elem)
    games = elem.find_all("div",{"class":"matches-set"})
    for match in games:
        print(match)
        for table in match:
            y = table.find("div", {"class": "match-teams"}).get_text()
            if y != None:
                team1Names.append(y.split(" v ")[0])
                team2Names.append(y.split(" v ")[1])
            draw = table.find("div", {"class": "selection-button selection-button-1"}).get_text()
            if draw != None:
                team1Odds.append(draw[1:])

            if table.find("div", {"class": "selection-button selection-button-X"}):
                odd1 = table.find("div", {"class": "selection-button selection-button-X"}).find("div",
                                                                                                {
                                                                                                    "class": "sel-odds"}).get_text()
                teamDraw.append(odd1)

            odd2 = table.find("div", {"class": "selection-button selection-button-2"}).get_text()
            if odd2 != None:
                team2Odds.append(odd2[1:])

teamTable = pd.DataFrame({
    "Team1": team1Names,
    "Team1odd": team1Odds,
    "MatchDraw": teamDraw,
    "Team2": team2Names,
    "Team2Odd": team2Odds
})
teamTable = teamTable[['Team1', 'Team1odd', 'MatchDraw', 'Team2', 'Team2Odd']]
pd.set_option('display.expand_frame_repr', False)
# print("\t ================================ M-Cheza ==============================")
# print(teamTable)
print("\t ================================ M-Cheza ==============================")
print(teamTable)
