import pytest

from PageObject.Locators.HomepageLoc import Locators
from Testbase.test_base import BasePage
from Utilities.screenshot import takescreenshot
from selenium import webdriver
from PageObject.Pages.Homepage import Homepage



@pytest.mark.usefixtures('setup')
class Test_Bwhistory(Homepage):
    @pytest.mark.history
    def test_TC03(self):
        Homepage.bwh(self)
        takescreenshot(self.driver,'Top Searched Products')
        self.driver.execute_script("window.scrollTo(0,400)")
        takescreenshot(self.driver,'Most Recent search')





