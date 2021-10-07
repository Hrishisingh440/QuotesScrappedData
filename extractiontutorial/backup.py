import scrapy
from scrapy.http import FormRequest
from ..items import ExtractiontutorialItem
class QuotesSpider(scrapy.Spider):
    name='quotes'
    pagenumber=2
    start_urls = [
        'http://quotes.toscrape.com/login'

    ]
    def parse(self, response):
        token=response.css('form input::attr(value)').extract()
        return FormRequest.from_response(response,formdata={
            'csrf_token':token,
            'username':'hrishikeshkumar440@gmail.com'
            'password':'hrishi123'
        }callback=self.start_scrapping)
    def start_scrapping(self,response):
        items = ExtractiontutorialItem()
        for quote in response.css('div.quote'):

            title = quote.css('span.text::text').extract()
            author = quote.css('small.author::text').extract()
            tags = quote.css('div.tags a.tag::text').extract()
            items['title'] = title
            items['author'] = author
            items['tag'] = tags
            yield items
            next_page = 'http://quotes.toscrape.com/page/' + str(QuotesSpider.pagenumber) + '/'
            if QuotesSpider.pagenumber <= 11:
                QuotesSpider.pagenumber += 1

                yield response.follow(next_page, callback=self.parse)
