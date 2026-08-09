from ui_tests.pages.login_page import LoginPage
from ui_tests.pages.inventory_page import InventoryPage


def test_successful_login(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    assert inventory_page.get_title() == "Products"


def test_failed_login_with_wrong_password(page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("standard_user", "completely_wrong_password")
    
    assert "Username and password do not match any user in this service" in login_page.get_error_message()


def test_add_backpack_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    
    assert inventory_page.get_cart_item_name() == "Sauce Labs Backpack"
