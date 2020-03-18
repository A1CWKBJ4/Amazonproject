import time
import pytest
from Testbase.test_base import BasePage
from Utilities.screenshot import takescreenshot
from selenium import webdriver
from PageObject.Pages.Homepage import Homepage
from PageObject.Pages.Loginpage import Loginpage
from Datareader.Registration_Iterator import Registration

@pytest.mark.usefixtures('setup')
class Test_REGISTRAION(BasePage):
    @pytest.mark.registration
    def test_registration(self):
        Homepage.hoveronhello(self)
        Homepage.switchaccount(self)
        Loginpage.addaccount(self)
        Loginpage.createaccount(self)
        time.sleep(10)
        for i in range(Registration.rowscount(self)):
            Loginpage.name(self,i)
            Loginpage.cell(self, i)
            Loginpage.email(self,i)
            Loginpage.pwd(self,i)
            takescreenshot(self.driver, "data+ i")


        time.sleep(5)



