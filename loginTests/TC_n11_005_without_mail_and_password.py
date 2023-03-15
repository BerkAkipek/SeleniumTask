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
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="/home/berk/chromedriver/stable/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    

    def test_without_mail_and_password(self):
        driver = self.driver
        driver.get("https://www.n11.com/")

        homePage = HomePage(driver=driver)
        homePage.click_login()

        loginPage = LoginPage(driver=driver)
        loginPage.click_login()

        message01 = loginPage.return_empty_mail_error_text()
        message02 = loginPage.return_empty_password_error_text()

        assert "Lütfen e-posta adresinizi girin." in message01
        assert "Bu alanın doldurulması zorunludur." in message02


    @classmethod
    def tearDownClass(self) -> None:
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()
