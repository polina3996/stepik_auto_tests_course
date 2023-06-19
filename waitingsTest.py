from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin
import time

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    if text:
        browser.find_element(By.ID, 'book').click()

        x = browser.find_element(By.ID, 'input_value').text
        browser.find_element(By.ID, 'answer').send_keys(log(abs(12 * sin(int(x)))))
        browser.find_element(By.ID, 'solve').click()
finally:
    time.sleep(50)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
