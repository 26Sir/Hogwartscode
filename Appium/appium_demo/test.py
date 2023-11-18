# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "Android"
caps['platformVersion']='6.0.1'
caps["appium:appPackage"] = "io.appium.android.apis"
caps["appium:appActivity"] = ".ApiDemos"
caps["appium:deviceName"] = "Sir"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 36000
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
# webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="OS")
el1.click()
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Morse Code")
el2.click()
el3 = driver.find_element(by=AppiumBy.ID, value="io.appium.android.apis:id/text")
el3.clear()
el4 = driver.find_element(by=AppiumBy.ID, value="io.appium.android.apis:id/text")
el4.send_keys("ceshiren.com")
driver.back()
driver.back()
driver.back()

driver.quit()