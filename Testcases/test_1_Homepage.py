import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Testcases.conftest import setup
from Testbase.test_base import BasePage
from PageObject.Locators.HomepageLoc import Locators
from Utilities.screenshot import takescreenshot
from PageObject.Pages.Homepage import Homepage

@pytest.mark.usefixtures('setup')
class Test_Amazonhomepage(Homepage):
    @pytest.mark.homepage
    def test_TC1(self):
        Homepage.langclick(self)
        takescreenshot(self.driver, 'Languageicon')
        Homepage.searchitem(self)
        takescreenshot(self.driver, 'Productresult')














