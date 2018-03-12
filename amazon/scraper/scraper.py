from bs4 import BeautifulSoup
import requests
import re
import fake_useragent

class ProductData:
    soup = ''
    reqt = ''

    def __init__(self, url):
        self.agent = fake_useragent.UserAgent()
        self.head = self.agent.random
        self.header = {'User-Agent': self.head}
        self.reqt = (requests.get(url,headers=self.header,timeout=None))
        self.soup = BeautifulSoup((self.reqt).text, "lxml")   # making soup

    def get_images(self):
        im = self.soup.find(text=re.compile('\\colorImages\\b'))  # finding product images

        if im is None:
            return None

        im = re.findall(r'\bhttps\S*', im.replace('"', ' '))  # making a list of images

        imgs = [i for i in im if (i.endswith('L.jpg'))]  # getting one image of all types

        if imgs:
            return list(set(imgs))  # returns list of images
        return None

    def meta_data(self):
        data = self.soup.find("div", {"id": "feature-bullets"})  # getting product description

        if data is None:
            return None

        data = str(data)
        data = data.replace('\t', '')
        data = data.split('\n')
        data = [i for i in data if (not (i.startswith('<')))]  # removing noise
        data = list(filter(None, data))  # removing NULL values from 'data'

        if data:
            return data

        return None

    def get_asin(self):
        asin = self.soup.find(text=re.compile('\\mediaAsin\\b'))

        if asin is None:
            return None
        asin = (asin[-34:-24]).split("\\hehehaharandom")  # cuz asin number are 10 digit

        if asin:
            return asin

        return None

    def get_category(self):
        category = self.soup.find_all("a", {"class": "a-link-normal a-color-tertiary"})

        if category is None:
            return None  # returns categories as list

        category = [(x.text).replace("\n", "").replace(" ", "") for x in category]

        if category:
            return category

        return None

    def get_title(self):
        title = self.soup.find_all("span", {"class": "a-size-large"})

        if title is None:
            return None

        title = [(x.text).replace("\n", "").replace("  ", "") for x in title]

        if title:
            return title  # returns title in list

        return None

    def __del__(self):
        # just a deconstructor
        return 0
# '''
# ['B01G1E3R3A']\t
# ['','']
# ["Alan Jones Men's Cotton Printed T-Shirt"]
# ['Clothing&Accessories', 'Men', 'T-Shirts&Polos', 'LongSleeveTops']
# ['Fabric - 100% Cotton', 'Luxurious cotton fabric for superior comfort', 'Collection AJC SS17, Authentic AJC® logo label', 'Care Instruction - Machine Wash or Hand Wash', 'Proudly made in India']
# '''





# "large":"https://images-na.ssl-images-amazon.com/images/I/51rrBALx3yL.jpg","main":{"https://images-na.ssl-images-amazon.com/images/I/91pnP8dhCUL._UY445_.jpg":[445,333],"https://images-na.ssl-images-amazon.com/images/I/91pnP8dhCUL._UY500_.jpg":[500,374],"https://images-na.ssl-images-amazon.com/images/I/91pnP8dhCUL._UY550_.jpg":[550,412],"https://images-na.ssl-images-amazon.com/images/I/91pnP8dhCUL._UY606_.jpg":[606,454],"https://images-na.ssl-images-amazon.com/images/I/91pnP8dhCUL._UY679_.jpg":[679,508]},"variant":"MAIN","lowRes":null},{"hiRes":"https://images-na.ssl-images-amazon.com/images/I/91ynOfDH9-L._UL1500_.jpg","thumb":"https://images-na.ssl-images-amazon.com/images/I/51r54JjOUdL._SR38,50_.jpg","large":"https://images-na.ssl-images-amazon.com/images/I/51r54JjOUdL.jpg","main":{"https://images-na.ssl-images-amazon.com/images/I/91ynOfDH9-L._UY445_.jpg":[445,321],"https://images-na.ssl-images-amazon.com/images/I/91ynOfDH9-L._UY500_.jpg":[500,361],"https://images-na.ssl-images-amazon.com/images/I/91ynOfDH9-L._UY550_.jpg":[550,397],"https://images-na.ssl-images-amazon.com/images/I/91ynOfDH9-L._UY606_.jpg":[606,438],"https://images-na.ssl-images-amazon.com/images/I/91ynOfDH9-L._UY679_.jpg":[679,490]},"variant":"PT01","lowRes":null},{"hiRes":"https://images-na.ssl-images-amazon.com/images/I/917dAmfWdbL._UL1500_.jpg","thumb":"https://images-na.ssl-images-amazon.com/images/I/51aSayhFitL._SR38,50_.jpg","large":"https://images-na.ssl-images-amazon.com/images/I/51aSayhFitL.jpg","main":{"https://images-na.ssl-images-amazon.com/images/I/917dAmfWdbL._UY445_.jpg":[445,326],"https://images-na.ssl-images-amazon.com/images/I/917dAmfWdbL._UY500_.jpg":[500,366],"https://images-na.ssl-images-amazon.com/images/I/917dAmfWdbL._UY550_.jpg":[550,403],"https://images-na.ssl-images-amazon.com/images/I/917dAmfWdbL._UY606_.jpg"