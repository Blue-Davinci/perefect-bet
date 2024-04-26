import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class SportPesa(object):

    def __init__(self):
        self.fileToRead = 'C:\\Users\\user\\Downloads\\Sites\\Sportpesa __ Get in the Game.html'
        self.specifics = []
        self.team1 = {}
        self.draws = []
        self.team2 = {}
        self.soup = self.read_file()
        self.odds = [[]]
        self.mainContents = self.soup.find_all('div', class_='col-xs-12 col-sm-7 col-md-7 col-lg-7 ng-scope')
        self.events = self.soup.find_all('div', {'class': 'bp-events upcomingmatches'})

    def read_file(self):
        url = "C:\\Users\\Blue_Davinci\\Downloads\\Sites\\Sportpesa __ Get in the Game.html"
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

    def sp_scrape(self):
        print("=> Retrieving SportPesa Results... ")
        for elem in self.events:
            for matches in elem:
                try:
                    self.specifics.append(
                        matches.find("ul", {"class": "bet-selector"}).find("li",
                                                                           {'class': 'pick01'}).get_text().replace("\n",
                                                                                                                   " "))
                    # ===================== First Team
                    self.teamName = matches.find("ul", {"class": "bet-selector"}).find("li", {'class': 'pick01'}).find(
                        "span",
                        {
                            "class": "team"}).get_text()  # get odd
                    self.teamOdd = matches.find("ul", {"class": "bet-selector"}).find("li", {'class': 'pick01'}).find(
                        "span", {
                            "class": "odd"}).get_text()  # get odd
                    self.team1[self.teamName] = self.teamOdd
                    # ====================== Draw
                    self.draws.append(
                        matches.find("ul", {"class": "bet-selector"}).find("li", {'class': 'pick0X'}).find("span", {
                            "class": "odd"}).get_text())
                    # ======================= 2nd Team
                    self.teamName2 = matches.find("ul", {"class": "bet-selector"}).find("li", {'class': 'pick02'}).find(
                        "span",
                        {
                            "class": "team"}).get_text()  # get odd
                    self.teamOdd2 = matches.find("ul", {"class": "bet-selector"}).find("li", {'class': 'pick02'}).find(
                        "span",
                        {
                            "class": "odd"}).get_text()  # get odd
                    self.team2[self.teamName2] = self.teamOdd2
                    self.odds.append([])  # append a new list
                except:
                    continue
        print("=> SportPesa Result Retrieval Complete. ")

    def sp_dataframe(self):
        self.sp_scrape()
        firstteams = [x for x in self.team1.keys()]
        firstteamodds = [x for x in self.team1.values()]
        secondteams = [x for x in self.team2.keys()]
        secondteamodds = [x for x in self.team2.values()]

       # print(len(firstteamodds)," == ", firstteamodds)
        #print(len(firstteams), " == ", firstteams)
        #print(len(secondteams), " == ", secondteams)
        #print(len(secondteamodds), " == ", secondteamodds)


        weather = pd.DataFrame({
            "Team1": firstteams,
            "Team1odd": firstteamodds,
            "MatchDraw": self.draws,
            "Team2": secondteams,
            "Team2Odd": secondteamodds
        })

            #print("\t ================================ Sport Pesa ==============================")
        #print(weather)
        return weather

    def place_holder(self):
        print("Please Access This Via Main Program")
        pass


if __name__ == "__main__":
    place_holder = SportPesa()
    place_holder.sp_dataframe()

