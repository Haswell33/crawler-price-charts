import scrapy

x = -1


def count_element_price():
    global x
    x = x + 1
    return x


class ProcessorSpider(scrapy.Spider):
    name = "ProcessorSpider"
    allowed_domains = ["morele.net"]

    start_urls = [
        'https://www.morele.net/kategoria/procesory-45/,,,,,15,,,0,,,,/1/'
    ]

    def parse(self, response):
        for selector in response.css('div.cat-product.card'):
            processor_name = selector.css('div.cat-product.card').attrib['data-product-name']
            processor_price = selector.css('div.cat-product.card').attrib['data-product-price']

            yield {
                'Model': processor_name,
                'Price' + str(count_element_price()) + '': processor_price,
            }















# process = CrawlerProcess({
   #     'FEED_FORMAT': 'xml',
   #     'FEED_URI': 'testtttttt.xml'
   # })

    #custom_settings = {
   #     'FEED_EXPORT_BATCH_ITEM_COUNT': 10,
    #    'FEEDS': {
   #         'page-%(batch_id)d.xml': {
   #             'format': 'xml',
   #         }
   #     }
   # }