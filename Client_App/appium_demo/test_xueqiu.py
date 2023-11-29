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
        caps["appium:appPackage"] = "com.xueqiu.android"
        caps["appium:appActivity"] = ".view.WelcomeActivityAlias"
        caps["appium:deviceName"] = "Sir"
        # caps["noReset"] = True
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 36000
        caps["appium:connectHardwareKeyboard"] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        #设置隐形等待
        self.driver.implicitly_wait(10)
    
    def teardown(self):
        # pass
        self.driver.quit()
    
    def test_input(self):
        searchbox_ele  = self.driver.find_element(by=AppiumBy.ID,value = 'com.xueqiu.android:id/tv_search')
        searchbox_res = searchbox_ele.is_displayed()
        if searchbox_res is True:
            searchbox_text  = searchbox_ele.text
            searchbox_location  = searchbox_ele.location
            searchbox_size  = searchbox_ele.size
            print(f"搜索框的文本为{searchbox_text}")
            print(f"搜索框的坐标为{searchbox_location}")
            print(f"搜索框的宽高为{searchbox_size}")
            searchbox_ele.click()
            searchbox_ele.send_keys()
        else:
            print("输入框不可用")
            assert  False

# if __main__:
