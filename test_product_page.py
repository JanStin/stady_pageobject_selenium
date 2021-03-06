from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('promo_pffer', ['0', '1', '2', '3', '4', '5', '6', 
    pytest.param(7, marks=pytest.mark.xfail), 
    '8', '9'])
def test_guest_can_add_product_to_basket(browser, promo_pffer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_pffer}"
    page = ProductPage(browser, link)
    page.open()
    page.can_add_product_to_basket()
