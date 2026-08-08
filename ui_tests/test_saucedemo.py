def test_login_saucedemo(page):
    page.goto("https://saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert page.locator(".title").text_content() == "Products"




def test_failed_login_saucedemo(page):
    # 1. Переходим на сайт
    page.goto("https://saucedemo.com")
    
    # 2. Вводим правильный логин, но СЛУЧАЙНЫЙ НЕВЕРНЫЙ пароль
    page.fill("#user-name", "standard_user")
    page.fill("#password", "completely_wrong_password")
    
    # 3. Нажимаем кнопку входа
    page.click("#login-button")
    
    # 4. Находим на странице красную плашку с ошибкой
    error_message = page.locator("[data-test='error']").text_content()
    
    # 5. Проверяем (assert), что текст ошибки содержит информацию о несовпадении данных
    assert "Username and password do not match any user in this service" in error_message
