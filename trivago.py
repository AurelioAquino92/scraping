from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("http://www.trivago.com.br")
    pagina.locator('#input-auto-complete').click()
    pagina.fill('#input-auto-complete', "Manaus")
    pagina.locator('//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div[2]/div/div/form/div[3]/button/span').click()
    pagina.locator('//*[@id="__next"]/div[1]/main/div[1]/div[4]/div/form/div[4]/div/div/div[2]/div/div[1]/button').click()
    pagina.locator('//*[@id="sorting-selector"]')
    pagina.select_option(label='Avaliação e sugestões')
    nome = pagina.locator('#__next > div.min-w-screen-3xs.text-grey-900 > main > div.relative > section > div > ol > li:nth-child(1) > div > article > div.flex.flex-grow-1.justify-between.accomodation-item_infoSection__jtzM6.flex-1 > div.px-2.w-1\/2.flex-1.mt-2.mb-3 > section > h2').all_text_contents()
    valor = pagina.locator('//*[@id="__next"]/div[1]/main/div[5]/section/div/ol/li[1]/div/article/div[2]/div[2]/div[2]/div/div/div/div[2]').all_text_contents()
    avaliacao = pagina.locator('//*[@id="__next"]/div[1]/main/div[5]/section/div/ol/li[1]/div/article/div[2]/div[1]/div[3]/button/span[1]/span/span[1]').all_text_contents()


    print("O melhor hotel encontrado foi: %s" % (nome))
    print("A diária custa: %s" %(valor))
    print("Com a nota: %s" % (avaliacao))
