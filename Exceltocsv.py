import pandas as pd
import os
import openpyxl as opx
import csv
import xlrd

path = 'F:\pyprogs'
filelist = os.listdir(path)

def selectsheet(filename):
    wb = opx.load_workbook(filename)
    sheets = wb.sheetnames
    for sheetname in sheets:
        sheet = wb[sheetname]
        if (sheet['A11'] == 'Who is prime minister of india?'):
             break
    return sheetname


for filename in filelist:
    if filename.endswith('.xlsx'):
        sheetname = selectsheet(filename)

        wb = xlrd.open_workbook(filename)
        filename = filename.replace('.xlsx', '.csv')
        sh = wb.sheet_by_name(sheetname)
        csvfile = open(filename, 'w')
        wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for rownum in range(11,sh.nrows):
            wr.writerow(sh.row_values(rownum))
