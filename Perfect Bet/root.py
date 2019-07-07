import os

import requests

import algotest
from FinishedProject import betikascraper
from FinishedProject import betpawascraper
from FinishedProject import betwayscraper
from FinishedProject import dafabetscraper
from FinishedProject import mchezascraper
from FinishedProject import onexbetscraper
from FinishedProject import spscraper


def default_border():
    border = "===================================================================================="
    fstring = "|| |=======   |=====  |=====    |=======         |=======   |=======  ============ ||"
    fstring1 = "|| |       |  |       |     |   |                |       |  |              ||      ||"
    fstring2 = "|| |=======   |=====  |=====    |=======         |========  |=======       ||      ||"
    fstring3 = "|| |          |       |     ||  |                |        | |              ||      ||"
    fstring4 = "|| |          |=====  |       | |        _______ |========  |=======       ||      ||"
    print(border)
    print(fstring)
    print(fstring1)
    print(fstring2)
    print(fstring3)
    print(fstring4)
    print(border)


def betika_results():
    betika_init = betikascraper.Betika_Scraper()
    betika_out = betika_init.betika_dataframe()
    betika_out.to_csv('betikatable.csv', encoding="ISO-8859-1")
    return betika_out


def betpawa_results():
    betpawa_init = betpawascraper.Betpawa_Scraper()
    betpawa_out = betpawa_init.betpawa_dataframe()
    betpawa_out.to_csv('betpawa.csv', encoding="ISO-8859-1")
    return  betpawa_out


def betway_results():
    betway_init = betwayscraper.BetWay_Scraper()
    betway_out = betway_init.betway_dataframe()
    betway_out.to_csv('betway.csv', encoding="ISO-8859-1")
    return betway_out


def dafabet_results():
    dafabet_init = dafabetscraper.Dafabet_Scraper()
    dafabet_out = dafabet_init.dafabet_dataframe()
    dafabet_out.to_csv('dafabet.csv', encoding="ISO-8859-1")
    return dafabet_out


def dafabet_ou_results():
    dafabet_init = dafabetscraper.Dafabet_Scraper()
    dafabet_out = dafabet_init.dafabet_ou_dataframe()
    dafabet_out.to_csv('dafabet_ou.csv', encoding="ISO-8859-1")
    return dafabet_out


def mcheza_reslts():
    mcheza_init = mchezascraper.Mcheza_Scraper()
    mcheza_out = mcheza_init.mcheza_dataframe()
    mcheza_out.to_csv('mcheza.csv', encoding="ISO-8859-1")
    return mcheza_out


def mcheza_ou_results():
    mcheza_init = mchezascraper.Mcheza_Scraper()
    mcheza_out = mcheza_init.mcheza_ou_dataframe()
    mcheza_out.to_csv('mcheza_ou.csv', encoding="ISO-8859-1")
    return mcheza_out


def sp_results():
    sp_init = spscraper.SportPesa()
    sp_out = sp_init.sp_dataframe()
    sp_out.to_csv('sp.csv', encoding="ISO-8859-1")
    return sp_out


def onexbet_results():
    onexbet_init = onexbetscraper.onexbet()
    onexbet_out = onexbet_init.one_dataframe()
    onexbet_out.to_csv('onexbet.csv',encoding="ISO-8859-1")
    return onexbet_out


def check_duplicates():
    pass


def match_results():
    algo = algotest.Algo()
    results = algo.algo_check()
    return results


def print_perfect_bets(bets_list):
    for p_bet in bets_list:
        print("".join(p_bet))


def checknet():
    for timeout in [1, 5, 10, 15]:
        try:
            response = requests.get("http://www.google.com")
            return True
        except requests.ConnectionError:
            print("Could not connect")
            return False


def main():
    condition = True
    print("\n|| Application Loaded Succesfully")
    print("=================================================")
    print("\n Please wait while we get the data for you...")
    print("=================================================")
    betika = betika_results()
    betpawa = betpawa_results()
    betway = betway_results()
    dafabet = dafabet_results()
    dafabet_ou = dafabet_ou_results()
    mcheza = mcheza_reslts()
    mcheza_ou = mcheza_ou_results()
    sportpesa = sp_results()
    while condition:
        print("\n=============================================")
        print("!= ALL Results Have Been Loaded Successfully.")
        print("=============================================")
        default_border()
        print("====[ Welcome To PERFECT_BET ]====")
        print("\n")
        print("1.Display Betika Results")
        print("2.Display Betpawa Results")
        print("3.Display Betway Results")
        print("4.Display Dafabet Results")
        print("5.Display M-Cheza Results")
        print("6.Display Sport-Pesa Results")
        print("7.Display Dafabet [OU] Results")
        print("8.Display Mcheza [OU] Results")
        print("9.Run Perfect Bet Analysis")
        print("10.Exit")
        choice = int(input("Please Enter Your Choice (1,2,3...8): "))
        if choice > 10 or choice < 1:
            print("Invalid Choice!")
            continue
        elif choice == 1:
            print(betika)
            input("Enter Any Key To Proceed...")
            os.system('cls')
            continue
        elif choice == 2:
            print(betpawa)
            input("Enter Any Key To Proceed...")
            os.system('cls')
            continue
        elif choice == 3:
            print(betway)
            input("Enter Any Key To Proceed...")
            os.system('cls')
            continue
        elif choice == 4:
            print(dafabet)
            input("Enter Any Key To Proceed...")
            os.system('cls')
            continue
        elif choice == 5:
            print(mcheza)
            input("Enter Any Key To Proceed...")
            os.system('cls')
            continue
        elif choice == 6:
            print(sportpesa)
            input("Enter Any Key To Proceed...")
            os.system('cls')
            continue
        elif choice == 7:
            print(dafabet_ou)
            input("Enter Any Key To Proceed...")
            os.system('cls')
            continue
        elif choice == 8:
            print(mcheza_ou)
            input("Enter Any Key To Proceed...")
            os.system('cls')
            continue
        elif choice == 9:
            print_perfect_bets(match_results())
            input("Enter Any Key To Proceed...")
            os.system('cls')
            continue
        elif choice == 10:
            condition = False


if __name__ == "__main__":
    if checknet():
        main()
    else:
        default_border()
        print("No Internet Connection Was Found. Please Recheck And Try Again")
        input("Press Any Key To Exit..")