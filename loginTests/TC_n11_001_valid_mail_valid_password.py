#!/usr/bin/python3

# Selenium Task

from time import sleep
from selenium import webdriver
import unittest
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/home/berk/chromedriver/stable/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://www.n11.com/")

        homePage = HomePage(driver=driver)
        homePage.click_login()

        loginPage = LoginPage(driver=driver)
        loginPage.enter_email("berk.akipek.99@gmail.com")
        loginPage.enter_password("ABS2254292asd")
        loginPage.click_login()

        sleep(2)
    

    @classmethod
    def tearDownClass(self):
        print("Test completed")


if __name__ == '__main__':
    unittest.main()

