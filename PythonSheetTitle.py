import openpyxl
my_wb = openpyxl.Workbook()
my_sheet = my_wb.active
my_sheet_title = my_sheet.title
print("My sheet title: " + my_sheet_title)
my_sheet.title = "My New Sheet"
print("sheet name is : " + my_sheet.title)

