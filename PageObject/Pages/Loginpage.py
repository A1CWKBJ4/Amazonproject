from selenium import webdriver
from PageObject.Locators.LoginpageLoc import Locators
from Testbase.test_base import BasePage

class Loginpage(BasePage):

    def clickonHello(self):
        self.click(Locators.SIGN_IN)

    def enterusername(self):
        self.enter_text(Locators.PHONE,'9810527338')

    def clickoncontinue(self):
        self.click(Locators.CONTINUE)

    def enterpassword(self):
        self.enter_text(Locators.PASSWORD,'11bcl1038')

    def clickonsubmit(self):
        self.click(Locators.SUBMIT)