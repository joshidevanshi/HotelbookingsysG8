# Generated by Selenium IDE
from random import random
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
import random
class TestRegisterPositive():
  def setup_method(self, method=None):
    self.driver = webdriver.Firefox(executable_path=r'C:/geckodriver.exe')
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_registerPositive(self):
    self.driver.get("http://127.0.0.1:8000/user/register")
    self.driver.set_window_size(1434, 699)
    # random input
    num = random.randint(5, 8)
    str = ''
    em =str.join(random.choice("0123456789qwertyuiopasdfghjklzxcvbnm!@#$%^&*()") for i in range(num))
    print('em :',em)
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys(em+"@gmail.com")
    num_2 = random.randint(10,16)
    str = ''
    paswd =str.join(random.choice("0123456789qwertyuiopasdfghjklzxcvbnm!@#$%^&*()") for i in range(num_2))
    print('paswd :',paswd)
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys(paswd)
    self.driver.find_element(By.ID, "passwordrepeat").click()
    self.driver.find_element(By.ID, "passwordrepeat").send_keys(paswd)
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.get("http://127.0.0.1:8000/admin/")
    self.driver.find_element(By.ID, "id_username").click()
    self.driver.find_element(By.ID, "id_username").send_keys("escgroup8")
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.ID, "id_password").send_keys("123456")
    self.driver.find_element(By.CSS_SELECTOR, ".submit-row > input").click()
    self.driver.find_element(By.LINK_TEXT, "Users").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > .field-email").click()
    self.driver.close()
  

if __name__ == '__main__':
# TestRegisterPositive testing
    test = TestRegisterPositive()
    test.setup_method()
    start = time.time()
    test.test_registerPositive()
    print('--------------------------------------------')
    print('run success time is '+ str(time.time()-start))
    time.sleep(2)
    # 关闭程序
    test.teardown_method()
