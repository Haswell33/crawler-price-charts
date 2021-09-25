from scrapy import cmdline
import os
import sys


def ProcessorSpider_runner(x):
    if os.path.exists('output_files/graphic_cards_output_'+str(x)+'.xml'):
        os.remove('output_files/graphic_cards_output_'+str(x)+'.xml')
    cmdline.execute(['scrapy', 'crawl', 'GraphicCardSpider', '-o', 'PricePlot_scrapy/output_files/graphic_cards_output_'+str(x)+'.xml'])


if __name__ == '__main__':
    ProcessorSpider_runner(sys.argv[1])