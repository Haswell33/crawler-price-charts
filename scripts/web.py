#inactive
from flask import Flask, request, url_for, redirect, render_template
import json
import time

ChartApp = Flask(__name__)


@ChartApp.route("/")
def index():

    return render_template('index.html')


@ChartApp.route("/processors")
def processors():
    if request.method == 'POST':
        return redirect(url_for('index'))

    with open('ProcessorSpider/output_test.xml', 'r') as output_file:
        data = json.load(output_file)

    #with open('ProcessorSpider/output20.json', 'r') as output_file:
    #     data = json.load(output_file)

    chart = pygal.Bar()
    processor_list = [x['Model'] for x in data]
    chart.add('Price change chart', processor_list)
    chart.x_labels = [x['Price'] for x in data]
    chart.render_to_file('static/images/bar_chart.svg')
    img_url = 'static/images/bar_chart.svg?cache=' + str(time.time())
    return render_template('processors.html', image_url=img_url)


@ChartApp.route('/graphic_cards', methods=['GET', 'POST'])
def graphic_cards():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('graphic_cards.html')


@ChartApp.route('/disks', methods=['GET', 'POST'])
def disks():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('disks.html',)


if __name__ == "__main__":
    ChartApp.run(host='localhost', port=8000, debug=True)



