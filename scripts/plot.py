import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from tkinter import *
import pandas as pd
import xml.etree.ElementTree as ET


def plot():
    tree = ET.parse('PricePlot_scrapy/output_files/items_processor.xml')
    root = tree.getroot()
    df = pd.DataFrame({'chart_with_prices': range(5),
                       str(root[0].text): (float(root[0][0].text), float(root[0][1].text), float(root[0][2].text),
                                           float(root[0][3].text), float(root[0][4].text)),
                       str(root[1].text): (float(root[1][0].text), float(root[1][1].text), float(root[1][2].text),
                                           float(root[1][3].text), float(root[1][4].text)),
                       str(root[2].text): (float(root[2][0].text), float(root[2][1].text), float(root[2][2].text),
                                           float(root[2][3].text), float(root[2][4].text)),
                       str(root[3].text): (float(root[3][0].text), float(root[3][1].text), float(root[3][2].text),
                                           float(root[3][3].text), float(root[3][4].text)),
                       str(root[4].text): (float(root[4][0].text), float(root[4][1].text), float(root[4][2].text),
                                           float(root[4][3].text), float(root[4][4].text))})
    plt.figure(figsize=(18, 7))
    plt.style.use('seaborn-darkgrid')
    palette = plt.get_cmap('Set1')
    number = 0
    for column in df.drop('chart_with_prices', axis=1):
        number += 1
        plt.plot(df['chart_with_prices'], df[column], marker='.', color=palette(number), linewidth=2, alpha=0.9, label=column)
    plt.legend(loc=2, ncol=3)
    plt.title("Spaghetti plot with price change", loc='left', fontsize=12, fontweight=0, color='black')
    plt.xlabel("Reading")
    plt.ylabel("Price[PLN]")
    plt.show()


if __name__ == "__main__":
    plot()
















    '''
        df = pd.DataFrame({'chart_with_prices': range(1, 5),
                            str(root[0].text): (float(root[0][0].text), float(root[0][1].text), float(root[0][2].text), float(root[0][3].text), float(root[0][4].text), float(root[0][5].text), float(root[0][6].text), float(root[0][7].text), float(root[0][8].text), float(root[0][9].text)),
                            str(root[1].text): (float(root[1][0].text), float(root[1][1].text), float(root[1][2].text), float(root[1][3].text), float(root[1][4].text), float(root[1][5].text), float(root[1][6].text), float(root[1][7].text), float(root[1][8].text), float(root[1][9].text)),
                            str(root[2].text): (float(root[2][0].text), float(root[2][1].text), float(root[2][2].text), float(root[2][3].text), float(root[2][4].text), float(root[2][5].text), float(root[2][6].text), float(root[2][7].text), float(root[2][8].text), float(root[2][9].text)),
                            str(root[3].text): (float(root[3][0].text), float(root[3][1].text), float(root[3][2].text), float(root[3][3].text), float(root[3][4].text), float(root[3][5].text), float(root[3][6].text), float(root[3][7].text), float(root[3][8].text), float(root[3][9].text)),
                            str(root[4].text): (float(root[4][0].text), float(root[4][1].text), float(root[4][2].text), float(root[4][3].text), float(root[4][4].text), float(root[4][5].text), float(root[4][6].text), float(root[4][7].text), float(root[4][8].text), float(root[4][9].text)),
                            str(root[5].text): (float(root[5][0].text), float(root[5][1].text), float(root[5][2].text), float(root[5][3].text), float(root[5][4].text), float(root[5][5].text), float(root[5][6].text), float(root[5][7].text), float(root[5][8].text), float(root[5][9].text)),
                            str(root[6].text): (float(root[6][0].text), float(root[6][1].text), float(root[6][2].text), float(root[6][3].text), float(root[6][4].text), float(root[6][5].text), float(root[6][6].text), float(root[6][7].text), float(root[6][8].text), float(root[6][9].text)),
                            str(root[7].text): (float(root[7][0].text), float(root[7][1].text), float(root[7][2].text), float(root[7][3].text), float(root[7][4].text), float(root[7][5].text), float(root[7][6].text), float(root[7][7].text), float(root[7][8].text), float(root[7][9].text)),
                            str(root[8].text): (float(root[8][0].text), float(root[8][1].text), float(root[8][2].text), float(root[8][3].text), float(root[8][4].text), float(root[8][5].text), float(root[8][6].text), float(root[8][7].text), float(root[8][8].text), float(root[8][9].text)),
                            str(root[9].text): (float(root[9][0].text), float(root[9][1].text), float(root[9][2].text), float(root[9][3].text), float(root[9][4].text), float(root[9][5].text), float(root[9][6].text), float(root[9][7].text), float(root[9][8].text), float(root[9][9].text))})
        '''