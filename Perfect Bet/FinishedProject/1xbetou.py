import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

file = "C:\\Users\\user\\Downloads\\Sites\\Fixed-odds sports betting _ 1XBET.COM Betting Company.html"

class OneBet_Scraper(object):
    def __init__(self):
        self.fileToRead = 'C:\\Users\\Blue_Davinci\\Downloads\\Sites\\Sportpesa __ Get in the Game.html'
        self.specifics = []
        self.team1 = {}
        self.draws = []
        self.team2 = {}
        self.soup = self.read_file()
        self.odds = [[]]
        self.mainContents = self.soup.find_all('div', class_='col-xs-12 col-sm-7 col-md-7 col-lg-7 ng-scope')
        self.events = self.soup.find_all('div', {'class': 'bp-events upcomingmatches'})

    def read_file(self):
        url = "C:\\Users\\user\\Downloads\\Sites\\S1XBET - Bets & Betting tips ᐉ Online sports betting odds ᐉ 1xbet.co.ke"
            #"https://www.sportpesa.com/?sportId=1"
        browser = webdriver.Chrome()
        browser.get(url)
        while True:
            try:
                element_present = EC.presence_of_element_located((By.ID, 'nav-content'))
                WebDriverWait(browser, 5).until(element_present)
                break
            except TimeoutException:
                print("!=> Failed To Get The Results For Sport-Pesa. Please Wait While We Re-Try.")

        html = browser.page_source
        browser.quit()
        return BeautifulSoup(html, 'html.parser')


with open(file,'rb') as fp:
    soup = BeautifulSoup(fp,'html.parser')

first_table = soup.find_all("div",{"storagename":"live_main"})
second_table = soup.find_all("div",{"storagename":"line_main"})
main_table = soup.find("div",{"class":"SSR"})
team_list = main_table.find_all("li",{"class":"c-events__item c-events__item_col"})
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
        the_team = teams.find("span",{"class":"c-events__teams"})
        the_odds = teams.find_all("div",{"class":"c-bets__item"})
        team_name = the_team.find_all("span",{"class":"c-events__team"})
        #team1Names.append(team_name[0].get_text())
        #team2Names.append(team_name[1].get_text())
        for x in the_odds[2]:
            try:
                y = x.find_all(("a", {"class": "c-bets__bet  "}))
            except:
                continue
            for z in y:
                print(z[0].get_text())
            #ou_odds = x.find_all("a", {"class": "c-bets__bet  "})
            #over = ou_odds[0].get_text()
            #under = ou_odds[1].get_text()
            print(x)
            print("\n \n ==================== \n \n")

get_1x_bet(team_list)
#get_1x_bet(second_table)
print(team1Names)
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
