import requests
from bs4 import BeautifulSoup
import pandas as pd

'''
<button class="422866 422866101" hometeam="Shimizu S-Pulse" oddtype="3 Way" bettype="prematch" awayteam="Urawa Red Diamonds" oddvalue="4.04" 
target="javascript:;" odd-key="1" parentmatchid="11879720" id="422866" custom="422866101" value="10" special-value-value="0" 
onclick="addBet(this.id,this.value,this.getAttribute('odd-key'),this.getAttribute('custom'),this.getAttribute('special-value-value'),
this.getAttribute('bettype'),this.getAttribute('hometeam'),this.getAttribute('awayteam'),
this.getAttribute('oddvalue'),this.getAttribute('oddtype'),this.getAttribute('parentmatchid'))">

<span class="theteam col-sm-9">Shimizu S-Pulse <span class="compt"></span></span> <span class="theodds col-sm-3">4.04</span></button>


<button class="422866 422866102" hometeam="Shimizu S-Pulse" oddtype="3 Way" bettype="prematch" awayteam="Urawa Red Diamonds" oddvalue="1.84" 
value="10" custom="422866102" odd-key="2" target="javascript:;" parentmatchid="11879720" id="422866" special-value-value="0" 
onclick="addBet(this.id,this.value,this.getAttribute('odd-key'),this.getAttribute('custom'),this.getAttribute('special-value-value'),
this.getAttribute('bettype'),this.getAttribute('hometeam'),this.getAttribute('awayteam'),this.getAttribute('oddvalue'),
this.getAttribute('oddtype'),this.getAttribute('parentmatchid'))">

<span class="theteam col-sm-9"> Urawa Red Diamonds<span class="compt"> </span></span><span class="theodds col-sm-3"> 1.84 </span></button>

'''


file = "C:\\Users\\Blue_Davinci\\Downloads\\Sites\\Betika - The #1 Online & SMS sports Betting Website In Kenya.html"

with open(file,'rb') as fp:
    soup = BeautifulSoup(fp,'html.parser')

betikaResults = soup.find_all("div",{"class":"matches full-width"})
xx= soup.find_all("div", {"class": "col-sm-12 top-matches"})
team1pack = []
team1oddpack = []
drawpack = []
team2pack = []
team2oddpack = []
for elem in xx:
    counter = 1
    counter2 = 1
    team1name = elem.find("span",{"class":"theteam col-sm-9"})

    #Get All Odds
    team1odd = elem.find_all("span",{"class":"theodds col-sm-3"})
    for i in team1odd:
        if counter2%2 == 0 and i !=None:
            team2oddpack.append(i.get_text())
        else:
            team1oddpack.append(i.get_text())
        counter2 +=1

    #Get All Draws
    teamdraw = elem.find("span",{"class":"label label-inverse"})
    if teamdraw != None:
        drawpack.append(teamdraw.get_text())


    #Get All Team Names
    team2name = elem.find_all("span",{"class":"theteam col-sm-9"})
    for i in team2name:
        if counter%2 == 0 and i != None:
            team2pack.append(i.get_text())
        else:
            team1pack.append(i.get_text())
        counter +=1


betikaTable = pd.DataFrame({
        "T1": team1pack,
        "T1 odd": team1oddpack,
        "M.Draw": drawpack,
        "T2": team2pack,
        "T2 Odd": team2oddpack
})
pd.set_option('display.expand_frame_repr', False)
print("\t ================================ Betika ==============================")
print(betikaTable)
#betikaTable.to_csv('xnk.csv')
#xpo = pd.read_csv("xnk.csv")
#print(xpo)
