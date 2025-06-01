from pages.sunscreens_page import SunscreensPage
from pages.cart_page import CartPage

def test_sunscreens_flow(browser):
    browser.get("https://weathershopper.pythonanywhere.com/sunscreen")
    page = SunscreensPage(browser)
    
    # Recherche par caractéristiques réelles des produits
    spf50_price = page.add_cheapest_product("spf50,spf-50,50,protection")
    spf30_price = page.add_cheapest_product("spf30,spf-30,30,protection")
    
    page.go_to_cart()
    
    cart_page = CartPage(browser)
    prices = cart_page.get_prices()
    total = cart_page.get_total()
    
    assert spf50_price in prices
    assert spf30_price in prices
    assert sum(prices) == total