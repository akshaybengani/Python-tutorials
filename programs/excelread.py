import xlrd

book = xlrd.open_workbook("Book1.xlsx")

sheet = book.sheet_by_index(0)

# For getting value of total number of rows/colums
# As per sheet index
totalrows = sheet.nrows
totalcols = sheet.ncols

valueAtPos = sheet.cell_value(0,0)
print(valueAtPos)
print(totalrows," ",totalcols)

# Program to extract all columns name
for value in range(totalcols):
    print(sheet.cell_value(0,value))

print("\n\n")
# Program to extract all rows name
for value in range(totalrows):
    if value==0:
        continue
    print(sheet.cell_value(value,0))

print("\n\n")
# Program to extract a particular row value
print(sheet.row_values(1))

