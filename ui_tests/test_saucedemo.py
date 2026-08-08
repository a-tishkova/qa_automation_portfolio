def test_login_saucedemo(page):
    page.goto("https://saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert page.locator(".title").text_content() == "Products"
