from .base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    ITEM_PRICES = (By.XPATH, "//tbody/tr/td[2]")
    TOTAL = (By.XPATH, "//p[@id='total']")
    
    def get_prices(self):
        prices = []
        elements = self.get_elements(self.ITEM_PRICES)
        for el in elements:
            price_text = el.text
            prices.append(int(''.join(filter(str.isdigit, price_text))))
        return prices
    
    def get_total(self):
        total_text = self.get_text(self.TOTAL)
        return int(''.join(filter(str.isdigit, total_text)))