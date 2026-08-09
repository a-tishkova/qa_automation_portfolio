class LoginPage:
    def __init__(self, page):
        self.page = page
        self._username_input = "#user-name"
        self._password_input = "#password"
        self._login_button = "#login-button"
        self._error_container = "[data-test='error']"

    def navigate(self):
        self.page.goto("https://saucedemo.com")

    def login(self, username, password):
        self.page.fill(self._username_input, username)
        self.page.fill(self._password_input, password)
        self.page.click(self._login_button)

    def get_error_message(self):
        return self.page.locator(self._error_container).text_content()
