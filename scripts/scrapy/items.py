import scrapy
from itemloaders.processors import MapCompose, TakeFirst


def serialize_price(value):
    return '%s' % str(value)


def serialize_name(value):
    pass


def process_float_or_int(value):
    try:
        return eval(value)
    except:
        return value


class ProcessorItem(scrapy.Item):
    processor_name = scrapy.Field()
    processor_price = scrapy.Field(serialized=float)