class InventoryPage:
    def __init__(self, page):
        self.page = page
        self._backpack_add_button = "#add-to-cart-sauce-labs-backpack"
        self._cart_link = ".shopping_cart_link"
        self._cart_item_name = ".inventory_item_name"
        self._page_title = ".title"

    def get_title(self):
        return self.page.locator(self._page_title).text_content()

    def add_backpack_to_cart(self):
        self.page.click(self._backpack_add_button)

    def open_cart(self):
        self.page.click(self._cart_link)

    def get_cart_item_name(self):
        return self.page.locator(self._cart_item_name).text_content()
