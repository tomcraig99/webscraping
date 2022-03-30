# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from cgi import test
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


req= Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title
print(title.text)


table_rows = soup.findAll('tr')

highestDeathName = ''
highestDeathRatio = 0.0
highestTestRatio = 0.0
highestTestName = ''
lowestTestRatio = 100.0
lowestTestName = ''

for row in table_rows[2:51]:
    td = row.findAll('td')

    state = td[1].text.strip()
    totalCases = int(td[2].text.replace(',',''))
    deaths = int(td[4].text.replace(',',''))
    totalTested = int(td[10].text.replace(',',''))

    ratio = deaths/totalCases
    tested = totalCases/totalTested

    if ratio > highestDeathRatio:
        highestDeathRatio = ratio
        highestDeathName = state
    
    if tested < lowestTestRatio:
        lowestTestRatio = tested
        lowestTestName = state
    elif tested > highestTestRatio:
        highestTestRatio = tested
        highestTestName = state
    '''
    print(f"state: {state}")
    print(f"Total Cases: {totalCases}")
    print(f"Deaths: {deaths}")
    print(f"Total Tested: {totalTested}")
    '''

print(f"\nHighest Death Ratio: \n{highestDeathName}: {format(highestDeathRatio, '.2%')}\n")
print(f"Highest Positivity Ratio: \n{highestTestName}: {format(highestTestRatio, '.2%')}\n")
print(f"Lowest Positivity ratio: \n{lowestTestName}: {format(lowestTestRatio, '.2%')}\n")

#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

