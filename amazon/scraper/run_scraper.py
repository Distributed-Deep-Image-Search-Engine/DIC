from scraper import ProductData
import pandas as pd
from collections import OrderedDict

df = pd.DataFrame()

file_name = 'give the desired file_name'

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

# TO pickle the data into specified file
df.to_pickle('dataframe_data')


#TO load the dataframe from the given file in the exact right format
dfs = pd.read_pickle('dataframe_data')
print(dfs.iloc[0][2])