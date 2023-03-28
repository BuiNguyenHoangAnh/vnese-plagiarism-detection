# khai bao thu vien
import json

import pandas as pd

from utils import *

# khai ban hang va bien
SOURCE = "../data/vie/dataset1/vie_new.json"
i = 0

# doc file json chua tai lieu nguon
with open(SOURCE, "r", encoding="utf-8") as f:
    DATA = json.load(f)
print(DATA)
# DATA = pd.read_json(SOURCE)[0]


data_content = []


for doc in DATA:
    print(doc["exact"])
    temp = doc["exact"]
    data_content.append(temp)
    i += 1

# tien xu ly tai lieu nguon
data_preprocessing = preprocessing(data_content)
print(data_preprocessing)

# luu ket qua xu ly vao file json
with open("../data/vie/dataset1/_vie.json", "w", encoding="utf-8") as json_file:
    json.dump(data_preprocessing, json_file, indent = 4, ensure_ascii=False)

