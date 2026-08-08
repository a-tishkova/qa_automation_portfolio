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





def test_add_to_cart_saucedemo(page):
    # 1. Авторизуемся на сайте
    page.goto("https://saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    # 2. Нажимаем кнопку "Add to cart" у первого товара (Рюкзак)
    # Кнопка имеет уникальный ID: #add-to-cart-sauce-labs-backpack
    page.click("#add-to-cart-sauce-labs-backpack")
    
    # 3. Переходим в корзину, кликнув по иконке корзины вверху справа
    page.click(".shopping_cart_link")
    
    # 4. Проверяем (assert), что в корзине лежит именно рюкзак
    # Ищем элемент названия товара на странице корзины
    assert page.locator(".inventory_item_name").text_content() == "Sauce Labs Backpack"
