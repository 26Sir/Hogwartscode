#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

class Test_Demo_2():
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps['platformVersion'] = '6.0.1'
        caps["appium:appPackage"] = "io.appium.android.apis"
        caps["appium:appActivity"] = ".ApiDemos"
        caps["appium:deviceName"] = "Sir"
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 36000
        caps["appium:connectHardwareKeyboard"] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
    
    def teardown(self):
        self.driver.quit()
        
    def test_input(self):
        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="OS")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Morse Code")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ID, value="io.appium.android.apis:id/text")
        el3.clear()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="io.appium.android.apis:id/text")
        el4.send_keys("ceshiren.com")
        self.driver.back()
        self.driver.back()
        self.driver.back()
        
# if __main__:
