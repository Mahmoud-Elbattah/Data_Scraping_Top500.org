from urllib.request import urlopen
from bs4 import BeautifulSoup


def getBasicInfo(url):
    soup = BeautifulSoup(urlopen(url))
    tableRows = soup.find('table', class_='table table-condensed').findAll("tr")[1:]
    segment = str(tableRows[0].findAll('td')[0].text).strip()
    city = str(tableRows[1].findAll('td')[0].text).strip()
    country = str(tableRows[2].findAll('td')[0].text).strip()
    return (segment,city,country)



def getSpecsInfo(url):
    soup = BeautifulSoup(urlopen(url))
    tableRows = soup.find('table', class_='table table-responsive').findAll("tr")
    manufacturer = str(tableRows[1].findAll('td')[3].text).strip()

    #Getting OS name
    tableRows = soup.find('table', class_='table table-condensed').findAll("tr")
    for row in tableRows:
        header = row.findAll("th", text='Operating System:')
        if len(header) == 1:
            OS = str(row.findAll("td")[0].text).strip()
            break
    return (manufacturer,OS)

def main():
    outputFile = open('top500.csv', 'a')
    #Writing Header Row
    outputFile.write("Segment,OS")
    rank = 1
    for i in range(1,6):
        url = 'https://www.top500.org/list/2017/06/?page='+str(i)
        print(url)
        page = urlopen(url)
        soup = BeautifulSoup(page)
        table=soup.find('table', class_='table table-condensed table-striped')
        for row in table.findAll("tr")[1:]:
            print("Rank: ", rank)
            try:
                #First, getting the city and country
                cells = row.findAll('td')
                url_1 = "https://www.top500.org" + str(cells[1].findAll("a")[0]['href'])
                name = str(cells[1].findAll("a")[0].text)
                (segment, city, country) = getBasicInfo(url_1)
                #Second, getting specs
                url_2="https://www.top500.org" + str(cells[2].findAll("a")[0]['href'])
                (manufacturer, OS) = getSpecsInfo(url_2)
                #print(manufacturer, coresCount, rMax, rPeak, power)
                outputFile.write("\n" + str(rank) + "," + name
                                 + "," + city + "," +country
                                 + "," + manufacturer +","+ segment + "," +OS)
            except:
                outputFile.write("\n" + str(rank) + ",NULL,NULL,NULL,NULL,NULL,NULL")
            rank=rank+1

    outputFile.close()
    print("End of Crawling!")

main()
