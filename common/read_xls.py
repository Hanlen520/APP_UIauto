import os,sys
import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple

def read_xls(filename):
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)) + "\\data", filename)
    xl=xlrd.open_workbook(file_path)
    table=xl.sheet_by_index(0)
    rows=table.nrows
    cols=table.ncols
    all_content=[]
    for i in range(rows):
        if i==0:
            continue
        row_content=[]
        for j in range(cols):
            ctype=table.cell(i,j).ctype
            cell=table.cell_value(i,j)
            if ctype==2 and cell%1==0:
                cell=str(int(cell))
            row_content.append(cell)
        all_content.append(row_content)
    return all_content

a=read_xls('test_data.xlsx')
