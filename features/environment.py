from selenium import webdriver
import time

def before_scenario(context, scenario):
    device = {"deviceName": "iPhone 16"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", device)
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        time.sleep(2)
        context.driver.quit()