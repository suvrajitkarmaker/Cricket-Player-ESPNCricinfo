import requests
from bs4 import BeautifulSoup as bs
import csv 

def getCountryInfo(number, catagoryNumber):
    r = requests.get('https://www.espncricinfo.com/ci/content/player/country.html?country='+str(number))

    soup = bs(r.content,'html.parser')
    playerList = soup.find_all("table")[catagoryNumber]
    playerList = playerList.find_all("td")

    countryName = soup.find("p", class_ = "ciGblSectionHead")
    countryName = countryName.text
    countryName = countryName.split(" ")
    countryName = countryName[-1]

    countryList.append(countryName)

    cnt = 0
    for item in playerList:
        try:
            dictList[cnt][countryName]=item.text
        except:
            dictList.append({countryName:item.text})
        cnt+=1

def writeCsv(csvFileName):
    with open(str(csvFileName)+'.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=countryList)

        writer.writeheader()
        writer.writerows(dictList)



if __name__ == '__main__':

    catagory = ['AllRecentPlayers', 'TestPlayers', 'ODIPlayers', 'T20Players', 'ContractedPlayers']

    for catagoryNumber in range(0,len(catagory)):
        dictList = []
        countryList = []
        countryListNumber = [25, 2, 1, 6, 5, 7, 3, 8, 4, 9, 40, 29]
        for i in countryListNumber:
            getCountryInfo(i, catagoryNumber)
        writeCsv(catagory[catagoryNumber])
