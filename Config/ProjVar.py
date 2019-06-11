import os

# 工程目录
proj_path = os.path.normpath(os.path.dirname(os.path.dirname(__file__)))

# 日志配置文件目录
log_conf_path = os.path.normpath(os.path.join(proj_path,"Config","Logger.conf"))

# 浏览器的插件位置
ie_driver_path = "c:\\IEDriverServer.exe"
edge_driver_path = "c:\\MicrosoftWebDriver.exe"
chrome_driver_path = "c:\\chromedriver.exe"
firefox_driver_path = "c:\\geckodriver.exe"

# 截图存放路径
pic_file_path = os.path.join(proj_path,"capture_pics")

# 测试用例存放路径
test_file_path = os.path.join(proj_path,"TestData",u"测试用例.xlsx")

# 测试用例表
test_sheet = u"测试用例"
test_case_sheet_col_no = 3
test_case_is_exec_col_no = 4
test_case_exec_time_col_no = 5
test_case_exec_res_col_no = 6

# 测试具体的case
case_action_col_no = 2
case_locate_method_col_no = 3
case_locate_expr_col_no = 4
case_operate_val_col_no = 5
case_exec_time_col_no = 6
case_res_col_no = 7
case_except_col_no = 8
case_capture_pics_col_no = 9

# 存放Object的地方
object_path = os.path.join(proj_path,"TestData","ObjectDeposit.ini")




if __name__ == "__main__":
    print(proj_path)
    print(test_file_path)