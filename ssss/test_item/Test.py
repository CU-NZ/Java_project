#coding=utf-8
import time

from selenium import webdriver
import unittest, os

class TestItem(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    #登录
    def test1_select(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("#change_margin_1 > input").clear()
        driver.find_element_by_css_selector("#change_margin_1 > input").send_keys("test")
        driver.find_element_by_css_selector("#change_margin_2 > input").clear()
        driver.find_element_by_css_selector("#change_margin_2 > input").send_keys("123")
        driver.find_element_by_css_selector("#change_margin_3 > input").click()
        driver.implicitly_wait(30)
        time.sleep(2)

        driver.quit()
    #注册
    def test2_insert(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("body > div > div:nth-child(5) > a").click()
        driver.implicitly_wait(30)
        time.sleep(2)

        driver.find_element_by_css_selector("#change_margin_1 > input").clear()
        driver.find_element_by_css_selector("#change_margin_1 > input").send_keys("abc")
        driver.find_element_by_css_selector("#change_margin_2 > input").clear()
        driver.find_element_by_css_selector("#change_margin_2 > input").send_keys("123")
        driver.find_element_by_css_selector("#change_margin_3 > input").click()

        driver.quit()

    #跳转超链接1
    def test3_URL(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("body > div > div:nth-child(6) > li:nth-child(1) > a > span").click()
        driver.implicitly_wait(100)
        time.sleep(5)

        driver.quit()

    #跳转超链接2
    def test4_URL(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("body > div > div:nth-child(6) > li:nth-child(2) > a > span").click()
        driver.implicitly_wait(300)
        time.sleep(5)

        driver.quit()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
