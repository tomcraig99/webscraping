from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

#print(title.text)
##
##
##
##
wb = xl.Workbook()
MySheet = wb.active
MySheet.Title = 'Box Office Report'

fontObject = Font(size=16,bold=True)
MySheet.column_dimensions['A'].width = 5
MySheet.column_dimensions['B'].width = 30
MySheet.column_dimensions['C'].width = 25
MySheet.column_dimensions['D'].width = 16
MySheet.column_dimensions['E'].width = 20
MySheet.column_dimensions['F'].width = 26

MySheet['A1'] = 'No.'
MySheet['A1'].font = fontObject
MySheet['B1'] = 'Movie Title'
MySheet['B1'].font = fontObject
MySheet['C1'] = 'Release Date'
MySheet['C1'].font = fontObject
MySheet['D1'] = 'Gross'
MySheet['D1'].font = fontObject
MySheet['E1'] = 'Total Gross'
MySheet['E1'].font = fontObject
MySheet['F1'] = '% Of Total Gross'
MySheet['F1'].font = fontObject

i=2

rows = soup.findAll('tr')
for row in rows[1:6]:
    td = row.findAll('td')
    
    ranking = td[0].text.strip()
    name = td[1].text.strip()
    releaseDate = td[8].text.strip()
    gross = int(td[5].text.strip().replace(',','').replace('$',''))
    total = int(td[7].text.strip().replace(',','').replace('$',''))
  
    MySheet['A' + str(i)] = ranking
    MySheet['B' + str(i)] = name
    MySheet['C' + str(i)] = releaseDate
    MySheet['D' + str(i)] = '$' + str(format(gross, ','))
    MySheet['E' + str(i)] = '$' + str(format(total, ','))
    MySheet['F' + str(i)] = str(format(round((float(gross)/float(total))*100, 2), '.2f')) + '%'

    i+=1

wb.save('MovieReport.xlsx')