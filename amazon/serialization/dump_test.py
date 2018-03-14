import pandas as pd
import _pickle as pickle

from scraper import ProductData

df = pd.DataFrame(columns = ['Asin', 'Title', 'Categories', 'Images', 'MetaData'])

i = 0
with open("links.txt") as f:
	for line in f:
		url = line.strip()
		prod = ProductData(line)
		data = [prod.get_asin(), prod.get_title(), prod.get_category(), prod.get_images(), prod.meta_data()]

		df.loc[i] = data

		i = i + 1


af = open("dump.pickle", 'wb')

pickle.dump(df, af)

print(df)

af.close()