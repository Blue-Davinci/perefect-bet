import requests
import pandas as pd
from bs4 import BeautifulSoup
'''
class="team">Malmo</span>
                <span class="odd">1.45</span>
    </a>
    pick0X
'''
fileToRead = 'C:\\Users\\Blue_Davinci\\Downloads\\Sites\\Sportpesa __ Get in the Game.html'

with open(fileToRead,'rb') as fp:
    soup = BeautifulSoup(fp,'html.parser')

mainContents = soup.find_all('div',class_='col-xs-12 col-sm-7 col-md-7 col-lg-7 ng-scope')
events = soup.find('div',{'class':'bp-events upcomingmatches'})
exact = events.find_all('div',{'class':'match FOOTBALL - HIGHLIGHTS'})
odds = [[]]
counter = 0  # init counter to get current list
specifics = []
team1 = {}
draws = []
team2 = {}
for elem in exact:
    specifics.append(elem.find("ul", {"class": "bet-selector"}).find("li",{'class':'pick01'}).get_text().replace("\n"," "))
    #===================== First Team
    teamName = elem.find("ul", {"class": "bet-selector"}).find("li",{'class':'pick01'}).find("span",{"class":"team"}).get_text() #get odd
    teamOdd = elem.find("ul", {"class": "bet-selector"}).find("li",{'class':'pick01'}).find("span",{"class":"odd"}).get_text() #get odd
    team1[teamName] = teamOdd
    #====================== Draw
    draws.append(elem.find("ul", {"class": "bet-selector"}).find("li",{'class':'pick0X'}).find("span",{"class":"odd"}).get_text())
    #======================= 2nd Team
    teamName2 = elem.find("ul", {"class": "bet-selector"}).find("li",{'class':'pick02'}).find("span",{"class":"team"}).get_text() #get odd
    teamOdd2 = elem.find("ul", {"class": "bet-selector"}).find("li",{'class':'pick02'}).find("span",{"class":"odd"}).get_text() #get odd
    team2[teamName2] = teamOdd2

    counter +=1 #inc counter to get next item
    odds.append([]) #append a new list

jjjo = [x for x in team1.keys()]
jjjp = [x for x in team1.values()]
ttt = [x for x in team2.keys()]
ttty= [x for x in team2.values()]

weather = pd.DataFrame({
        "First Team": jjjo,
        "First Odd ": jjjp,
        "M.Draw": draws,
        "Team 2": ttt,
        "Team 2 Odd": ttty
    })

print("\t ================================ Sport Pesa ==============================")
print(weather)
weather.to_csv('sport.csv')