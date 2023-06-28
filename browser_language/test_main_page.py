import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_button(browser):
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "btn-add-to-basket"), 'Кнопки добавления в корзину нет'
    time.sleep(5)

def test_guest_can_go_to_login_page(browser):
    link2 = "http://selenium1py.pythonanywhere.com/"
    browser.get(link2)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()