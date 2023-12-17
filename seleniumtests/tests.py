import unittest
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

class NavigationTestCases(unittest.TestCase):

    browser = Firefox()

    def setUp(self) -> None:
        self.browser.get('http://saucedemo.com')
        campo_input = self.browser.find_element(By.ID, 'user-name')
        campo_input.send_keys('standard_user')
        campo_senha = self.browser.find_element(By.ID, 'password')
        campo_senha.send_keys('secret_sauce')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        botao_login.click()
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()

    def test_home_page_ct_2_3(self):
        menuBtn = self.browser.find_element(By.ID, 'react-burger-menu-btn')
        menuBtn.click()

        allItemsLink = self.browser.find_element(By.ID, 'inventory-sidebar-link')
        allItemsLink.click()

        titleText = self.browser.find_element(By.ID, 'title').text

        self.assertEqual(titleText, 'Products')

class ShoppingCartTestCases(unittest.TestCase):
    
    browser = Firefox()

    def setUp(self) -> None:
        self.browser.get('http://saucedemo.com')
        campo_input = self.browser.find_element(By.ID, 'user-name')
        campo_input.send_keys('standard_user')
        campo_senha = self.browser.find_element(By.ID, 'password')
        campo_senha.send_keys('secret_sauce')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        botao_login.click()
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()

    def test_3_items_ct_3_1(self):
        product1 = self.browser.find_element(By.CSS_SELECTOR, '#inventory_container > div > div:nth-child(1)')
        product1.find_element(By.CLASS_NAME, 'btn').click()
        product2 = self.browser.find_element(By.CSS_SELECTOR, '#inventory_container > div > div:nth-child(2)')
        product2.find_element(By.CLASS_NAME, 'btn').click()
        product3 = self.browser.find_element(By.CSS_SELECTOR, '#inventory_container > div > div:nth-child(3)')
        product3.find_element(By.CLASS_NAME, 'btn').click()

        productCount = self.browser.find_element(By.CLASS_NAME, 'shopping_cart_badge')
        self.assertEqual(productCount.text, '3')
    
    def test_remove_item_ct_3_2(self):
        product1 = self.browser.find_element(By.CSS_SELECTOR, '#inventory_container > div > div:nth-child(3)')
        product1.find_element(By.CLASS_NAME, 'btn').click()

        productCount = self.browser.find_element(By.CLASS_NAME, 'shopping_cart_badge')
        self.assertEqual(productCount.text, '2')
    
    def test_total_price_ct_3_3(self):
        product1 = self.browser.find_element(By.CSS_SELECTOR, '#inventory_container > div > div:nth-child(1)')
        price1 = product1.find_element(By.CLASS_NAME, 'inventory_item_price').text
        product2 = self.browser.find_element(By.CSS_SELECTOR, '#inventory_container > div > div:nth-child(2)')
        price2 = product2.find_element(By.CLASS_NAME, 'inventory_item_price').text

        total = float(price1.replace('$', '')) + float(price2.replace('$', ''))

        shoppingCartBtn = self.browser.find_element(By.CLASS_NAME, 'shopping_cart_link')
        shoppingCartBtn.click()
        
        checkoutBtn = self.browser.find_element(By.ID, 'checkout')
        checkoutBtn.click()

        firstNameInput = self.browser.find_element(By.ID, 'first-name')
        firstNameInput.send_keys('a')
        lastNameInput = self.browser.find_element(By.ID, 'last-name')
        lastNameInput.send_keys('a')
        zipCodeInput = self.browser.find_element(By.ID, 'postal-code')
        zipCodeInput.send_keys('0')
        continueBtn = self.browser.find_element(By.ID, 'continue')
        continueBtn.click()

        calculatedTotal = self.browser.find_element(By.CLASS_NAME, 'summary_subtotal_label').text

        self.assertEqual(calculatedTotal, 'Item total: $' + str(total))

    def test_empty_shopping_cart_ct_3_4(self):
        cancelBtn = self.browser.find_element(By.ID, 'cancel')
        cancelBtn.click()
        product1 = self.browser.find_element(By.CSS_SELECTOR, '#inventory_container > div > div:nth-child(1)')
        product1.find_element(By.CLASS_NAME, 'btn').click()
        product2 = self.browser.find_element(By.CSS_SELECTOR, '#inventory_container > div > div:nth-child(2)')
        product2.find_element(By.CLASS_NAME, 'btn').click()

        shoppingCartBtn = self.browser.find_element(By.CLASS_NAME, 'shopping_cart_link')
        shoppingCartBtn.click()
        
        checkoutBtn = self.browser.find_element(By.ID, 'checkout')
        checkoutBtn.click()

        firstNameInput = self.browser.find_element(By.ID, 'first-name')
        firstNameInput.send_keys('a')
        lastNameInput = self.browser.find_element(By.ID, 'last-name')
        lastNameInput.send_keys('a')
        zipCodeInput = self.browser.find_element(By.ID, 'postal-code')
        zipCodeInput.send_keys('0')
        continueBtn = self.browser.find_element(By.ID, 'continue')
        continueBtn.click()

        finishBtn = self.browser.find_element(By.ID, 'finish')
        finishBtn.click()

        message = self.browser.find_element(By.CLASS_NAME, 'title').text

        self.assertNotEqual(message, 'Checkout: Complete!')

class LogoutTestCases(unittest.TestCase):
    
    browser = Firefox()

    def setUp(self) -> None:
        self.browser.get('http://saucedemo.com')
        campo_input = self.browser.find_element(By.ID, 'user-name')
        campo_input.send_keys('standard_user')
        campo_senha = self.browser.find_element(By.ID, 'password')
        campo_senha.send_keys('secret_sauce')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        botao_login.click()
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()

    def test_logout_ct_5_1(self):
        menuBtn = self.browser.find_element(By.ID, 'react-burger-menu-btn')
        menuBtn.click()

        logoutLink = self.browser.find_element(By.ID, 'logout-sidebar-link')
        logoutLink.click()

        title = self.browser.find_element(By.CLASS_NAME, 'login_logo').text
        
        self.assertEqual(title, 'Swag Labs')


if __name__ == '__main__':
    unittest.main()