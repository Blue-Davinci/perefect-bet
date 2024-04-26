import requests
from bs4 import BeautifulSoup
import pandas as pd


class Betika_Scraper(object):
    def __init__(self):
        self.file = "C:\\Users\\user\\Downloads\\Sites\\Betika - The #1 Online & SMS sports Betting Website In Kenya.html"
        self.soup = ""
        self.read_file()
        self.team1pack = []
        self.team1oddpack = []
        self.drawpack = []
        self.team2pack = []
        self.team2oddpack = []
        self.betikaResults = self.soup.find_all("div", {"class": "matches full-width"})
        self.xx = self.soup.find_all("div", {"class": "col-sm-12 top-matches"})

    def read_file(self):
        result = requests.get("https://www.betika.com/upcoming")
        self.soup = BeautifulSoup(result.text, 'html.parser')

    def betika_scrape(self):
        print("=> Retrieving Betika Results... ")
        for elem in self.xx:
            counter = 1
            counter2 = 1
            team1name = elem.find("span", {"class": "theteam col-sm-9"})

            # Get All Odds
            team1odd = elem.find_all("span", {"class": "theodds col-sm-3"})
            for i in team1odd:
                if counter2 % 2 == 0 and i != None:
                    self.team2oddpack.append(i.get_text())
                else:
                    self.team1oddpack.append(i.get_text())
                counter2 += 1

            # Get All Draws
            teamdraw = elem.find("span", {"class": "label label-inverse"})
            if teamdraw != None:
                self.drawpack.append(teamdraw.get_text())

            # Get All Team Names
            team2name = elem.find_all("span", {"class": "theteam col-sm-9"})
            for i in team2name:
                if counter % 2 == 0 and i != None:
                    self.team2pack.append(i.get_text())
                else:
                    self.team1pack.append(i.get_text())
                counter += 1
        print("=> Betika Results Retrieval Complete. ")

    def betika_dataframe(self):
        self.betika_scrape()
        betikaTable = pd.DataFrame({
            "Team1": self.team1pack,
            "Team1odd": self.team1oddpack,
            "MatchDraw": self.drawpack,
            "Team2": self.team2pack,
            "Team2Odd": self.team2oddpack
        })
        pd.set_option('display.expand_frame_repr', False)
        #print(betikaTable)
        #print("\t => Betika Results Succesfully Loaded...")
        return betikaTable

    def place_holder(self):
        print("Please Access This Via Main Program")
        pass


if __name__ == "__main__":
    place_holder = Betika_Scraper()
    place_holder.betika_dataframe()

