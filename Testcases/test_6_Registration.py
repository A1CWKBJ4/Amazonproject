import time
import pytest
from Testbase.test_base import BasePage
from Utilities.screenshot import takescreenshot
from selenium import webdriver
from PageObject.Pages.Registrationpage import Registration
from PageObject.Pages.Loginpage import Loginpage


@pytest.mark.usefixtures('setup')
class Test_Registration(BasePage):

    def test_newuser(self):
        Loginpage.clickonHello(self)
        Registration.createacc(self)
        Registration.firstname(self)
        Registration.mobile(self)
        Registration.email(self)
        Registration.pwd(self)
        Registration.submit(self)




