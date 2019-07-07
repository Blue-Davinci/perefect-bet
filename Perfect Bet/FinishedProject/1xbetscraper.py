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
        self.second_table = self.soup.find_all("div", {"storagename": "line"})
        self.team1Names = []
        self.team1Odds = []
        self.teamDraw = []
        self.team2Names = []
        self.team2Odds = []

    def read_file(self):
        url = "https://1xbet.co.ke/en/line/Football/"
        browser = webdriver.Chrome()
        browser.get(url)
        html = browser.page_source
        browser.quit()
        return BeautifulSoup(html, 'html.parser')

    def onescraper(self,table):
        print("=> Retrieving 1xBet Results... ")
        for teams in table:
            team = teams.find_all("li", {"class": "c-events__item c-events__item_col"})
            print(team.get_text())

        print("=> 1xBet Retrieval Complete... ")

    def one_dataframe(self):
        self.onescraper(self.second_table)
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