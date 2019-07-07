from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class Mcheza_Scraper(object):
    def __init__(self):
        self.file = "C:\\Users\\Blue_Davinci\\Downloads\\Sites\\mCHEZA1.html"
        self.soup = ""
        self.read_file()
        self.team1Names = []
        self.team1Odds = []
        self.team1ouOdds = []
        self.teamDraw = []
        self.team2Names = []
        self.team2Odds = []
        self.team2ouOdds = []
        self.games = self.soup.find_all("div",{"class":"matches-set"})
        self.pop = self.soup.find_all("div",{"class":"match-section-sport-content"})

    def read_file(self):
        #https://www.mcheza.co.ke/sports
        url = "https://www.mcheza.co.ke/sports"
        browser = webdriver.Chrome()
        browser.get(url)
        #time.sleep(15)
        while True:
            try:
                element_present = EC.presence_of_element_located((By.CLASS_NAME, 'featured-matches'))
                WebDriverWait(browser, 5).until(element_present)
                break
            except TimeoutException:
                print("!=> Failed To Get The Results For Mcheza. Please Wait While We Re-Try.")
        html = browser.page_source
        browser.quit()
        self.soup = BeautifulSoup(html, 'html.parser')

    def mcheza_scrape(self,table):
        print("=> Retrieving M_Cheza Results... ")
        for elem in table:
            y = elem.find("div", {"class": "match-teams"}).get_text()
            if y != None:
                self.team1Names.append(y.split(" v ")[0])
                self.team2Names.append(y.split(" v ")[1])
            try:
                draw = elem.find("div", {"class": "selection-button selection-button-X"}).get_text()
                if draw != None:
                    self.teamDraw.append(draw.replace("X", ""))
            except:
                self.teamDraw.append('0')

            try:
                odd1 = elem.find("div", {"class": "selection-button selection-button-1"}).find("div", {
                    "class": "sel-odds"}).get_text()
                if odd1 != None:
                    self.team1Odds.append(odd1)
            except:
                self.team1Odds.append('0')

            try:
                odd2 = elem.find("div", {"class": "selection-button selection-button-2"}).get_text()
                if odd2 != None:
                    self.team2Odds.append(odd2[1:])
            except:
                self.team2Odds.append('0')

        print("=> M_Cheza Results Retrieval Complete.")

    def mcheza_ou_scraper(self,table):
        print("=> Retrieving M_Cheza [OU] Results... ")
        for elem in table:
            y = elem.find("div", {"class": "match-teams"}).get_text()
            if y != None:
                self.team1Names.append(y.split(" v ")[0])
                self.team2Names.append(y.split(" v ")[1])

            try:
                odd1 = elem.find("div", {"class": "selection-button selection-button-Over"}).find("div", {
                    "class": "sel-odds"}).get_text()
                if odd1 != None:
                    self.team1ouOdds.append(odd1)
            except:
                self.team1ouOdds.append('0')

            try:
                odd2 = elem.find("div", {"class": "selection-button selection-button-Under"}).find("div", {
                    "class": "sel-odds"}).get_text()
                if odd2 != None:
                    self.team2ouOdds.append(odd2)
            except:
                self.team2ouOdds.append('0')

        print("=> M_Cheza [OU] Results Retrieval Complete.")

    def mcheza_dataframe(self):
        self.mcheza_scrape(self.games[0])
        self.mcheza_scrape(self.games[1])
        teamTable = pd.DataFrame({
            "Team1": self.team1Names,
            "Team1odd": self.team1Odds,
            "MatchDraw": self.teamDraw,
            "Team2": self.team2Names,
            "Team2Odd": self.team2Odds
        })
        teamTable = teamTable[['Team1', 'Team1odd', 'MatchDraw', 'Team2', 'Team2Odd']]
        pd.set_option('display.expand_frame_repr', False)
        #print("\t ================================ M-Cheza ==============================")
        #print(teamTable)
        return teamTable

    def mcheza_ou_dataframe(self):
        self.mcheza_ou_scraper(self.games[0])
        self.mcheza_ou_scraper(self.games[1])
        teamTable = pd.DataFrame({
            "Team1": self.team1Names,
            "Over": self.team1ouOdds,
            "Team2": self.team2Names,
            "Under": self.team2ouOdds
        })
        teamTable = teamTable[['Team1', 'Over', 'Team2', 'Under']]
        pd.set_option('display.expand_frame_repr', False)
        # print("\t ================================ M-Cheza ==============================")
        #print(teamTable)
        return teamTable
    
    def place_holder(self):
        print("Please Access This Via Main Program")
        pass

if __name__ == "__main__":
    place_holder = Mcheza_Scraper()
    place_holder.mcheza_ou_dataframe()