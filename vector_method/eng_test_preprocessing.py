# khai bao thu vien
import pandas as pd
import json

from utils import *

# khai ban hang va bien
SOURCE = "../data/eng/dataset1/suspeciuos"
i = 0

# doc file json chua tai lieu nguon
# with open(SOURCE, "r", encoding="utf-8") as f:
#     DATA = json.load(f)
DATA = read_txt_files(SOURCE)

data_content = []

for doc in DATA:
    # print(doc)
    data_content.append(preprocessing_english(doc))
    print(data_content)

# luu ket qua xu ly vao file json
with open("../data/eng/dataset1/_test.json", "w", encoding="utf-8") as json_file:
    json.dump(data_content, json_file, indent = 4, ensure_ascii=False)


