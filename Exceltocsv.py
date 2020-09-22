import os
import csv
import xlrd

path = '<Path to folder where .xlsx files are stored>'
filelist = os.listdir(path)

for filename in filelist:
    if filename.endswith('.xlsx'):
        print('Working on file: {}'.format(filename))
        wb = xlrd.open_workbook(filename)
        sheets = wb.sheet_names()
        for sheet in sheets :
            sh = wb.sheet_by_name(sheet)
            csvfilename = sheet+'.csv'
            csvfile = open(csvfilename, 'w')
            wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

            for rownum in range(0,sh.nrows):
                wr.writerow(sh.row_values(rownum))

            print('{0} created from sheet in {1} '.format(csvfilename,filename))
        print('File {} converted to CSV'.format(filename))

