import scrapy

x = -1


def count_element_price():
    global x
    x = x + 1
    return x


class GraphicCardSpider(scrapy.Spider):
    name = "GraphicCardSpider"
    allowed_domains = ["morele.net"]

    start_urls = [
        'https://www.morele.net/kategoria/karty-graficzne-12/,,,,,,,,0,,,,8144O971250,8143O!2835/1/'
    ]

    def parse(self, response):
        for selector in response.css('div.cat-product.card'):
            graphic_card_name = selector.css('div.cat-product.card').attrib['data-product-name']
            graphic_card_price = selector.css('div.cat-product.card').attrib['data-product-price']

            yield {
                'Model': graphic_card_name,
                'Price' + str(count_element_price()) + '': graphic_card_price,
            }
