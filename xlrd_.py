import xlrd


# ----------------------------------------------------------------------
def open_file(path):
    """
    Open and read an Excel file
    """
    book = xlrd.open_workbook(path)

    # print number of sheets
    print ("  number of sheets is - " + str(book.nsheets))

    # print sheet names
    print ("sheet names are: " + str(book.sheet_names()))


    # get the first worksheet
    first_sheet = book.sheet_by_index(0)

    # read a row
    print ("first worksheet riw is: " + str( first_sheet.row_values(0)))

    # read a cell
    cell = first_sheet.cell(0, 0)
    print ('cell is: ', cell)
    print ('cell value is: ', cell.value)

    # read a row slice
    print ('row slice is ', first_sheet.row_slice(rowx=1,
                          start_colx=0,
                          end_colx=20)
           )
"""
"""
# ----------------------------------------------------------------------
if __name__ == "__main__":
    path = "test.xls"
    open_file('/home/denis/015.12.01_Reestr.xls')