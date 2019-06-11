from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import traceback
import time

class WaitUtil(object):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)
        self.locate_method = {
            "id":By.ID,
            "xpath":By.XPATH,
            "name":By.NAME,
            "tag_name":By.TAG_NAME,
            "link_text":By.LINK_TEXT,
            "partial_link_text":By.PARTIAL_LINK_TEXT,
        }

    def presenceofElement(self,locate_method,locate_expr):
        try:
            element = self.wait.until(EC.presence_of_element_located(
                (self.locate_method[locate_method],locate_expr)))
            # element = self.wait.until(lambda x: x.find_element(self.locate_method[locate_method], locate_expr))
            return element
        except TimeoutException:
            traceback.print_exc()
            raise TimeoutException

    def visableofElement(self,locate_method,locate_expr):
        try:
            element = self.wait.until(EC.visibility_of_element_located(
                (self.locate_method[locate_method],locate_expr)))
            return element
        except TimeoutException:
            traceback.print_exc()
            raise TimeoutException

    def switchToFrame(self,locate_method,locate_expr):
        try:
            element = self.wait.until(EC.frame_to_be_available_and_switch_to_it(
                (self.locate_method[locate_method],locate_expr)))
            return element
        except Exception as e:
            raise e


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="c:\chromedriver.exe")
    wait_obj = WaitUtil(driver)
    driver.get("https://www.baidu.com")
    try:
        element = wait_obj.visableofElement("id","kw")
        element.send_keys(u"西游记")
    except:
        print("operate fail!")
    finally:
        driver.close()

    # driver.get("http://mail.126.com")
    # try:
        # iframe = driver.find_element_by_xpath("//iframe[contains(@id,'x-URS-iframe')]")
        # driver.switch_to_frame(iframe)
        # wait_obj.switchToFrame("xpath", "//iframe[contains(@id,'x-URS-iframe')]")
        # time.sleep(3)
        # wait_obj.presenceofElement("name", "email")
        # wait_obj.visableofElement("name", "password")
    # except TimeoutException:
    #     print("Not Find!")
    # finally:
    #     driver.close()