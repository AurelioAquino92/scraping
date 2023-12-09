import unittest
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

class LoginTestCase(unittest.TestCase):

    browser = Firefox()

    def setUp(self) -> None:
        self.browser.get('http://saucedemo.com')
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()

    def test_valid_login(self):
        campo_input = self.browser.find_element(By.ID, 'user-name')
        campo_input.send_keys('standard_user')
        campo_senha = self.browser.find_element(By.ID, 'password')
        campo_senha.send_keys('secret_sauce')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        botao_login.click()

        label_titulo = self.browser.find_element(By.CLASS_NAME, 'title').text
        self.assertEqual(label_titulo, 'Products')

if __name__ == '__main__':
    unittest.main()