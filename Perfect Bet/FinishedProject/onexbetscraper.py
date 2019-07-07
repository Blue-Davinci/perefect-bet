from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class onexbet(object):

    def __init__(self):
        self.file = "C:\\Users\\Blue_Davinci\\Downloads\\Sites\\1XBET.COM Betting Company. Online sports betting _ 1XBET.COM Betting Company.html"
        self.soup = self.read_file()
        self.first_table = self.soup.find_all("div", {"storagename": "live_main"})
        self.second_table = self.soup.find_all("div", {"storagename": "line_main"})
        self.team1Names = []
        self.team1Odds = []
        self.teamDraw = []
        self.team2Names = []
        self.team2Odds = []


    def read_file(self):
        url = "1xbet.co.ke"
        browser = webdriver.Chrome()
        browser.get(url)
        html = browser.page_source
        browser.quit()
        return BeautifulSoup(html, 'html.parser')

    def onescraper(self,table):
        print("=> Retrieving 1xBet Results... ")
        for teams in table:
            container_element = teams.find_all("div", {"class": "c-events__item"})
            for t in container_element:
                team = t.find("span", {"class": "c-events__teams"}).get_text().split("   ")
                self.team1Names.append(team[0])
                self.team2Names.append(team[1])
                teamodds = t.find_all("div", {"class": "c-bets__item"})
                counter = 1
                for x in teamodds[0]:
                    theodd = x.get_text()
                    if counter == 1:
                        self.team1Odds.append(theodd)
                    elif counter == 2:
                        self.teamDraw.append(theodd)
                    elif counter == 3:
                        self.team2Odds.append(theodd)
                    counter += 1

                counter = 1
        print("=> 1xBet Retrieval Complete... ")

    def one_dataframe(self):
        teamTable = pd.DataFrame({
            "Team1": self.team1Names,
            "Team1odd": self.team1Odds,
            "MatchDraw": self.teamDraw,
            "Team2": self.team2Names,
            "Team2Odd": self.team2Odds

        })
        teamTable = teamTable[['Team1', 'Team1odd', 'MatchDraw', 'Team2', 'Team2Odd']]
        pd.set_option('display.expand_frame_repr', False)  # display full width
        pd.set_option('display.max_rows', 500)  # display full height
        return teamTable

    def place_holder(self):
        print("Please Access This Via Main Program")
        pass


if __name__ == "__main__":
    place_holder = onexbet()
    place_holder.one_dataframe()