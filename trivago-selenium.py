import unittest
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

class TrivagoTestCase(unittest.TestCase):

    browser = Firefox()

    def setUp(self) -> None:
        self.browser.get('http://trivago.com.br')
        botaoLinguagem = self.browser.find_element(By.CSS_SELECTOR, "button[data-testid='header-localization-menu']")
        botaoLinguagem.click()

        selecaoLinguagem = self.browser.find_element(By.ID, 'language-select')
        selecaoLinguagem.send_keys('Português')

        botaoSubmit = self.browser.find_element(By.CSS_SELECTOR, "div > button[type='submit']")
        botaoSubmit.click()

        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()

    def test_trivago_info(self):
        campoBusca = self.browser.find_element(By.ID, 'input-auto-complete')
        campoBusca.send_keys('Manaus')
        
        botaoPesquisar = self.browser.find_element(By.CSS_SELECTOR, "button[data-testid='search-button-with-loader']")
        botaoPesquisar.click()
        sleep(2)
        botaoPesquisar.click()
        
        sleep(2)

        ordenador = self.browser.find_element(By.ID, 'sorting-selector')
        ordenador.send_keys('Avaliações e sugestões')

        sleep(2)

        itensEncontrados = self.browser.find_element(By.CSS_SELECTOR, "ol[data-testid='accommodation-list']")
        primeiroItem = itensEncontrados.find_element(By.CSS_SELECTOR, 'l:nth-child(1)')

        print(primeiroItem.find_element(By.CSS_SELECTOR, "span[itemprop='name']").text)

if __name__ == '__main__':
    unittest.main()