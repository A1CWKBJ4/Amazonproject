import time

import pytest
from selenium.webdriver import ActionChains

from PageObject.Locators.MobileLoc import Locators
from Testbase.test_base import BasePage
from Utilities.screenshot import takescreenshot
from selenium import webdriver
from PageObject.Pages.Mobilepage import Mobilepage


@pytest.mark.usefixtures('setup')
class Test_SearchIphone(Mobilepage):
    @pytest.mark.searchphone
    def test_TC04(self):
        Mobilepage.mobileclick(self)
        self.driver.execute_script("window.scrollTo(0, 500)")
        takescreenshot(self.driver, 'Top list Mobile')
        time.sleep(5)
        Mobilepage.hoveronmobile(self)
        takescreenshot(self.driver,'Mobile and Accessories')
        time.sleep(4)
        Mobilepage.clickapple(self)
        Mobilepage.searchmobie(self)









