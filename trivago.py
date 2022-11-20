from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    navegador = p.firefox.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("http://www.trivago.com.br")
    
    pagina.fill('#input-auto-complete', "Manaus")
    pagina.wait_for_timeout(2000)
    pagina.click('[data-testid="search-button"]')

    pagina.select_option('#sorting-selector', label="Avaliação e sugestões")
    item = pagina.query_selector('[data-testid="accommodation-list-element"]')
    assert item == None

    nome = item.query_selector('[itemprop="name"]').inner_text()
    valores = item.query_selector_all('strong')
    avaliacao = item.query_selector('[itemprop="ratingValue"]').inner_text()

    print("O melhor hotel encontrado foi: %s" % (nome))
    for valor in valores:
        print("A diária custa: %s" %(valor.inner_text()))
    print("Com a nota: %s" % (avaliacao))
