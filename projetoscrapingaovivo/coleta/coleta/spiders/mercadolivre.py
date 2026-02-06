import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"]

    def parse(self, response):
        products = response.css('div.poly-card__content')
        
        
        for product in products:
            yield{
                
                    'brand': product.css("span.poly-component__seller span.poly-phrase-label::text").get()
                
                }
