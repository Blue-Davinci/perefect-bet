import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

file = "C:\\Users\\Blue_Davinci\\Downloads\\Sites\\Dafabet1.html"

url = "https://dafabet.co.ke/sports-african/foot"
browser = webdriver.Chrome()
browser.get(url)
html = browser.page_source

req = requests.get("https://dafabet.co.ke/sports-african/foot")
soup = BeautifulSoup(html,'html.parser')

games = soup.find_all("div",{"class":"panel-main"})
team1Names = []
team1Odds = []
teamDraw = []
team2Names = []
team2Odds =[]

def check_viability(x):
    try:
        z = x[0]
        return True
    except:
        print(" =============   ERRRORRR   ========================")
        return False
for elem in games:
    firstelem = elem.find_all("div",{"class":"event-row "})
    for secelem in firstelem:
        team1Names.append(secelem.find("div",{"class":"event-description"}).get_text().splitlines()[3])
        team2Names.append(secelem.find("div", {"class": "event-description"}).get_text().splitlines()[4])
        if check_viability(secelem.find("div",{"class":"period period-1X2 periods-5 outcome-3 outcomelength-13 "}).
                               find_all("div",{"class":"price-container"})):
            team1Odds.append(
                float(secelem.find("div", {"class": "period period-1X2 periods-5 outcome-3 outcomelength-13 "}).
                      find_all("div", {"class": "price-container"})[0].find("span", {
                    "class": "outcome-price"}).get_text().strip()))

            teamDraw.append(
                float(secelem.find("div", {"class": "period period-1X2 periods-5 outcome-3 outcomelength-13 "}).
                      find_all("div", {"class": "price-container"})[1].
                      find("span", {"class": "outcome-price"}).get_text().strip()))
            team2Odds.append(
                float(secelem.find("div", {"class": "period period-1X2 periods-5 outcome-3 outcomelength-13 "}).
                      find_all("div", {"class": "price-container"})[2].
                      find("span", {"class": "outcome-price"}).get_text().strip()))
        else:
            team1Odds.append(0)
            teamDraw.append(0)
            team2Odds.append(0)



#print(team1Names)
#print(team2Names)

teamTable = pd.DataFrame({
    "Team 1": team1Names,
    "| Team 1 odd": team1Odds,
    "| Match Draw": teamDraw,
    "| Team 2": team2Names,
    "| Team 2 Odd": team2Odds

})
teamTable = teamTable[['Team 1', '| Team 1 odd', '| Match Draw', '| Team 2', '| Team 2 Odd']]
pd.set_option('display.expand_frame_repr', False)  # display full width
pd.set_option('display.max_rows',500)  # display full height
print("\t ================================ Dafa Bet ==============================")
print(teamTable)
