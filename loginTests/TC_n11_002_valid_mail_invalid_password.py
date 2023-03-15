#!/usr/bin/python3

# Selenium Task

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/home/berk/chromedriver/stable/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    

    def test_login_with_invalid_password(self):
        driver = self.driver
        driver.get("https://www.n11.com/")

        homePage = HomePage(driver=driver)
        homePage.click_login()

        loginPage = LoginPage(driver=driver)
        loginPage.enter_email("berk.akipek.99@gmail.com")
        loginPage.enter_password("asdasdfasdasdasdasd")
        loginPage.click_login()

        message = loginPage.return_invalid_password_text()
        assert "Girilen değer en fazla 15 karakter olmalıdır." in message

    @classmethod
    def tearDownClass(self):
        print("Test Finished")


if __name__ == '__main__':
    unittest.main()