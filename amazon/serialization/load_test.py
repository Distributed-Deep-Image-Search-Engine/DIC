import pandas as pd
import _pickle as pickle

f = open("dump.pickle", "rb")
x = pickle.load(f)

print(x)