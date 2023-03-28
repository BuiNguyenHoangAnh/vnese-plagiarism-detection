import json
from random import randint

SOURCE = "../data/vie/dataset1/news_dataset.json"
CASES = 1500
ID = 160000

with open(SOURCE, "r", encoding="utf-8") as f:
    DATA = json.load(f)

i = 0
index = []
test_data = []
for item in DATA:
# while(i < CASES):
#     temp = randint(1, ID + 1)
    if i< CASES:
#         index.append(temp)
#     else:
#         for j in index:
#             while(temp == j):
#                temp = randint(0, CASES) 
#         index.append(temp)
        data = {
            "id": DATA[i]["id"],
            "exact": DATA[i]["content"],
            "modified": ""
        }
        test_data.append(data)
        i += 1
    else:
        break

with open("../data/vie/vie_new.json", "w", encoding="utf-8") as json_file:
    json.dump(test_data, json_file, indent = 4, ensure_ascii=False)