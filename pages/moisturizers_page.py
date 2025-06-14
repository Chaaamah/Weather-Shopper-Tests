from .base_page import BasePage
from selenium.webdriver.common.by import By
import pytest

class MoisturizersPage(BasePage):
    PRODUCTS = (By.XPATH, "//div[@class='text-center col-4']")
    ADD_BTN = (By.XPATH, ".//button[contains(@class, 'btn-primary')]")
    CART_BTN = (By.ID, "cart")
    
    def add_cheapest_product(self, keyword):
        products = self.get_elements(self.PRODUCTS)
        matching_products = []
        
        for product in products:
            text = product.text
            if keyword.lower() in text.lower():
                # Correction: utiliser l'avant-dernière ligne pour le prix
                price_text = text.splitlines()[-2]  # Ligne modifiée
                price = int(''.join(filter(str.isdigit, price_text)))
                add_btn = product.find_element(*self.ADD_BTN)
                matching_products.append((price, add_btn))
        
        if not matching_products:
            pytest.fail(f"Aucun produit contenant '{keyword}' trouvé")
        
        cheapest = min(matching_products, key=lambda x: x[0])
        cheapest[1].click()
        return cheapest[0]
    
    def go_to_cart(self):
        self.click(self.CART_BTN)