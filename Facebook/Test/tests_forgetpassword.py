from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from Facebook.BasicTest.location import *


def test_valid_forgetpassword():
    driver = webdriver.Chrome()
    driver.get(facebookWebsite)
    driver.find_element(By.XPATH, "//a[contains(text(),'Forgotten password?')]").click()

    driver.find_element(By.XPATH, "//input[@id='identify_email']").click()
    fb_recover = driver.find_element(By.XPATH, "//input[@id='identify_email']")
    fb_recover.send_keys("example@gmail.com")
    driver.find_element(By.XPATH, "//button[@id='did_submit']").click()
    sleep(5)
    driver.close()


def test_invalid_forgetpassword_incorrect_gmail():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    driver.find_element(By.XPATH, "//a[contains(text(),'Forgotten password?')]").click()

    driver.find_element(By.XPATH, "//input[@id='identify_email']").click()
    fb_recover = driver.find_element(By.XPATH, "//input[@id='identify_email']")
    fb_recover.send_keys("examplegmail.com")
    driver.find_element(By.XPATH, "//button[@id='did_submit']").click()
    sleep(5)
    driver.close()

def test_invalid_forgetpassword_NONE_gmail():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    driver.find_element(By.XPATH, "//a[contains(text(),'Forgotten password?')]").click()

    driver.find_element(By.XPATH, "//input[@id='identify_email']").click()
    fb_recover = driver.find_element(By.XPATH, "//input[@id='identify_email']")
    fb_recover.send_keys("")
    driver.find_element(By.XPATH, "//button[@id='did_submit']").click()
    sleep(5)
    driver.close()


