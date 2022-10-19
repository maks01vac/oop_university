import csv
import json
import requests
urlBTC = "http://jservice.io/api/clues?value=100&min_date=1985-02-20"
urlETH = ""
urlDOGE = ""


response = requests.get(urlBTC)
response = response.json()

def createCsvFile():
    with open("data.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(
            ("name cryptocurrency","date","price")
        )    

def appendData(nameCryptho,response):
    for game in response:
        with open("data.csv", "a") as file:
            writer=csv.writer(file)
            writer.writerow(
                [
                    nameCryptho,
                    game['question'],
                    game['game_id']
                ]
            )

def createAndFillCsv():
    createCsvFile()
    appendData("BTC",response)
    appendData("ETH",response)
    appendData("DOGE",response)