from pages.sunscreens_page import SunscreensPage
from pages.cart_page import CartPage

def test_sunscreens_flow(browser):
    browser.get("https://weathershopper.pythonanywhere.com/sunscreen")
    page = SunscreensPage(browser)
    
    # Ajouter les 2 produits requis
    spf50_price = page.add_cheapest_product("spf-50") or page.add_cheapest_product("spf 50")
    spf30_price = page.add_cheapest_product("spf-30") or page.add_cheapest_product("spf 30")
    
    # Aller au panier
    page.go_to_cart()
    
    # Vérifier le total
    cart_page = CartPage(browser)
    prices = cart_page.get_prices()
    total = cart_page.get_total()
    
    assert spf50_price in prices
    assert spf30_price in prices
    assert sum(prices) == total