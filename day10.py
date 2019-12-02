# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:33:23 2019

@author: Moath
"""

import xlsxwriter

# =============================================================================
# workbook = xlsxwriter.Workbook('example10.xlsx')
# worksheet = workbook.add_worksheet()
# 
# worksheet.autofilter('A1:B4')
# 
# data = ['Test', 10, 40, 50, 20]
# 
# format = workbook.add_format()
# format.set_bold()
# format.set_font_color('red')
# format.set_font_size(20)
# 
# worksheet.write_column('A1', data, format)
# worksheet.write_comment('B1', 'This is a comment')
# 
# format2 = workbook.add_format({'bold' : True, 'font_color': 'blue'})
# worksheet.write_column('B1', data, format2)
# 
# workbook.close()
# =============================================================================

print('-----------------------------------------------')

# =============================================================================
# workbook = xlsxwriter.Workbook('chart_line.xlsx')
# worksheet = workbook.add_worksheet()
# 
# data = [10, 40, 50, 20, 10, 50]
# worksheet.write_column('A1', data)
# 
# chart = workbook.add_chart({'type' : 'line'})
# 
# chart.add_series({'values' : '=Sheet1!$A$1:$A$6'})
# 
# worksheet.insert_chart('C1', chart)
# 
# workbook.close()
# =============================================================================

print('-----------------------------------')

# =============================================================================
# from xlwt import Workbook, Formula
# 
# book = Workbook()
# 
# sheet1 = book.add_sheet('Sheet 1')
# sheet1.write(0, 0, 10)
# sheet1.write(0, 1, 20)
# sheet1.write(1, 0, Formula('A1 / B1'))
# 
# sheet2 = book.add_sheet('Sheet 2')
# row = sheet2.row(0)
# row.write(0, Formula('sum(1,2,3)'))
# row.write(1, Formula('SuM(1;2;3)'))
# row.write(2, Formula("$A$1+$B$1*SUM('ShEEt 1'!$A$1:$b$2)"))
# 
# book.save('example4.xls')
# 
# =============================================================================

print('-----------------------------------')

# =============================================================================
# from xlrd import open_workbook
# 
# wb = open_workbook('simple.xls')
# for s in wb.sheets():
#     print('Sheet: ', s.name)
#     for row in range(s.nrows):
#         values = []
#         for col in range(s.ncols):
#             values.append(s.cell(row, col).value)
#         print(','.join(values))
# =============================================================================























