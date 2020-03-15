import time
import pytest
from PageObject.Pages.Shoppingcartpage import Shoppingcart
from selenium.webdriver import ActionChains
from PageObject.Locators.ShoppingcartLoc import Locators
from PageObject.Locators.HomepageLoc import Locators
from Testbase.test_base import BasePage
from Utilities.screenshot import takescreenshot
from selenium import webdriver
from PageObject.Pages.Homepage import Homepage


@pytest.mark.usefixtures('setup')
class Test_REMOVECART(BasePage):
    @pytest.mark.removecart
    def test_removecart(self):
        Homepage.cartvalue(self)
        takescreenshot(self.driver, 'BeforeDeleting')
        '''Shoppingcart.deleteitem(self)
        Homepage.logout(self)'''

        '''ids = self.driver.find_elements_by_xpath("//*[@value='Delete']")
        for i in ids:
            print(i.get_attribute('aria-label'))
            if 'Boots' in i.get_attribute('aria-label'):
                i.click()
                break'''
        for i in Shoppingcart.allelements(self):
             print(i.get_attribute('aria-label'))




