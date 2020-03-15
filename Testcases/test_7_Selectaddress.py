import time
import pytest
from PageObject.Locators.HomepageLoc import Locators
from Testbase.test_base import BasePage
from Utilities.screenshot import takescreenshot
from selenium import webdriver
from PageObject.Pages.Homepage import Homepage
from PageObject.Locators.HomepageLoc import Locators


@pytest.mark.usefixtures('setup')
class Test_SELECTADDRESS(BasePage):
    @pytest.mark.address
    def test_address(self):
        Homepage.selectaddress(self)
        time.sleep(6)
        takescreenshot(self.driver, 'All the lists of address')
        for i in Homepage.displayalladdress(self):
            print(i.get_attribute('aria-label'))

            