import scrapy


class InformacoesIBGESpider(scrapy.Spider):
    name = 'informacoesIBGE'
    uf = str(input("Digite a UF do estado: ")).lower()
    start_urls = [f'https://www.ibge.gov.br/cidades-e-estados/{uf}.html']
    print(start_urls)

    def parse(self, response):
        #(-1) porque o Python inicia com 0 (0 até 11 --> 12 execuções)
        cont = len(response.css('.ind-label p::text').getall()) - 1
        i = 0
        while i <= cont:
            yield {
                'rotulo': response.css('.ind-label p::text')[i].get(),
                'valor': response.css('.ind-value::text')[i].get()
                }
            i += 1

        pass
