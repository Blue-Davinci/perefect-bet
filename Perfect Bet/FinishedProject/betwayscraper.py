import requests
from bs4 import BeautifulSoup
import pandas as pd


class BetWay_Scraper(object):
    def __init__(self):
        self.file = "C:\\Users\\user\\Downloads\\Sites\\Sports betting on Betway.co.ke _ Best online betting odds in Kenya.html"
        self.soup = ""
        self.read_file()
        self.team1Names = []
        self.team1Odds = []
        self.teamDraw = []
        self.team2Names = []
        self.team2Odds = []
        self.teamOddList = []
        self.uniCounter = 1  # reset to 1 in self
        self.games = self.soup.find_all("div", {"class": "fixture-holder"})

    def read_file(self):
        result = requests.get("https://www.betway.co.ke/")
        self.soup = BeautifulSoup(result.text, 'html.parser')

    def betway_scrape(self):
        print("=> Retrieving Bet_Way Results... ")
        for elem in self.games:
            x = elem.find_all("div", {"class": "inplayStatusDetails"})
            for team in x:
                y = team.find('b').get_text()
                self.team1Names.append(y.split(" v ")[0][3:])
                self.team2Names.append(y.split(" v ")[1])

            odds = elem.find_all("div", {"class": "outcomeBtnLong outcomebuttonDiv"})
            for od in odds:
                self.teamOddList.append(od.find("div", {"class": "outcome-pricedecimal "}).get_text())
            # match odds
            for teamodd in self.teamOddList:
                if self.uniCounter % 2 == 0:
                    self.team1Odds.append(teamodd)
                else:
                    self.team2Odds.append(teamodd)
                self.uniCounter += 1
            draws = elem.find_all("div", {"class": "outcomeBtnShort outcomebuttonDiv"})
            for draw in draws:
                self.teamDraw.append(draw.find("div", {"class": "outcome-pricedecimal drawPriceDecimal"}).get_text())
        print("=> Bet_Way Results Retrieval Complete. ")

    def betway_dataframe(self):
        self.betway_scrape()
        teamTable = pd.DataFrame({
            "Team1": self.team1Names,
            "Team1odd": self.team1Odds,
            "MatchDraw": self.teamDraw,
            "Team2": self.team2Names,
            "Team2Odd": self.team2Odds

        })
        teamTable = teamTable[['Team1', 'Team1odd', 'MatchDraw', 'Team2', 'Team2Odd']]
        pd.set_option('display.expand_frame_repr', False)
        #print("\t ================================ Bet-Way ==============================")
        #print(teamTable)
        return teamTable

    def place_holder(self):
        print("Please Access This Via Main Program")
        pass

if __name__ == "__main__":
    place_holder = BetWay_Scraper()
    place_holder.betway_dataframe()


