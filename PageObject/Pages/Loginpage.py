from selenium import webdriver
from PageObject.Locators.LoginpageLoc import Locators
from Testbase.test_base import BasePage
from Datareader.Registration_Iterator import Registration


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

    def addaccount(self):
        self.click(Locators.ADD_ACCOUNT)

    def createaccount(self):
        self.click(Locators.CREATE_ACCOUNT)

    def name(self,i):
        self.clear(Locators.NAME)
        self.enter_text(Locators.NAME,Registration.yourname(self,i))

    def cell(self,i):
        self.clear(Locators.NUMBER)
        self.enter_text(Locators.NUMBER,Registration.mobile(self,i))

    def email(self,i):
        self.clear(Locators.EMAIL)
        self.enter_text(Locators.EMAIL, Registration.email(self, i))

    def pwd(self,i):
        self.clear(Locators.PASSWORD)
        self.enter_text(Locators.PASSWORD, Registration.password(self,i))

