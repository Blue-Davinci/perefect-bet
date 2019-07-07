import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

file = "C:\\Users\\Blue_Davinci\\Downloads\\Sites\\Upcoming betting events Betpawa.html"
#http://www.betpawa.co.ke/upcoming
#with open(file,'rb') as fp:
#    soup = BeautifulSoup(fp,'html.parser')

url = "http://www.betpawa.co.ke/upcoming"
browser = webdriver.Chrome()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
games = soup.find_all("div",{"class":"block event"})
team1Names = []
team1Odds = []
teamDraw = []
team2Names = []
team2Odds =[]
for elem in games:
    for game in elem:
       y = game.find("div",{"class":"general-live-container first"}).find("h3").get_text()
       team1Names.append(y.split(" - ")[0])
       team2Names.append(y.split(" - ")[1])
       #bets are 3 and are all called 'event-bet
       eventBet = game.find_all('span',{"class":"event-bet"})
       team1Odds.append(eventBet[0].get_text()[1:])
       teamDraw.append(eventBet[1].get_text()[1:])
       team2Odds.append(eventBet[2].get_text()[1:])

teamTable = pd.DataFrame({
    "Team 1": team1Names,
    "| Team 1 odd": team1Odds,
    "| Match Draw": teamDraw,
    "| Team 2": team2Names,
    "| Team 2 Odd": team2Odds

})
teamTable = teamTable[['Team 1','| Team 1 odd','| Match Draw','| Team 2','| Team 2 Odd']]
pd.set_option('display.expand_frame_repr', False)
print("\t ================================ Bet-PaWa ==============================")
print(teamTable)
#teamTable.to_csv('betpawa.csv')