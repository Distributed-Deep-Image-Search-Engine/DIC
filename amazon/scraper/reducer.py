#!/usr/bin/env python3
"""reducer.py"""

import sys
import pickle
import base64
import urllib.request as ur


def download_images(urls):
    images = []
    for url in urls:
        try:
            image = ur.urlopen(url).read()
        except urllib.error.HTTPError as e:
            print(e.code)
        except urllib.error.URLError as e:
            print(e.args)
        images.append(image)
    return images

def encode_images(images):
    enc_images = []
    for image in images:
        enc_image = base64.b64encode(image)
        enc_images.append(enc_image)
    return enc_images

def main():
    current_asin = None
    # input is a json dump
    for line in sys.stdin:
        # clean dump
        line = line.strip()    
        # parse the input we got from mapper.py
        asin, data_dump = line.split('\t')
        # if we have duplicate asins
        if current_asin == asin:
           continue;
        else:
            data['asin'] = asin
            images = download_images(data['links'])
            enc_images = encode_images(images)
            data['images'] = enc_images
            sys.stdin.buffer.write(data)
            current_asin = asin
            sys.stderr.write("reporter:counter:scraper,product_counter,1\n")
if __name__ == '__main__':
    main()
