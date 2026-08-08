def test_successful_login(page):
    page.goto("https://saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert page.locator(".title").text_content() == "Products"


def test_failed_login_with_wrong_password(page):
    page.goto("https://saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "completely_wrong_password")
    page.click("#login-button")
    
    error_message = page.locator("[data-test='error']").text_content()
    assert "Username and password do not match any user in this service" in error_message


def test_add_backpack_to_cart(page):
    page.goto("https://saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    assert page.locator(".inventory_item_name").text_content() == "Sauce Labs Backpack"
