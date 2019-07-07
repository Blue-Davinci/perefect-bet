import pandas as pd

frame = pd.DataFrame({'Name':['manu','chelsea','liverpool'],'Odd':[1.18,2.4,3.5],'secname':['Sunderland','WestHam','Gond'],
                     'secodd':[2,3,4]})
frame2 = pd.DataFrame({'Name':['manu','chelsea','liverpool'],'Odd':[1.10,2.3,3.2],'secname':['Sunderland','WestHam','Gond'],
                     'secodd':[7.0,3.3,4.5]})
if frame2.Name.str.contains("manu").any():
    #frame['Name'].values[0]
    print(frame)
    #print(frame['Name'].values[0])
    #print(frame.loc[frame['Name']=='manu','Odd'])
mylist = []
for team in frame['Name']:
    teamodd = float(frame.loc[frame['Name']==team,'Odd'])
    teamsec = frame.loc[frame['Name']==team,'secname']
    if frame2.Name.str.contains(team).any():
        secondteamodd = float(frame2.loc[frame['Name']==team,'secodd'])
        print(secondteamodd)
        total = (1/teamodd * 100) + (1/secondteamodd * 100)
        if total < 100:
            #print("===============")
            #print(frame2[frame2['Name'] == team]['secname'].values)
            #frame2.loc[frame2['Name']==team,'secname']
            print("===============")
            xx =frame2[frame2['Name'] == team]['secname'].values[0]
            mylist.append([team + " vs " + xx + " | Total: " + str(total)])

print(mylist)

