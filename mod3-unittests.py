import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        input1 = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        input3.send_keys("ivanoviv@gmail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # успеваем скопировать код за 30 секунд
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_abs2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        input1 = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        input3.send_keys("ivanoviv@gmail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # успеваем скопировать код за 30 секунд
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
