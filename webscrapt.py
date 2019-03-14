#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:48:50 2019

@author: kia
"""

import time
from selenium import webdriver
from termcolor import colored
from os import system

url = 'http://www.appstehran.com/LoginProfile.aspx'
username = '*********'
password = '************' 

driver = webdriver.Chrome('/home/kia/Downloads/chromedriver')

while True:
    driver.get(url)
    print(colored('loadSite','red'))
    driver.find_element_by_xpath('//*[@id="ctl00_txtUsername"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="ctl00_txtPassword"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="ctl00_btnLogin"]').click()
    print(colored('complate inputs','red'))
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder3_btnEntekhabvahed"]').click()
    print(colored('waiting 60 second...','red'))
    time.sleep(70)
    status = driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td').text
    time.sleep(1)
    print(status)
    if status != "زمان نوبت دهی به پایان رسیده است":
        system('cvlc win.wav &')
    driver.close()
    time.sleep(600)
