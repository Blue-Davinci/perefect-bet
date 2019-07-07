import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
file = "C:\\Users\\Blue_Davinci\\Downloads\\Sites\\1XBET.COM Betting Company. Online sports betting _ 1XBET.COM Betting Company.html"

with open(file,'rb') as fp:
    soup = BeautifulSoup(fp,'html.parser')

first_table = soup.find_all("div",{"storagename":"live_main"})
second_table = soup.find_all("div",{"storagename":"line_main"})
team1Names = []
team1Odds = []
teamDraw = []
team2Names = []
team2Odds =[]
#driver = webdriver.Chrome()
#driver.get(file)
#select = driver.find_element_by_id('countLiveEventsOnMain')
#select.click()
#select.select_by_visible_text('TOP 50')

def get_1x_bet(table):
    for teams in table:
        container_element = teams.find_all("div",{"class":"c-events__item"})
        for t in container_element:
            team = t.find("span", {"class": "c-events__teams"}).get_text().split("   ")
            team1Names.append(team[0])
            team2Names.append(team[1])
            teamodds = t.find_all("div",{"class":"c-bets__item"})
            counter = 1
            for x in teamodds[0]:
                theodd = x.get_text()
                if counter == 1:
                    team1Odds.append(theodd)
                elif counter == 2:
                    teamDraw.append(theodd)
                elif counter == 3:
                    team2Odds.append(theodd)
                counter +=1

            counter = 1

get_1x_bet(first_table)
get_1x_bet(second_table)
teamTable = pd.DataFrame({
    "Team1": team1Names,
    "Team1odd": team1Odds,
    "MatchDraw": teamDraw,
    "Team2": team2Names,
    "Team2Odd": team2Odds

})
teamTable = teamTable[['Team1', 'Team1odd', 'MatchDraw', 'Team2', 'Team2Odd']]
pd.set_option('display.expand_frame_repr', False)  # display full width
pd.set_option('display.max_rows', 500)  # display full height
print("\t ================================ Dafa Bet ==============================")
print(teamTable)
