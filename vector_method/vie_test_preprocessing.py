# khai bao thu vien
import json

from utils import *

# khai ban hang va bien
SOURCE = "../data/vie/dataset1/test.json"
i = 0

# doc file json chua tai lieu nguon
with open(SOURCE, "r", encoding="utf-8") as f:
    DATA = json.load(f)
# DATA = pd.read_json(SOURCE)
print('source:', DATA)

data_exact = []
data_modified = []

for doc in DATA:
    print(doc)
    temp = doc["exact"]
    data_exact.append(temp)
    if DATA[i]["modified"] != "":
        temp = doc["modified"]
        data_modified.append(temp)
    i += 1

# tien xu ly tai lieu nguon
data_exact = preprocessing(data_exact)
data_modified = preprocessing(data_modified)

# luu ket qua xu ly vao file json
with open("../data/vie/dataset1/_exact.json", "w", encoding="utf-8") as json_file:
    json.dump(data_exact, json_file, indent = 4, ensure_ascii=False)
with open("../data/vie/dataset1/_modified.json", "w", encoding="utf-8") as json_file:
    json.dump(data_modified, json_file, indent = 4, ensure_ascii=False)


