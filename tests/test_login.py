import allure
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait


@allure.feature("Login")
@allure.story("Valid Login")
def test_valid_login(driver):
    login = LoginPage(driver)
    login.load()

    login.login("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(
        lambda d: "inventory" in d.current_url
    )

    assert "inventory" in driver.current_url


@allure.feature("Login")
@allure.story("Invalid Login")
def test_invalid_login(driver):
    login = LoginPage(driver)
    login.load()

    login.login("invalid_user", "wrong_password")

    WebDriverWait(driver, 10).until(
        lambda d: "Epic sadface" in d.page_source
    )

    assert "Epic sadface" in driver.page_source

def test_add_to_cart(driver):
    login = LoginPage(driver)
    login.load()

    login.login("standard_user", "secret_sauce")

    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    cart = driver.find_element("class name", "shopping_cart_badge").text

    assert cart == "1"