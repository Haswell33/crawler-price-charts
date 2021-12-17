import xml.etree.ElementTree as ET


def generate_xml(filename):
    output_root = ET.Element("Items")
    m = range(5)
    n = range(5)
    x = -1
    for i in m:
        input_tree_get_model = ET.parse('PricePlot_scrapy/output_files/processors_output_'+str(i)+'.xml')
        input_root_get_model = input_tree_get_model.getroot()
        for child_model in input_root_get_model.iter('Model'):
            x = x + 1
            model = child_model.text
            model_element = ET.SubElement(output_root, "Model")
            model_element.text = model
            for j in n:
                input_tree_get_price = ET.parse('PricePlot_scrapy/output_files/processors_output_'+str(j)+'.xml')
                input_root_get_price = input_tree_get_price.getroot()
                for child_price in input_root_get_price.iter('Price'+str(x)):
                    price = child_price.text
                    ET.SubElement(model_element, "Price").text = price
        x = -1
    output_tree = ET.ElementTree(output_root)
    with open('PricePlot_scrapy/output_files/'+filename, "wb") as output_file:
        output_tree.write(output_file)
    print("xml_parse.py loaded")


if __name__ == "__main__":
    generate_xml("items_processor.xml")
