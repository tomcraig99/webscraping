import openpyxl as xl
from openpyxl.styles import Font

#create new excel document

wb = xl.Workbook()

MySheet = wb.active

MySheet.title = 'First Sheet'

#create new worksheet
wb.create_sheet(index=1,title='Second Sheet')

#write content to cell
MySheet['A1'] = 'An Example of Sum Formula'

#change font and italicize
MySheet['A1'].font = Font(name='Times New Roman', size=24, italic=True, bold=True)

#font object
fontObject = Font(name='Times New Roman', size=24, italic=True, bold=True)
MySheet['A1'].font = fontObject

#adding values to cells
MySheet['B2'] = 50
MySheet['B3'] = 75
MySheet['B4'] = 100
MySheet['A6'] = 'Total'
MySheet['A6'].font = Font(size=16,bold=True)
MySheet['B6'] = '=SUM(B2:B4)'

#columnm dimensions
MySheet.column_dimensions['A'].width = 25


wb.save('PythonToExcel.xlsx')