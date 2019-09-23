# Main links

# network and telecomm connectors
# https://ph.rs-online.com/web/c/connectors/network-telecom-connectors/

# telecomm peripherals
# https://ph.rs-online.com/web/c/computing-peripherals/telecommunications/

# wireless components and modules (computing)
# https://ph.rs-online.com/web/c/computing-peripherals/wireless-components-modules/

# network and communications cabling
# https://ph.rs-online.com/web/c/cables-wires/network-communication-cable/

import requests
import re
import csv
from bs4 import BeautifulSoup

filename = './csv/wifi-routers-table-output'
filetype = '.csv'

url = 'https://ph.rs-online.com/web/c/computing-peripherals/networking-connectivity/network-switches/'

response = requests.get(url)

# print(response.text)
soup = BeautifulSoup(response.text, 'lxml')

names = [re.sub(r'<a [\/\s\w=\-"]+>|<\/a>|\;+', '', str(item)) for item in soup.findAll("a", {"class": "product-name"})]
# stock_numbers = [re.sub(r'<td\s+[\w=\"]+>|</td>', '', str(item)) for item in soup.findAll("a", {"class": "small-link"})]

packs = [re.sub(r'<span [\/\s\w=\-"]+>|</span>|\;+', '', str(item)) for item in soup.findAll("span", {"class": "col-xs-12 pack text-left"})]
prices = [re.sub(r'<span [\/\s\w=\-"]+>|</span>|\;+', '', str(item)) for item in soup.findAll("span", {"class": "col-xs-12 price text-left"})]

# print(len(names))
# print(len(packs))
# print(len(prices))

items = soup.findAll("td", {"class": "otherCol"})

# print(len(items))

# print(packs[4])
objects_for_conversion = []

for i in range(0, len(items)//14):
    name = names[i]
    pack = packs[i]
    price = prices[i]
    model = re.sub(r'<td\s+[\w=\"]+>|</td>', '', str(items[i * 14]))
    number_of_ports = re.sub(r'<td\s+[\w=\"]+>|</td>', '', str(items[i * 14 + 1]))
    desktop_roundmount = re.sub(r'<td\s+[\w=\"]+>|</td>', '', str(items[i * 14 + 2]))
    switch_type = re.sub(r'<td\s+[\w=\"]+>|</td>', '', str(items[i * 14 + 3]))
    network_speed = re.sub(r'<td\s+[\w=\"]+>|</td>', '', str(items[i * 14 + 4]))
    rj45_ports = re.sub(r'<td\s+[\w=\"]+>|</td>', '', str(items[i * 14 + 5]))
    sfp_ports = re.sub(r'<td\s+[\w=\"]+>|</td>', '', str(items[i * 14 + 6]))
    POE = re.sub(r'<td\s+[\w=\"]+>|</td>', '', str(items[i * 14 + 7]))
    dimensions = re.sub(r'<td\s+[\w=\"]+>|</td>', '', str(items[i * 14 + 8]))
    height = re.sub(r'<td\s+[\w=\"]+>|</td>', '', str(items[i * 14 + 9]))
    width = re.sub(r'<td\s+[\w=\"]+>|</td>', '', str(items[i * 14 + 10]))
    depth = re.sub(r'<td\s+[\w=\"]+>|</td>', '', str(items[i * 14 + 11]))
    # width = re.sub(r'<td\s+[\w=\"]+>|</td>', '', str(items[i * 14 + 12]))
    # height = re.sub(r'<td\s+[\w=\"]+>|</td>', '', str(items[i * 14 + 10]))

    obj = {
        "name": name,
        "pack": pack,
        "price": price,
        "model": model,
        "number_of_ports": wireless_connectivity,
        "network_speed": network_speed,
        "wifi_rating": wifi_rating,
        "wifi_standard": wifi_standard,
        "wireless_data_rate": wireless_data_rate,
        "wifi_band": wifi_band,
        "number_of_lan_ports": number_of_lan_ports,
        "security_protocols": security_protocols,
        "dimensions": dimensions,
        "weight": weight,
        "depth": depth,
        # "width": width,
        # "height": height,
    }

    objects_for_conversion.append(obj)

print(objects_for_conversion)

with open(filename + filetype, 'a',
          newline='', encoding='utf-8') as csvfile:

    header = ['name', 'pack', 'price', 'model', 'wireless_connectivity', 'network_speed',
              'wifi_rating', 'wifi_standard', 'wireless_data_rate', 'wifi_band', 
              'number_of_lan_ports', 'security_protocols', 'dimensions', 'weight', 
              'depth', 'width', 'height']

    csvwriter = csv.DictWriter(csvfile, fieldnames=header)

    # csvwriter.writeheader()
    for item in objects_for_conversion:
        csvwriter.writerow(item)
