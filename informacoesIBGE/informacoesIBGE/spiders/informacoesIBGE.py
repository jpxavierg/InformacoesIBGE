import scrapy


class InformacoesIBGESpider(scrapy.Spider):
    name = 'informacoesIBGE'
    uf = str(input("Digite a UF do estado: ")).lower()
    start_urls = [f'https://www.ibge.gov.br/cidades-e-estados/{uf}.html']
    print(start_urls)

    def parse(self, response):
        cont = len(response.css('.ind-label p::text').getall())
        for i in range(cont):
            yield {
                'rotulo': response.css('.ind-label p::text')[i].get(),
                'valor': response.css('.ind-value::text')[i].get()
                }


        pass
