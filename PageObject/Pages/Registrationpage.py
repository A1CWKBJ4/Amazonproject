from selenium import webdriver
from PageObject.Locators.LoginpageLoc import Locators
from Testbase.test_base import BasePage
from PageObject.Pages.Homepage import Homepage


class Registration(BasePage):

    def createacc(self):
        self.click(Locators.CREATEACC)

    def firstname(self):
        self.clear(Locators.NAME)
        self.enter_text(Locators.NAME, 'Mohit')

    def mobile(self):
        self.clear(Locators.NUMBER)
        self.enter_text(Locators.NUMBER, '9810981098')

    def email(self):
        self.enter_text(Locators.EMAIL, 'abc@gmail.com')

    def pwd(self):
        self.enter_text(Locators.PASSWORD, 'password')

    def submit(self):
        self.click(Locators.CONTINUE)




