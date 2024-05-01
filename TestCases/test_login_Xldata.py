import pytest
from selenium import webdriver
from PageObjects.LoginPage import login
from selenium.webdriver.common.by import By
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils
import time

class Test_001_XLdata_Login:
    baseURL  = ReadConfig.getApplicationURL()
    path="//.TestData//LoginData.xlsx"

    logger =LogGen.loggen()


    def test_loginpage(self, setup):

        self.logger.info("*************** Test_001_XLdata_Login ***************")
        self.logger.info("************ Verifying Dashboard Page Title ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = login(self.driver)

        self.rows = XLUtils.getrowCount(self.path,'sheet1')
        print("Number of Rows i a Excel:",self.rows)

        for r in range(2,self.rows+1):
            self.Username = XLUtils.readData(self.path, 'sheet1', r, 1)
            self.Password = XLUtils.readData(self.path, 'sheet1', r, 2)
            self.Result   = XLUtils.readData(self.path, 'sheet1', r, 3)

            self.lp.setuserName(self.Username)
            self.lp.setPassword(self.Password)
            self.lp.clickLogin()
            time.sleep(5)



