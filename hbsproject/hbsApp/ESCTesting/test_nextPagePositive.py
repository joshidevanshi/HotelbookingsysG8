# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestNextPagePositive():
  def setup_method(self, method=None):
    self.driver = webdriver.Firefox(executable_path=r'C:/geckodriver.exe')
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_nextPagePositive(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1434, 703)
    self.driver.find_element(By.CSS_SELECTOR, ".fa-bars").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > a").click()
    self.driver.execute_script("window.scrollBy(0,{})".format(600))
    time.sleep(2)
    self.driver.find_element(By.NAME, "hotel_date").click()
    self.driver.find_element(By.CSS_SELECTOR, ".pmu-sunday:nth-child(7)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".pmu-days > .pmu-button:nth-child(8)").click()
    self.driver.find_element(By.ID, "destination").click()
    self.driver.find_element(By.ID, "destination").send_keys("Singapore, Singapore")
    self.driver.find_element(By.ID, "sub").click()
    time.sleep(10)
    self.driver.execute_script("window.scrollBy(0,{})".format(1000))
    time.sleep(1)
    self.driver.find_element(By.ID, "plus").click()
    self.driver.find_element(By.CSS_SELECTOR, ".tm-main > p").click()
    self.driver.close()
  
if __name__ == '__main__':
# TestDestinationNegative testing
    test = TestNextPagePositive()
    test.setup_method()
    start = time.time()
    test.test_nextPagePositive()
    print('run success time is '+ str(time.time()-start))
    time.sleep(2)
    # 关闭程序
    test.teardown_method()