from selenium.webdriver.common.by import By
from selenium import webdriver


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[value='Log In']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")