from .base_page import BasePage  # Ajout de l'import manquant
from selenium.webdriver.common.by import By

class HomePage(BasePage):  # BasePage est maintenant importé
    TEMPERATURE = (By.ID, "temperature")
    MOISTURIZERS_BTN = (By.XPATH, "//button[contains(.,'Buy moisturizers')]")  # Texte corrigé
    SUNSCREENS_BTN = (By.XPATH, "//button[contains(.,'Buy sunscreens')]")  # Texte corrigé
    
    def get_temperature(self):
        temp_text = self.get_text(self.TEMPERATURE)
        return int(''.join(filter(str.isdigit, temp_text)))
    
    def go_to_moisturizers(self):
        self.click(self.MOISTURIZERS_BTN)
    
    def go_to_sunscreens(self):
        self.click(self.SUNSCREENS_BTN)