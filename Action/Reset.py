from Util.ExcelUtil import *
from Config.ProjVar import *
import traceback


def clear_cells(test_excel,exec_sheet,col_no):
    try:
        # 设置当前操作的sheet
        test_excel.set_sheet_by_name(exec_sheet)
        # 获取一列
        clear_col = test_excel.get_rows(col_no)[1:]
        # 遍历每列，并且清空单元格中的数据
        for cell in clear_col:
            # print(cell.row,cell.column)
            test_excel.write_cell(cell.row,cell.column,"")
    except:
        traceback.print_exc()
        return False


if __name__ == "__main__":
    # 解析表格
    test_excel = ParseExcel(test_file_path)
    # 设置当前操作的sheet为测试用例
    test_excel.set_sheet_by_name(test_sheet)
    # 获取所有可执行的sheet
    test_case_is_exec_sheets = []
    for cell in test_excel.get_rows(test_case_is_exec_col_no)[1:]:
        if cell.value.lower() == "n":
            continue
        test_case_is_exec_sheets.append(test_excel.get_cell_value(cell.row, test_case_sheet_col_no))
    # print(test_case_is_exec_sheets)

    # 遍历可执行的sheet，遍历需要清空数据的列
    for sheet in test_case_is_exec_sheets:
        for col in [case_exec_time_col_no,case_res_col_no,case_except_col_no,case_capture_pics_col_no]:
            clear_cells(test_excel,sheet,col)