from selenium.webdriver.common.by import By

class Locators():
    #--------Home Page Locators--------
    SIGN_IN =(By.ID,'nav-link-accountList')
    RE_ORDERS =(By.ID,'nav-orders')
    SEARCH_BOX = (By.ID,'twotabsearchtextbox')
    SEARCH_ICON = (By.XPATH,'//input[@value="Go"]')
    LANG_ICON = (By.XPATH,'//a[@id="icp-nav-flyout"]')
    BROWSING_HISTORY = (By.XPATH,'//*[@id="nav-xshop"]/a[7]')
    CART = (By.XPATH, '//*[@id="nav-cart"]')
    LOGOUT = (By.XPATH,'//*[@id="nav-item-signout"]/span')
    ADDRESS_ICON = (By.XPATH, '//*[@id="nav-global-location-slot"]/span/a')
    ADDRESS = ("//*[@deliverydestinationtype='CUSTOMER_ADDRESS']")
    SWITCH_ACCOUNTS = (By.XPATH, '//*[@id="nav-item-switch-account"]/span')



