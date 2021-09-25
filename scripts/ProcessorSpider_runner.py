from scrapy import cmdline
import os
import sys

import scrapy


def ProcessorSpider_runner(x):
    if os.path.exists('output_files/processors_output_'+str(x)+'.xml'):
        os.remove('output_files/processors_output_'+str(x)+'.xml')
    cmdline.execute(['scrapy', 'crawl', 'ProcessorSpider', '-o', 'PricePlot_scrapy/output_files/processors_output_'+str(x)+'.xml'])


if __name__ == '__main__':
    ProcessorSpider_runner(sys.argv[1])