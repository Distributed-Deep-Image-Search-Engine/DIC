#!/usr/bin/env python3
"""mapper.py"""

import sys
from scraper import ProductData

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words

    prod = ProductData(line)
    info = {'Asin':prod.get_asin(), 'Title':prod.get_title(), 'Images_link':prod.get_images(), 'Category':prod.get_category(), 'Metadata':prod.meta_data()}
    for k,v in info.items():
        if(v == None):
            sys.exit('None Error')
    # increase counters
    data = [v for k,v in info.items()]
    for k,v in info.items():
        # write the results to STDOUT (standard output);
        print('{}\t{}'.format(data[0][0], data[1:]))