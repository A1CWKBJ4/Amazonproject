from selenium import webdriver

def takescreenshot(driver, name):
    driver.get_screenshot_as_file('C:/Users/LADDUGOPAL/PycharmProjects/AmazonA/Snapshots/' + name + '.png')

