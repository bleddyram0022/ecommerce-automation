import pytest
from selenium import webdriver
from PageObjects.LoginPage import login
from selenium.webdriver.common.by import By
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_Login:
    baseURL  = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password  = ReadConfig.getPassword()

    logger =LogGen.loggen()

#Terminal Run Command pytest -v -s C:\Users\USER\PycharmProjects\ECommerce\TestCases\test_login.py
    def test_homePageTitle(self,setup):

        self.logger.info("*************** Test_001_Login ***************")
        self.logger.info("************Verifying Home Page Title ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************ Home Page Title is Passed ***************")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************ Home Page Title is failed ***************")
            assert False


    def test_loginpage(self, setup):

        self.logger.info("*************** Test_001_Login ***************")
        self.logger.info("************Verifying Dashboard Page Title ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = login(self.driver)
        self.lp.setuserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("************ Home Page Title is Passed ***************")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_loginpage.png")
            self.driver.close()
            self.logger.error("************ Dashboard Page Title is failed ***************")
            assert False

