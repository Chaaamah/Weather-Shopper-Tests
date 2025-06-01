from pages.moisturizers_page import MoisturizersPage
from pages.cart_page import CartPage

def test_moisturizers_flow(browser):
    browser.get("https://weathershopper.pythonanywhere.com/moisturizer")
    page = MoisturizersPage(browser)
    
    # Ajouter les 2 produits requis
    aloe_price = page.add_cheapest_product("aloe")
    almond_price = page.add_cheapest_product("almond")
    
    # Aller au panier
    page.go_to_cart()
    
    # Vérifier le total
    cart_page = CartPage(browser)
    prices = cart_page.get_prices()
    total = cart_page.get_total()
    
    assert aloe_price in prices
    assert almond_price in prices
    assert sum(prices) == total