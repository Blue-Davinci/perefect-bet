from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Betpawa_Scraper(object):

    def __init__(self):
        self.file = "C:\\Users\\user\\Downloads\\Sites\\Upcoming betting events Betpawa.html"
        self.soup = ""
        self.read_file()
        self.team1Names = []
        self.team1Odds = []
        self.teamDraw = []
        self.team2Names = []
        self.team2Odds = []
        self.games = self.soup.find_all("div", {"class": "block event"})

    def read_file(self):
        #http://www.betpawa.co.ke/upcoming
        url = "http://www.betpawa.co.ke/upcoming"
        browser = webdriver.Chrome()
        browser.get(url)
        while True:
            try:
                element_present = EC.presence_of_element_located((By.CLASS_NAME, 'events-wrapper'))
                WebDriverWait(browser, 5).until(element_present)
                break
            except TimeoutException:
                print("!=> Failed To Get The Results For BetPawa. Please Wait While We Re-Try.")
        html = browser.page_source
        browser.quit()
        self.soup = BeautifulSoup(html, 'html.parser')

    def betpawa_scrape(self):
        print("=> Retrieving Bet_Pawa Results... ")
        for elem in self.games:
            for game in elem:
                y = game.find("div", {"class": "general-live-container first"}).find("h3").get_text()
                self.team1Names.append(y.split(" - ")[0])
                self.team2Names.append(y.split(" - ")[1])
                # bets are 3 and are all called 'event-bet
                eventBet = game.find_all('span', {"class": "event-bet"})
                self.team1Odds.append(eventBet[0].get_text()[1:])
                self.teamDraw.append(eventBet[1].get_text()[1:])
                self.team2Odds.append(eventBet[2].get_text()[1:])

        print(self.team2odds)
        print("=> Bet_Pawa Results Retrieval Complete. ")

    def betpawa_dataframe(self):
        self.betpawa_scrape()
        teamTable = pd.DataFrame({
            "Team1": self.team1Names,
            "Team1odd": self.team1Odds,
            "MatchDraw": self.teamDraw,
            "Team2": self.team2Names,
            "Team2Odd": self.team2Odds

        })
        teamTable = teamTable[['Team1', 'Team1odd', 'MatchDraw', 'Team2', 'Team2Odd']]
        pd.set_option('display.expand_frame_repr', False)
        #print("\t ================================ Bet-PaWa ==============================")
        #print(teamTable)
        return teamTable

    def place_holder(self):
        print("Please Access This Via Main Program")
        pass

if __name__ == "__main__":
    place_holder = Betpawa_Scraper()
    place_holder.betpawa_dataframe()

