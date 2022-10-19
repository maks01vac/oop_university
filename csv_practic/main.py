import csv
import json
import requests
import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


urlBTC = "https://api.coincap.io/v2/assets/bitcoin/history?interval=d1"
urlETH = "https://api.coincap.io/v2/assets/ethereum/history?interval=d1"
urlSOCKS = "https://api.coincap.io/v2/assets/unisocks/history?interval=d1"

def getAndFormatData(url):
    response = requests.get(url)
    response = response.json()
    response = response['data']

    for elem in response:
        listDate = elem['date'].rsplit('T')
        elem['date'] = listDate[0]

    return response

def createCsvFile():
    with open("data.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(
            ("name cryptocurrency","date","price")
        )    

def appendData(nameCryptho,response):
    for day in response:
        with open("data.csv", "a") as file:
            writer=csv.writer(file)
            writer.writerow(
                [
                    nameCryptho,
                    day['date'],
                    day['priceUsd']
                ]
            )

responseBTC = getAndFormatData(urlBTC)
responseETH = getAndFormatData(urlETH)
responseSOCKS = getAndFormatData(urlSOCKS)


def createAndFillCsv():
    createCsvFile()
    appendData("BTC",responseBTC)
    appendData("ETH",responseETH)
    appendData("SOCKS",responseSOCKS)

createAndFillCsv()




data = pd.read_csv('data.csv', index_col='name cryptocurrency')

dataBTC = data.loc['BTC']
dataETH = data.loc['ETH']
dataSOCKS = data.loc['SOCKS']

plt.plot(dataSOCKS['date'], dataSOCKS['price'], label='Unisocks')
plt.plot(dataETH['date'], dataETH['price'], label='Ethereum')
plt.plot(dataBTC['date'], dataBTC['price'], label='Bitcoin')


plt.title('Rate of cryptocurrencies')

plt.xlabel('date')
plt.ylabel('price in $')

plt.legend(fontsize = 10)

plt.xticks(np.arange(0, len(dataSOCKS), 80))

plt.show()

