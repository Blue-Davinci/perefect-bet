import pandas as pd


class Algo(object):

    def __init__(self):
        self.betika = pd.read_csv("betikatable.csv", encoding="ISO-8859-1")
        self.betika['Team1odd'] = self.betika['Team1odd'].astype(float).fillna(0.0)
        self.betika['Team2Odd'] = self.betika['Team2Odd'].astype(float).fillna(0.0)
        self.betpawa = pd.read_csv("betpawa.csv", encoding="ISO-8859-1")
        self.betpawa['Team1odd'] = self.betpawa['Team1odd'].astype(float).fillna(0.0)
        self.betpawa['Team2Odd'] = self.betpawa['Team2Odd'].astype(float).fillna(0.0)
        self.betway = pd.read_csv("betway.csv", encoding="ISO-8859-1")
        self.betway['Team1odd'] = self.betway['Team1odd'].astype(float).fillna(0.0)
        self.betway['Team2Odd'] = self.betway['Team2Odd'].astype(float).fillna(0.0)
        self.sportpesa = pd.read_csv("sp.csv", encoding="ISO-8859-1")
        self.sportpesa['Team1odd'] = self.sportpesa['Team1odd'].astype(float).fillna(0.0)
        self.sportpesa['Team2Odd'] = self.sportpesa['Team2Odd'].astype(float).fillna(0.0)
        self.mcheza = pd.read_csv("mcheza.csv", encoding="ISO-8859-1")
        self.mcheza['Team1odd'] = self.mcheza['Team1odd'].astype(float).fillna(0.0)
        self.mcheza['Team2Odd'] = self.mcheza['Team2Odd'].astype(float).fillna(0.0)
        self.dafabet = pd.read_csv("dafabet.csv", encoding="ISO-8859-1")
        self.dafabet['Team1odd'] = self.dafabet['Team1odd'].astype(float).fillna(0.0)
        self.dafabet['Team2Odd'] = self.dafabet['Team2Odd'].astype(float).fillna(0.0)
        #self.onexbet = pd.read_csv("onexbet.csv", encoding="ISO-8859-1")
        #self.onexbet['Team1odd'] = self.onexbet['Team1odd'].astype(float).fillna(0.0)
        #self.onexbet['Team2Odd'] = self.onexbet['Team2Odd'].astype(float).fillna(0.0)

    def algo_check(self):
        result_tables = {'Betika Results': self.betika, 'Sportpesa Results': self.sportpesa, 'Betway Results': self.betway,
                         'Betpawa Results': self.betpawa, 'Mcheza Results': self.mcheza, 'Dafabaet Results': self.dafabet}
        perfect_bets = []
        web_sites = {}
        for key, table in result_tables.items():  # get each table in our dictionary
            if not table.empty:  # if the table is not empty
                for teams in table['Team1']:  # get each team in our current table
                    first_team_odd = table.loc[table['Team1'] == teams, 'MatchDraw']  # get the team's odd
                    #first_team_draw = table.loc[table['MatchDraw'] == teams, 'MatchDraw']
                    for seckey, other_tables in result_tables.items():  # get other tables for comparisons
                        if seckey != key:  # if this is not our current table
                            if not other_tables.empty:  # table is not empty
                                for other_teams in other_tables['Team1']:
                                    if other_teams == teams:
                                        second_team_name = \
                                            other_tables[other_tables['Team1'] == other_teams]['Team2'].values[0]
                                        second_team_odd = float(
                                            other_tables[other_tables['Team1'] == other_teams]['Team2Odd'].
                                                values[0])  # get the team's odd
                                        ###############################################################################
                                        for thirkey, th_tables in result_tables.items():  # get other tables for comparisons
                                            if thirkey != key and thirkey != seckey:  # if this is not our current table
                                                if not th_tables.empty:  # table is not empty
                                                    for th_teams in th_tables['Team1']:
                                                        if str(th_teams).strip() == str(teams).strip():
                                                            print("\nMatch Found... Analyzing.",end='')
                                                            th_team_name = \
                                                                th_tables[th_tables['Team1'] == th_teams][
                                                                    'Team2'].values[0]
                                                            th_team_odd = float(
                                                                th_tables[th_tables['Team1'] == th_teams][
                                                                    'Team1odd'].
                                                                    values[0])  # get the team's odd
                                                            total = (1 / first_team_odd * 100) + (
                                                            1 / second_team_odd * 100) + (1/th_team_odd * 100)
                                                            try:
                                                                if float(total) < 100:
                                                                    print(" [Found] :-)")
                                                                    if key not in web_sites.keys():
                                                                        web_sites[key] = []
                                                                    statement = '!=> %s in %s with "%f" has a perfect bet with %s in %s ' \
                                                                                ' with "%f" And %s in %s with "%f" Having a total of %f. [1x2]' % \
                                                                                (teams, key, first_team_odd,
                                                                                 second_team_name, seckey,
                                                                                 second_team_odd,th_team_name,thirkey,th_team_odd, total)
                                                                    perfect_bets.append([statement])
                                                                else:
                                                                    print(" [Failed] :-( : ", total)
                                                            except TypeError:
                                                                print("!!!!!!!!!")
                                       # second_team_draw = float(other_tables[other_tables['MatchDraw'] == other_teams]['MatchDraw'].values[0])
                                        # print(other_teams, " === ", second_team_name, " ===== ",seckey, " ===== ", key, " == ",
                                        # second_team_odd)

        return perfect_bets

if __name__ == '__main__':
    print("please run this via the main app.")
    ft = Algo()
    zt = ft.algo_check()
    if len(zt) == 0:
        print("Sorry. No Sure Bet Opportunities Were Found!")
    else:
        for result in zt:
            print("".join(result))
    input("Press any key to exit...")
