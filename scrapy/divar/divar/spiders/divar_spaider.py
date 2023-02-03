import scrapy
url ='https://divar.ir/v/-/{token}'

token_file = open('C:\pp\scrapy\divar\divar\spiders\/tokens.txt','r',encoding='utf8')
tokens= token_file.read().split(',')
token_file.close()

class DivarSpider(scrapy.Spider):
    name='divar'
    start_urls=[url.format(token=token) for token in tokens]
    
    def parse(self,response):
        information=response.css('div span.kt-group-row-item__value::text')
        area=information[0].extract()
        constracttion =information[1].extract()
        
        # address=response.ccs('div div.kt-page-title__subtitle--responsive-sized::text').extract()
        # price = response.css('div p.kt-unexpandable-row__value , .kt-page-title__subtitle--responsive-sized::text').extract()
        
        yield{
            'Area':area,
            'Cons':constracttion,
            # 'addr':address,
            # 'price':price,
        }