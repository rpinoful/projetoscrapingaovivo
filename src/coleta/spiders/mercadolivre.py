import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"]
    page_count = 1
    max_page =10
    
    def parse(self, response): 
        products = response.css('div.poly-card__content')
        
        
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
        
    
        if self.page_count < self.max_page:
            self.page_count += 1
            offset = (self.page_count - 1) * 48 + 1
            next_page = f"https://lista.mercadolivre.com.br/tenis-corrida-masculino_Desde_{offset}_NoIndex_True"
            yield scrapy.Request(url=next_page, callback=self.parse)    
            
            



