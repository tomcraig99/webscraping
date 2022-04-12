from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://crypto.com/price/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

'''
title = soup.title
print(title.text)
'''


rows = soup.findAll('tr')
for row in rows[1:6]:
    columns = row.findAll('td')
    
    ranking = columns[1].text.strip()
    name = columns[2].find('span',attrs={'class':"chakra-text css-1mrk1dy"}).text.strip()
    symbol = columns[2].find('span',attrs={'class':'chakra-text css-ft1qn5'}).text.strip()
    price = float(columns[3].find('div',attrs={'class':"css-b1ilzc"}).text.strip().replace('$','').replace(',',''))
    #logic to only grab percentage (mainly for if %change is >10%) because I couldn't figure out how to get only percentage from the website
    percentageChange = columns[3].find('div',attrs={'class':"css-16q9pr7"}).text.strip()
    for char in percentageChange:
        if char == '+' or char == '-':
            pos = len(percentageChange)-percentageChange.index(char)
    percentageChange = percentageChange[-pos:]

    alert = False
    if symbol == 'BTC':
        if price < 40000:
            alert = True
            pass #twilio text stuff

    elif symbol == 'ETH':
        if price < 3000:
            alert = True
            pass #twilio text stuff

    print()
    print(f"Ranking: {ranking}")
    print(f"Currency: {name} ({symbol})")
    print(f"Current Price: ${price} ({percentageChange})")
    if alert:
        print("Sent text message, buy!")
    print()
    
