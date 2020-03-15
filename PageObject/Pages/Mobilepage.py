from selenium import webdriver
from PageObject.Locators.MobileLoc import Locators
from Testbase.test_base import BasePage

class Mobilepage(BasePage):
    def mobileclick(self):
        self.click(Locators.Mobile)

    def hoveronmobile(self):
        self.hover_to(Locators.MandA)

    def searchmobie(self):
        self.click(Locators.GB128)
        self.click(Locators.gbRAM4)
        self.click(Locators.gbRAM4)
        self.click(Locators.Item)

    def clickapple(self):
        self.click(Locators.apple)


