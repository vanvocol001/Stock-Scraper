from msilib.schema import tables
import requests
import pandas as pd


headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}


def get_screener(version):
    screen = requests.get(
        f'https://finviz.com/screener.ashx?v=111&s=ta_{version}', headers=headers).text

    tables = pd.read_html(screen)
    tables = tables[-2]
    tables.columns = tables.iloc[0]
    tables = tables[1:]

    return tables


print("What category of stocks do you want to see? ")
val = input("Top gainers, Top losers, New highs, New lows, Unusual volume: ")
if val == "Top gainers":
    tablestopgainers = get_screener("topgainers")
    tablestopgainers.to_csv('TopGainer.csv')
    print(get_screener("topgainers"))
if val == "Top losers":
    tablestoplosers = get_screener('toplosers')
    tablestoplosers.to_csv('TopLosers.csv')
    print(get_screener('toplosers'))
if val == "New highs":
    tablesnewhigh = get_screener("newhigh")
    tablesnewhigh.to_csv('NewHighs.csv')
    print(get_screener("newhigh"))
if val == "New lows":
    tablesnewLows = get_screener("newlow")
    tablesnewLows.to_csv('NewLows.csv')
    print(get_screener('newlow'))
if val == "Overbought":
    tablesOverbought = get_screener("overbought")
    tablesOverbought.to_csv('Overbought.csv')
    print(get_screener("overbought"))
if val == "Oversold":
    tablesoversold = get_screener("oversold")
    tablesoversold.to_csv('Oversold.csv')
    print(get_screener('oversold'))
if val == "Unusual volume":
    tablesUnusualvolume = get_screener("unusualvolume")
    tablesUnusualvolume.to_csv('UnusualVolume.csv')
    print(get_screener("unusualvolume"))