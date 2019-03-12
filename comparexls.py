import xlrd
import csv


def main():

    """ The file being controlled """
    file_controling = open("Submit-Batch2.csv")
    reader = csv.reader(file_controling)
    new_rows_list = []
    for row in reader:
        row.insert(0, 'D')
        new_rows_list.append(row)
    file_controling.close()

    """ File with controling data """
    wb_control = xlrd.open_workbook("MyEPS_JPG.xls")
    ws_wb_control = wb_control.sheet_by_index(0)

    for row_index in range(0, ws_wb_control.nrows):
        compare_str = ws_wb_control.cell(row_index, 0).value
        for new_rows_list_row in new_rows_list:
            if compare_str == new_rows_list_row[1]:
                new_rows_list_row[0] = "S"

    """ Write result """
    f_result = open("result.csv", 'w', newline='')
    writer = csv.writer(f_result)
    for new_rows_list_row in new_rows_list:
        if new_rows_list_row[0] == 'S':
            del new_rows_list_row[0]
            writer.writerow(new_rows_list_row)
    f_result.close()


if __name__ == '__main__':
    main()
