from selenium import webdriver
from Config.ProjVar import *
from Util.WaitUtil import *
import time
from Util.Log import *
from Util.Dir import *

driver = None


def open_browser(browser):
    global driver
    all_browser = ["ie","chrome","firefox","edge"]
    if browser in all_browser:
        if browser.lower() == "ie":
            driver = webdriver.Ie(executable_path=ie_driver_path)
        elif browser.lower() == "chrome":
            driver = webdriver.Chrome(executable_path=chrome_driver_path)
        elif browser.lower() == "firefox":
            driver = webdriver.Firefox(executable_path=firefox_driver_path)
        elif browser.lower() == "edge":
            driver = webdriver.Edge(executable_path=edge_driver_path)
    else:
        return driver

def visit(url):
    global driver
    try:
        driver.get(url)
    except:
        logging.info("%s can not be visited!" %url)
        raise Exception("网址%s无法访问" %url)

def input(locate_method,locate_expr,content):
    global driver
    try:
        element = WaitUtil(driver).visableofElement(locate_method,locate_expr)
        element.send_keys(content)
    except:
        logging.info("webelement:%s->%s  operate fail" % (locate_method, locate_expr))

def sleep(duration):
    if isinstance(duration,(int,float)):
        time.sleep(duration)
    elif isinstance(duration,str):
        try:
            duration = int(duration)
            time.sleep(duration)
        except:
            pass

def click(locate_method,locate_expr):
    global driver
    try:
        wait_obj = WaitUtil(driver)
        element = wait_obj.visableofElement(locate_method, locate_expr)
        element.click()
    except:
        logging.info("webelement:%s->%s  operate fail" % (
            locate_method, locate_expr))


def assert_word(word):
    global driver
    assert word in driver.page_source


def quit():
    global driver
    driver.close()


def capture_pic():
    global driver
    try:
        date_dir = make_date_dir(pic_file_path)
        screenshot_file_path = os.path.join(date_dir,get_current_time() + ".png")
        driver.get_screenshot_as_file(screenshot_file_path)
    except IOError as e:
        logging.info(e)
        traceback.print_exc()
    except Exception as e:
        logging.info(e)
        traceback.print_exc()
    return screenshot_file_path


if __name__ == "__main__":
    try:
        open_browser("chrome")
        visit("https://www.baidu.com")
        input("id","kw","微博")
        click("id","su")
        sleep(5)
        assert_word("https://www.weibo.com/login.php")
        quit()
    except Exception as e:
        print("execute fail reason:")
        traceback.print_exc()
    finally:
        quit()