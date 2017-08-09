from lxml import html
import requests

targets = [
    'http://www.performancebike.com/webapp/wcs/stores/servlet/Product_10052_10551_1195075_-1___000000',
    'http://www.performancebike.com/webapp/wcs/stores/servlet/Product_10052_10551_1119246_-1_400219__400219',
    'http://www.performancebike.com/webapp/wcs/stores/servlet/Product_10052_10551_1177844_-1___000000'




]
for target in targets:
    response = requests.get(target)
    tree = html.fromstring(response.content)
    ##print(page.text)
    itemName = tree.xpath('//li[@class="active-page"]/text()')
    salePrice = tree.xpath('//span[@class="sale_price_val"]/text()')
    print(itemName[0].strip() + " = " + salePrice[0].strip())




##<li class="active-page">Performance Elite Team Bib Shorts - 2017</li>
##<span class="sale_price_val">$79.99</span>
