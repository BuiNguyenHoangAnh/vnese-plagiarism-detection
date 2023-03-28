# khai bao thu vien
import json

import pandas as pd

from utils import *

# khai ban hang va bien
SOURCE = "../data/vie/vie.json"
_SOURCE = "../data/vie/_vie.json"
NEW = "<path>/new.json" # need to be modified

# doc du lieu moi
new_data = pd.read_json(NEW)[0]

# mo cac file nguon
source = pd.read_json(SOURCE)[0] 
_source = pd.read_json(_SOURCE)[0]

# them data moi vao nguon
# data_obj = {
#     "id": "",
#     "author": "",
#     "content": data,
#     "picture_count" : 0,
#     "processed" : 0,
#     "source" : "",
#     "title" : "",
#     "topic" : "",
#     "url" : "",
#     "crawled_at" : ""
# }
data = []
i = 0
for doc in new_data:
    source.append(doc)
    temp = new_data[i]["content"]
    data.append(temp)
    i += 1

data = preprocessing(data)
for doc in data:
    _source.append(doc)

# update cac file nguon
with open("../data/vie/vie.json", "w", encoding="utf-8") as json_file:
    json.dump(source, json_file, indent = 4, ensure_ascii=False)
    
with open("../data/vie/_vie.json", "w", encoding="utf-8") as json_file:
    json.dump(_source, json_file, indent = 4, ensure_ascii=False)