import scrapy
from ..items import ExtractiontutorialItem
class QuotesSpider(scrapy.Spider):
    name='quotes'
    pagenumber=2
    start_urls = [
        'http://quotes.toscrape.com/page/1/'

    ]

    def parse(self, response):

        items=ExtractiontutorialItem()
        for quote in response.css('div.quote'):

                title= quote.css('span.text::text').extract()
                author= quote.css('small.author::text').extract()
                tags=quote.css('div.tags a.tag::text').extract()
                items['title']=title
                items['author']=author
                items['tag']=tags
                yield items
                next_page='http://quotes.toscrape.com/page/'+str(QuotesSpider.pagenumber)+'/'
                if QuotesSpider.pagenumber<=11 :
                    QuotesSpider.pagenumber+=1

                    yield response.follow(next_page,callback=self.parse)

