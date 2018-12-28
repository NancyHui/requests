from xlrd import open_workbook
import os.path

proDir = os.path.split(os.path.realpath(__file__))[0]
xlsPath = os.path.join(proDir, "testFile", "case.xlsx")
# print(xlsPath)

# xlrd.book.Book  Contents of a "workbook".
book = open_workbook(xlsPath)
# print(type(book.read(1, 20)))
# print(book.read(10, 200))
print(type(book))

# the number of sheets in the excel
print("nsheets:" + str(book.nsheets))

#  A list of the names of all the worksheets in the workbook file
print("sheet names:")
print(book.sheet_names())

# xlrd.sheet.Sheet object
# A list of all sheets in the book.[xlrd.sheet.Sheet object]
print(book.sheets())

print('*****************************')
# the same result from the three codes below

for sheet_index in range(book.nsheets):
    print(book.sheet_by_index(sheet_index))
    print(sheet_index)
print('*****************************')
for sheet_name in book.sheet_names():
    print(book.sheet_by_name(sheet_name))
    print(sheet_name)
print('*****************************')
for sheet in book.sheets():
    print(sheet)

print('--------------------------------------')
# book.sheet_by_name()/book.sheet_by_index() 只有这两种取xrld.Sheet.sheet对象后才有其对应的方法
sheet = book.sheets()[0]
print(type(sheet))
print(sheet)

sheet1 = book.sheet_by_name(u"Sheet1")
print(type(sheet1))
print(sheet1)
print(sheet1.nrows)
print(sheet1.ncols)

sheet2 = book.sheet_by_index(0)
print(type(sheet2))
print(sheet2)
print(sheet2.nrows)
print(sheet2.ncols)

# 获取整行和整列的值（数组）
print("+++++++++++++++++++++++++++++++++")
print("row values")
for i in range(sheet2.nrows):
    print(sheet2.row_values(i))

for j in range(sheet2.ncols):
    print(sheet2.col_values(j))

# 单元格（索引获取）
cell_A1 = sheet2.cell(0, 0).value
print(cell_A1)
cell_C4 = sheet2.cell(2, 3).value
print(cell_C4)

# 分别使用行列索引
cell_A1 = sheet2.row(0)[0].value
cell_A2 = sheet2.col(1)[0].value

cls = []
for i in range(sheet2.nrows):
    if sheet2.row_values(i)[0] != u'case_name':
        cls.append(sheet2.row_values(i))
print(cls)