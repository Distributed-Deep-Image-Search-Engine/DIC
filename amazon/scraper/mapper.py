#!/usr/bin/env python3
"""mapper.py"""

import sys
from scraper import ProductData

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    url = line.strip()
    # split the line into words
    prod = ProductData(url)
    asin = prod.get_asin()
    title = prod.get_title()
    link = prod.get_images()
    category = prod.get_category()
    metadata = prod.meta_data()
    info = [asin, title, link, category, metadata]
    
    for i in info:
        if(i == None):
            sys.exit('None Error')

    print('{}|{}'.format(info[0][0], info[1:]))