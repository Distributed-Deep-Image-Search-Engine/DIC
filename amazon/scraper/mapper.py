#!/usr/bin/env python3
"""mapper.py"""

import sys
import json

from scraper import ProductData

def main():
    # input comes as a product link
    for line in sys.stdin:
        # strip the url of leading whitespaces
        url = line.strip()
        # scrape the product details
        prod = ProductData(url)
        asin = prod.get_asin()
        title = prod.get_title()
        links = prod.get_images()
        category = prod.get_category()
        metadata = prod.meta_data()
        data = [title, links, category, metadata]
        # Check for scraper errors
        for item in data:
            if data[item] is None:
                sys.exit('Fetch Error')
        # dump data as json string
        data_dump = json.dumps(data)
        # put asin and json data to output stream  
        print('{}\t{}'.format(asin, data_dump))

if __name__ == '__main__':
    main()