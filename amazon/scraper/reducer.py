#!/usr/bin/env python3
"""reducer.py"""

import sys
import pickle
import base64
import urllib.request as ur
import json

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
        asin, data = line.split('\t')
        # get back the dict format
        data = json.loads(data_dump)
        # if we have duplicate asins
        if current_asin == asin:
           continue;
        else:
            images = download_images(data[1])
            enc_images = encode_images(images)
            data.append(enc_images)
            data.append(asin)
            data_pkl = pickle.dumps(data)
            sys.stdout.buffer.write(data_pkl)
            current_asin = asin
            sys.stderr.write("reporter:counter:scraper,product_counter,1\n")

if __name__ == '__main__':
    main()
