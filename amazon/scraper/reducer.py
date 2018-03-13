#!/usr/bin/env python3
"""reducer.py"""

import sys
import json
import base64
import urllib.request as ur


def download(urls):
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
    json_images = []
    for image in images:
        json_image = base64.b64encode(image)
        json_images.append(json_image)
    json_images = json.dumps(json_images) 
    return json_images

def store_image(images):
    pass

def main():
    current_asin = None
    # input is a json dump
    for line in sys.stdin:
        # clean dump
        line = line.strip()    
        # parse the input we got from mapper.py
        asin, data_dump = line.split('\t')
        # get back the dict format
        data = json.loads(data_dump)
        # if we have duplicate asins
        if current_asin == asin:
           continue;
        else:
            links = data['links']
            images = download(links)
            json_images = encode_images(images)
            current_asin = asin
            print("{}\t{}{}".format(asin, data_dump, json_images))

if __name__ == '__main__':
    main()
