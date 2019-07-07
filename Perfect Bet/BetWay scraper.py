import requests
from bs4 import BeautifulSoup
import pandas as pd
'''
frame = pd.DataFrame([
        [1, .1, 'a'],
        [2, .2, 'e'],
        [3,  1, 'i'],
        [4,  4, 'o']
    ], columns=['one thing', 'second thing', 'other thing'])
    '''
file = "C:\\Users\\Blue_Davinci\\Downloads\\Sites\\Sports betting on Betway.co.ke _ Best online betting odds in Kenya.html"

with open(file,'rb') as fp:
    soup = BeautifulSoup(fp,'html.parser')

games = soup.find_all("div",{"class":"fixture-holder"})
team1Names = []
team1Odds = []
teamDraw = []
team2Names = []
team2Odds =[]
teamOddList = []
uniCounter = 1 #reset to 1 in self
for elem in games:
    x = elem.find_all("div", {"class": "inplayStatusDetails"})
    for team in x:
        y = team.find('b').get_text()
        team1Names.append(y.split(" v ")[0][3:])
        team2Names.append(y.split(" v ")[1])

    odds = elem.find_all("div",{"class":"outcomeBtnLong outcomebuttonDiv"})
    for od in odds:
        teamOddList.append(od.find("div",{"class":"outcome-pricedecimal "}).get_text())
    #match odds
    for teamodd in teamOddList:
        if uniCounter%2 == 0:
            team1Odds.append(teamodd)
        else:
            team2Odds.append(teamodd)
        uniCounter +=1
    draws = elem.find_all("div",{"class":"outcomeBtnShort outcomebuttonDiv"})
    for draw in draws:
        teamDraw.append(draw.find("div",{"class":"outcome-pricedecimal drawPriceDecimal"}).get_text())

teamTable = pd.DataFrame({
    "Team 1": team1Names,
    "| Team 1 odd": team1Odds,
    "| Match Draw": teamDraw,
    "| Team 2": team2Names,
    "| Team 2 Odd": team2Odds

})
teamTable = teamTable[['Team 1', '| Team 1 odd', '| Match Draw', '| Team 2', '| Team 2 Odd']]
pd.set_option('display.expand_frame_repr', False)
print("\t ================================ Bet-Way ==============================")
print(teamTable)
teamTable.to_csv('betway.csv')