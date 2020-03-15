from selenium import webdriver
from PageObject.Locators.HomepageLoc import Locators
from Testbase.test_base import BasePage


class Homepage(BasePage):
    def langclick(self):
        self.click(Locators.LANG_ICON)

    def searchitem(self):
        self.enter_text(Locators.SEARCH_BOX, 'Mobile')
        self.click(Locators.SEARCH_ICON)

    def bwh(self):
        self.click(Locators.BROWSING_HISTORY)

    def removeitem(self):
        self.click(Locators.CART)

    def cartvalue(self):
        self.click(Locators.CART)

    def logout(self):
        self.hover_to(Locators.SIGN_IN)
        self.click(Locators.LOGOUT)

    def selectaddress(self):
        self.click(Locators.ADDRESS_ICON)

    def displayalladdress(self):
        return self.elements(Locators.ADDRESS)
