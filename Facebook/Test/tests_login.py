from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from Facebook.BasicTest.location import *


def test_login_valid_using_correct_userName_and_password(): # correct user and password

    driver = webdriver.Chrome()
    driver.get(facebookWebsite)
    fb_user = driver.find_element(By.XPATH, userName)
    fb_user.send_keys("Shuki Ruki")

    fb_password = driver.find_element(By.XPATH, password)
    fb_password.send_keys("Post567&")
    driver.find_element(By.XPATH, login).click()
    sleep(10)


def test_login_invalid_using_NONE_user_field_and_correct_password():  # incorrect user and correct password

    driver = webdriver.Chrome()
    facebook = driver.get(facebookWebsite)
    q = driver.current_url
    assert q == facebook
    fb_user = driver.find_element(By.XPATH, userName)
    fb_user.send_keys("")
    fb_password = driver.find_element(By.XPATH, password)
    fb_password.send_keys("Post567&")
    driver.find_element(By.XPATH, login).click()
    sleep(5)
    error = driver.find_element(By.XPATH, error_message).text
    assert error == "Find your account and log in."
    sleep(10)
    driver.close()


def test_login_invalid_using_correct_username_and_incorrect_password_invalid_field_none(): #  correct user name  and password
    driver = webdriver.Firefox() # ###
    driver.get(facebookWebsite)
    fb_user = driver.find_element(By.XPATH, userName)
    fb_user.send_keys("Shuki Ruki")
    fb_password = driver.find_element(By.XPATH, password)
    fb_password.send_keys("")
    driver.find_element(By.XPATH, ).click()
    sleep(4)

    error = driver.find_element(By.XPATH, error_message).text
    assert error == " Forgotten password?"
    sleep(10)
    driver.close()


def test_login_invalid_with_both_username_and_password_field_none():# both user and password are incorrect

    driver = webdriver.Chrome()
    driver.get(facebookWebsite)
    fb_user = driver.find_element(By.XPATH, userName)
    fb_user.send_keys("")
    fb_password = driver.find_element(By.XPATH, password)
    fb_password.send_keys("")
    driver.find_element(By.XPATH, login).click()
    sleep(5)
    error = driver.find_element(By.XPATH, error_message).text
    assert error == "Find your account and log in."
    sleep(10)
    driver.close()

def test_login_invalid_using_incorrect_username_and_NONE_password(): # incorrect username and NONE password
    driver = webdriver.Firefox()
    driver.get(facebookWebsite)
    fb_user = driver.find_element(By.XPATH, userName)
    fb_user.send_keys("3456789oi")
    fb_password = driver.find_element(By.XPATH, password)
    fb_password.send_keys("")
    driver.find_element(By.XPATH, ).click()
    sleep(4)

    error = driver.find_element(By.XPATH, error_message).text
    assert error == " Forgotten password?"
    sleep(10)
    driver.close()


def test_login_invalid_with_both_username_and_password_field_are_invalid(): # both_username_and_password_field_are_invalid

    driver = webdriver.Chrome()
    driver.get(facebookWebsite)
    fb_user = driver.find_element(By.XPATH, userName)
    fb_user.send_keys("ertyuio")
    fb_password = driver.find_element(By.XPATH, password)
    fb_password.send_keys("4zxfdtr64")
    driver.find_element(By.XPATH, login).click()
    sleep(5)
    error = driver.find_element(By.XPATH, error_message).text
    assert error == "Find your account and log in."
    sleep(10)
    driver.close()






