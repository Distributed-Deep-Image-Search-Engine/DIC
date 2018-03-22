from scraper import ProductData
import pandas as pd
from collections import OrderedDict

df = pd.DataFrame()

file_name = 'Mens-fashion-product-links'


try:
	count = 0 
	for line in open(file_name):
		url = line.strip()
		
		# Making the class object
		prod = ProductData(url)

		my_dict = OrderedDict()
		my_dict['Asin'] = prod.get_asin()
		my_dict['Title'] = prod.get_title()
		my_dict['Categories'] = prod.get_category()
		my_dict['Images_Links'] = prod.get_images()
		my_dict['MetaData'] = prod.meta_data()

		df = df.append(my_dict, ignore_index = True)
		count = count + 1
		print(count) 

except KeyboardInterrupt:
	df.to_pickle('dataframe_data')
	dfs = pd.read_pickle('dataframe_data')
	print(dfs)

# #TO load the dataframe from the given file in the exact right format
# dfs = pd.read_pickle('dataframe_data')
# print(dfs.iloc[0][2])