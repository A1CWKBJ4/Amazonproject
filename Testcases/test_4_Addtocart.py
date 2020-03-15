import time
import pytest
from selenium.webdriver import ActionChains
from PageObject.Locators.MobileLoc import Locators
from Testbase.test_base import BasePage
from Utilities.screenshot import takescreenshot
from selenium import webdriver
from PageObject.Pages.Mobilepage import Mobilepage


@pytest.mark.usefixtures('setup')
class Test_ADDCART(Mobilepage):
    @pytest.mark.sanity
    def test_addtocart(self):
        Mobilepage.mobileclick(self)
        Mobilepage.hoveronmobile(self)
        time.sleep(5)
        Mobilepage.clickapple(self)
        Mobilepage.searchmobie(self)
        handles = self.driver.window_handles
        size = len(handles)
        parent_handle = self.driver.current_window_handle
        for x in range(size):
            if handles[x] != parent_handle:
                self.driver.switch_to.window(handles[x])
                takescreenshot(self.driver, 'Searched Product')
                BasePage.click(self, Locators.Addcart)
                takescreenshot(self.driver, 'Addded into cart')










