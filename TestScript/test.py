from Util.ExcelUtil import *
from Config.ProjVar import *
from Action.WebElementAction import *
from Action.Reset import *
from Util.Log import *
from Util.GetTime import *


# 第一部分：获取可执行的sheet
# 解析表格
test_excel = ParseExcel(test_file_path)
# 设置当前操作的sheet为测试用例
test_excel.set_sheet_by_name(test_sheet)
# 获取所有可执行的sheet
test_case_is_exec_sheets = []
for cell in test_excel.get_rows(test_case_is_exec_col_no)[1:]:
    if cell.value.lower() == "n":
        continue
    test_case_is_exec_sheets.append(test_excel.get_cell_value(cell.row,test_case_sheet_col_no))
# print(test_case_is_exec_sheets)


count_success = 0
for sheet in test_case_is_exec_sheets:
    # 设置当前操作的sheet
    test_excel.set_sheet_by_name(sheet)

    # 第二部分：每次执行前先清空之前可执行sheet中对应列的数据
    # 遍历可执行的sheet，遍历需要清空数据的列
    need_to_clear = [case_exec_time_col_no,case_res_col_no,case_except_col_no,case_capture_pics_col_no]
    for col in need_to_clear:
        clear_cells(test_excel, sheet, col)

    # 第三部分：获取Action，开始执行sheet中的case
    test_actions_cell_obj = test_excel.get_rows(case_action_col_no)
    test_actions_cell_val = []
    for cell in test_actions_cell_obj[1:]:
        # 遍历每个Action cell
        action = cell.value
        row = cell.row
        # 获取每个Action cell所在行对应的定位方法、定位表达式、操作值
        locate_method = test_excel.get_cell_value(row,case_locate_method_col_no)
        locate_expr = test_excel.get_cell_value(row,case_locate_expr_col_no)
        operate_value = test_excel.get_cell_value(row,case_operate_val_col_no)
        print(action,locate_method,locate_expr,operate_value)
        # 执行Action
        if locate_method is None and locate_expr is None and operate_value is not None:
            cmd = "%s('%s')" % (action,operate_value)
        elif locate_method is not None and locate_expr is not None and operate_value is not None:
            cmd = "%s('%s','%s','%s')" % (action,locate_method,locate_expr,operate_value)
        elif locate_method is not None and locate_expr is not None and operate_value is None:
            cmd = "%s('%s','%s')" % (action,locate_method,locate_expr)
        elif locate_method is None and locate_expr is None and operate_value is None:
            cmd = "%s()" % action
        elif locate_method is not None and locate_expr is not None and operate_value is None:
            cmd = "%s('%s','%s')" % (action,locate_method,locate_expr)
        try:
            test_excel.write_cell(row, case_exec_time_col_no,get_current_date() + " " + get_current_time1())
            res = eval(cmd)
            # 执行成功之后，写入执行结果
            test_excel.write_cell(row,case_res_col_no,"pass")
            # 统计执行成功的次数
            count_success += 1
        except AssertionError as e:
            # 写入日志中
            logging.info(cmd + "\n" + "断言失败：\n" + traceback.format_exc())
            # 断言失败后，写入失败的结果
            test_excel.write_cell(row,case_res_col_no,"fail")
            # 失败后截图，并写入截图的位置
            pic_path = capture_pic()
            test_excel.write_cell(row,case_capture_pics_col_no,pic_path)
            # 写入失败日志
            test_excel.write_cell(row,case_except_col_no,traceback.format_exc())
        except Exception as e:
            # 写入日志中
            logging.info(cmd+"\n"+e+"\n"+traceback.format_exc())
            # 失败后截图，并写入截图的位置
            pic_path = capture_pic()
            test_excel.write_cell(row, case_capture_pics_col_no, pic_path)
            # 写入失败日志
            test_excel.write_cell(row, case_except_col_no, traceback.print_exc())
    # 如果成功的次数等于sheet有效执行行数，那么执行成功，否则执行失败
    # 并且把执行时间以及结果写入测试用例中
    if count_success == test_excel.get_max_row()-1:
        test_excel.set_sheet_by_name(test_excel.wb.sheetnames[0])
        for cell in test_excel.get_rows(test_case_sheet_col_no):
            if cell.value == sheet:
                test_excel.write_cell(cell.row,test_case_exec_time_col_no,get_current_date() + " " + get_current_time1())
                test_excel.write_cell(cell.row,test_case_exec_res_col_no,"pass")
    else:
        test_excel.set_sheet_by_name(test_excel.wb.sheetnames[0])
        for cell in test_excel.get_rows(test_case_sheet_col_no):
            if cell.value == sheet:
                test_excel.write_cell(cell.row, test_case_exec_time_col_no, get_current_date() + " " + get_current_time1())
                test_excel.write_cell(cell.row, test_case_exec_res_col_no, "fail")


