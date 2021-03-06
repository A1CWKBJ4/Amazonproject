import time
import pytest
from selenium import webdriver



@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome("C:/Users/LADDUGOPAL/Desktop/chromedriver.exe") #if not added in PATH
    driver.implicitly_wait(10)
    driver.get("http:www.amazon.in")
    driver.maximize_window()
    driver.find_element_by_id('nav-link-accountList').click()
    driver.find_element_by_id('ap_email').send_keys('9810527338')
    driver.find_element_by_id('continue').click()
    driver.find_element_by_id('ap_password').send_keys('11bcl1038')
    driver.find_element_by_id('signInSubmit').click()

    time.sleep(20)

    request.cls.driver = driver

    yield driver
    driver.quit()