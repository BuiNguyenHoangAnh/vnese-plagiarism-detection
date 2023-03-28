# import thư viện
import json
import pandas as pd

from utils import *
from plagiarism_detection import *


SOURCE = "../data/eng/dataset1/_eng.json"
TEST = "../data/eng/dataset1/_test.json"

n = 4 # set ngram number

# plagiarism threshold
# In order to determine those plagiarism sentences above, we apply
# the method, which is mentioned in Section 3 with the following
# specific parameters: the threshold_n-gram is 0.7, the
# threshold_cs_lcs is 0.54, the vietnet_theshold is 0.3, the
# p_threshold is 0.6, and the v_threshold is 0.15.
threshold_ngram = 0.7
threshold_lcs_cs = 0.54
threshold_fuzzy = 0.6

tp = 0
fn = 0

# tiền xử lý
source_data = pd.read_json(SOURCE)[0]

test_data = pd.read_json(TEST)[0]

ewp = []

# kiểm tra đạo văn
print("Processing......")
for doc in test_data:
    # temp, result_ngram = diff_ngram(source_data, doc, n, threshold_ngram)
    temp = plagiarism_detection(source_data, doc, n, threshold_ngram, threshold_lcs_cs, threshold_fuzzy)
    if temp == 0:
        ewp.append(doc)
    tp += temp


# xuat ket qua
fn = len(test_data) - tp

print("tp: ", tp)
print("fn: ", fn)
with open("ewp.json", "w", encoding="utf-8") as json_file:
    json.dump(ewp, json_file, indent = 4, ensure_ascii=False)