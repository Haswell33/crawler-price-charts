import sys
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    exec(open('xml_parse.py').read())
    exec(open('plot.py').read())


if __name__ == '__main__':
    main()























#script_descriptor = open("ProcessorSpider_runner.py")
    #a_script = script_descriptor.read()
    #sys.argv = ["ProcessorSpider_runner.py", y]
    #exec(a_script)