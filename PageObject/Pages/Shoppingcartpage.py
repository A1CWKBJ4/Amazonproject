from selenium import webdriver
from PageObject.Locators.HomepageLoc import Locators
from PageObject.Locators.ShoppingcartLoc import Locators
from Testbase.test_base import BasePage

class Shoppingcart(BasePage):
    def deleteitem(self):
        self.click(Locators.DELETE)

    def logout(self):
        self.click(Locators.LOGOUT)

    def allelements(self):
        return self.elements(Locators.DEL)





