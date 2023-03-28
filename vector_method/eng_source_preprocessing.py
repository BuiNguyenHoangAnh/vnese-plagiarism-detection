# khai bao thu vien
from traceback import print_tb
import pandas as pd
import json

from utils import *

# khai ban hang va bien
SOURCE = "../data/eng/dataset1/source"
i = 0

# doc file json chua tai lieu nguon
# with open(SOURCE, "r", encoding="utf-8") as f:
#     DATA = json.load(f)
# DATA = pd.read_json(SOURCE)[0]
DATA = read_txt_files(SOURCE)
# print(DATA)

data_content = []


# for doc in DATA:
#     print(doc["exact"])
#     temp = doc["exact"]
#     data_content.append(temp)
#     i += 1

# tien xu ly tai lieu nguon
for doc in DATA:
    # print(doc)
    data_content.append(preprocessing_english(doc))
    print(data_content)

# luu ket qua xu ly vao file json
with open("../data/eng/dataset1/_eng.json", "w", encoding="utf-8") as json_file:
    json.dump(data_content, json_file, indent = 4, ensure_ascii=False)

