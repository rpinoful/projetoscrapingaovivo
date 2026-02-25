import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"]

    def parse(self, response):
        products = response.css('div.poly-card__content')
        #old_prices = products.css('s.andes-money-amount--previous *::text').getall()
        #current_prices = products.css('div.poly-price__current .andes-money-amount--cents-superscript *::text').getall() #(elementoprincipal.claseelementoprincipal .clase unica do elemento (aquela que contem --))
        
        for product in products:
            old_prices = product.css('s.andes-money-amount--previous *::text').getall()
            current_prices = product.css('div.poly-price__current .andes-money-amount--cents-superscript *::text').getall()
            reviews = product.css('span.poly-component__review-compacted .poly-phrase-label::text').getall()
            
            
            yield{
                    'brand': product.css("span.poly-component__seller span.poly-phrase-label::text").get(),
                    'name': product.css('h3.poly-component__title-wrapper .poly-component__title::text').get(),
                    'old_price': "".join(old_prices).replace("R$", "").replace(",", ".").strip() if old_prices else None,
                    'current_price': "".join(current_prices).replace("R$", "").replace(",", ".").strip() if current_prices else None,
                    'review' : reviews[0] if len(reviews) >=1 and len(reviews[0])==3  else 0 
                
                }
            
            

