import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_button(browser):
    browser.get(link)
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket"), 'Кнопки добавления в корзину нет'
    time.sleep(30)