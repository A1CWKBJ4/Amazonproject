from selenium.webdriver.common.by import By


class Locators():
    SIGN_IN = (By.ID, 'nav-link-accountList')
    PHONE = (By.ID, 'ap_email')
    CONTINUE = (By.ID, 'continue')
    PASSWORD = (By.ID, 'ap_password')
    SUBMIT = (By.ID, 'signInSubmit')
    NAME = (By.ID, 'ap_customer_name')
    NUMBER = (By.ID, 'ap_phone_number')
    EMAIL = (By.ID, 'ap_email')
    ERROR = (By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div/div[1]/div/div/h4')
