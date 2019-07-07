from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class Dafabet_Scraper(object):
    def __init__(self):
        self.file = "C:\\Users\\Blue_Davinci\\Downloads\\Sites\\Dafabet.html"
        self.soup = ""
        self.read_file()
        self.team1Names = []
        self.team1Odds = []
        self.teamDraw = []
        self.team2Names = []
        self.team2Odds = []
        self.team1ouOdds = []
        self.team2ouOdds = []
        self.games = self.soup.find_all("div", {"class": "league-container"})

    def read_file(self):
        url = "https://dafabet.co.ke/sports-african/foot"
        browser = webdriver.Chrome()
        browser.get(url)
        while True:
            try:
                element_present = EC.presence_of_element_located((By.CLASS_NAME, 'loading'))
                WebDriverWait(browser, 5).until(element_present)
            except TimeoutException:
                break
        html = browser.page_source
        browser.quit()
        self.soup = BeautifulSoup(html, 'html.parser')
        #result = requests.get("https://dafabet.co.ke/sports-african/foot")

    def check_viability(self,score):
        try:
            testodd = score[0]
            return True
        except:
            print("!=> [Dafa_Bet] No Odds Found For This Team!")
            return False


    def dafabet_scrape(self):
        print("=> Retrieving Dafa_Bet Results... ")
        for elem in self.games:
            firstelem = elem.find_all("div", {"class": "event-row "})
            for secelem in firstelem:
                self.team1Names.append(secelem.find("div", {"class": "event-description"}).get_text().splitlines()[3])
                self.team2Names.append(secelem.find("div", {"class": "event-description"}).get_text().splitlines()[4])
                if self.check_viability(secelem.find("div",{"class":"period period-1X2 periods-5 outcome-3 outcomelength-13 "}).
                               find_all("div",{"class":"price-container"})):
                    self.team1Odds.append(
                        float(secelem.find("div", {"class": "period period-1X2 periods-5 outcome-3 outcomelength-13 "}).
                              find_all("div", {"class": "price-container"})[0].
                              find("span", {"class": "outcome-price"}).get_text().strip()))
                    self.teamDraw.append(
                        float(secelem.find("div", {"class": "period period-1X2 periods-5 outcome-3 outcomelength-13 "}).
                              find_all("div", {"class": "price-container"})[1].
                              find("span", {"class": "outcome-price"}).get_text().strip()))
                    self.team2Odds.append(
                        float(secelem.find("div", {"class": "period period-1X2 periods-5 outcome-3 outcomelength-13 "}).
                              find_all("div", {"class": "price-container"})[2].
                              find("span", {"class": "outcome-price"}).get_text().strip()))
                else:
                    self.team1Odds.append(0)
                    self.teamDraw.append(0)
                    self.team2Odds.append(0)


        print("=> Dafa_Bet Result Retrieval Complete. ")

    def dafabet_ou_scraper(self):
        print("=> Retrieving Dafa_Bet [OU] Results... ")
        for elem in self.games:
            firstelem = elem.find_all("div", {"class": "event-row "})
            for secelem in firstelem:
                self.team1Names.append(secelem.find("div", {"class": "event-description"}).get_text().splitlines()[3])
                self.team2Names.append(secelem.find("div", {"class": "event-description"}).get_text().splitlines()[4])
                if self.check_viability(secelem.find("div",{"class":"period period-OU periods-5 outcome-3 outcomelength-13 "}).
                               find_all("div",{"class":"price-container"})):
                    self.team1ouOdds.append(
                        float(secelem.find("div", {"class": "period period-OU periods-5 outcome-3 outcomelength-13 "}).
                              find_all("div", {"class": "price-container"})[0].
                              find("span", {"class": "outcome-price"}).get_text().strip()))
                    self.team2ouOdds.append(
                        float(secelem.find("div", {"class": "period period-OU periods-5 outcome-3 outcomelength-13 "}).
                              find_all("div", {"class": "price-container"})[1].
                              find("span", {"class": "outcome-price"}).get_text().strip()))
                else:
                    self.team1ouOdds.append(0)
                    self.team2ouOdds.append(0)


        print("=> Dafa_Bet [OU] Results Retrieval Complete. ")

    def dafabet_dataframe(self):
        self.dafabet_scrape()
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
       # print("\t ================================ Dafa Bet ==============================")
       # print(teamTable)
        return teamTable

    def dafabet_ou_dataframe(self):
        self.dafabet_ou_scraper()
        teamTable = pd.DataFrame({
            "Team1": self.team1Names,
            "Over": self.team1ouOdds,
            "Team2": self.team2Names,
            "Under": self.team2ouOdds

        })
        teamTable = teamTable[['Team1', 'Over', 'Team2', 'Under']]
        pd.set_option('display.expand_frame_repr', False)  # display full width
        pd.set_option('display.max_rows', 500)  # display full height
        # print("\t ================================ Dafa Bet ==============================")
        # print(teamTable)
        return teamTable

    def place_holder(self):
        print("Please Access This Via Main Program")
        pass

if __name__ == "__main__":
    place_holder = Dafabet_Scraper()
    xy = place_holder.dafabet_ou_dataframe()
    xy.to_csv('mcheza_ou.csv', encoding="ISO-8859-1")
    print(xy)



