#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import urllib.request as ur
import sys

current_asin = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    print("\n\nREDUCER INPUT\n\n {}".format(line))
    
    # parse the input we got from mapper.py
    asin, data = line.split('|')

    print("\n\nREDUCER SPLIT\n\n")
    print(asin)
    print()
    print(data)

#     # this IF-switch only works because Hadoop sorts map output
#     # by key (here: word) before it is passed to the reducer
#     if current_asin == asin:
#         continue
#     else:
#         if asin:
#             urls = data[2]
#             # write result to STDOUT
#             print '%s\t%s' % (current_word, current_count)
#         current_count = count
#         current_word = word

# # do not forget to output the last word if needed!
# if current_word == word:
#     print '%s\t%s' % (current_word, current_count)





def download(urls=['http://www.gunnerkrigg.com//comics/00000001.jpg']):
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

def store_image(images):
    pass
