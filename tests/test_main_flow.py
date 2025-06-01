from pages.homepage import HomePage
import pytest

def test_temperature_redirection(browser):
    browser.get("https://weathershopper.pythonanywhere.com/")
    homepage = HomePage(browser)
    temp = homepage.get_temperature()
    
    if temp < 19:
        homepage.go_to_moisturizers()
        assert "moisturizer" in browser.current_url
    elif temp > 34:
        homepage.go_to_sunscreens()
        assert "sunscreen" in browser.current_url
    else:
        pytest.skip("Température dans la plage normale")