# import thư viện
import json
import pandas as pd

from utils import *
from plagiarism_detection import *


SOURCE = "../data/vie/dataset1/_vie.json"
TEST_EXACT = "../data/vie/dataset1/_exact.json"
TEST_MODIFIED = "../data/vie/dataset1/_modified.json"
TEST_NEUTRAL = "../data/vie/dataset1/_neu.json"

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

tp_exact = 0
fn_exact = 0
tp_modified = 0
fn_modified = 0
tp_neu = 0
fn_neu = 0

# tiền xử lý
source_data = pd.read_json(SOURCE)[0]

exact_data = pd.read_json(TEST_EXACT)[0]
modified_data = pd.read_json(TEST_MODIFIED)[0]
neu_data = pd.read_json(TEST_NEUTRAL)[0]
# source_data=['ngôn_ngữ giúp con_người rút_ngắn']
# neu_data=['Selenium là bộ kiểm thử tự_động miễn_phí mã nguồn mở dành cho các ứng_dụng web trên các trình duyệt và nền_tảng khác nhau Nó khá là giống với HP Quick_Test_Pro QTP bây_giờ là UFT chỉ khác là Selenium thì tập_trung vào việc tự_động_hoá các ứng_dụng dựa trên nền_tảng web Kiểm thử được thực_hiện bằng cách sử_dụng công_cụ Selenium thường được gọi_là Kiểm thử Selenium Selenium không_chỉ là công_cụ độc_lập mà là bộ công_cụ của phần mềm mỗi bộ đều đáp_ứng được nhu_cầu kiểm thử khác_nhau của tổ chức Nó có thành phần ']


ewp = []
mwp = []
nwp = []

# kiểm tra đạo văn
print("Processing......")
for doc in exact_data:
    # temp, result_ngram = diff_ngram(source_data, doc, n, threshold_ngram)
    temp = plagiarism_detection(source_data, doc, n, threshold_ngram, threshold_lcs_cs, threshold_fuzzy)
    if temp == 0:
        ewp.append(doc)
    tp_exact += temp

for doc in modified_data:
    temp = plagiarism_detection(source_data, doc, n, threshold_ngram, threshold_lcs_cs, threshold_fuzzy)
    if temp == 0:
        mwp.append(doc)
    tp_modified += temp

for doc in neu_data:
    temp = plagiarism_detection(source_data, doc, n, threshold_ngram, threshold_lcs_cs, threshold_fuzzy)
    if temp == 0:
        nwp.append(doc)
    tp_neu += temp


# xuat ket qua
fn_exact = len(exact_data) - tp_exact
fn_modified = len(modified_data) - tp_modified
fn_neu = len(neu_data) - tp_neu

print("tp - exact: ", tp_exact)
print("tp - modified: ", tp_modified)
print("tp - neu: ", tp_neu)
print("fn - exact: ", fn_exact)
print("fn - modified: ", fn_modified)
print("fn - neu: ", fn_neu)

with open("ewp.json", "w", encoding="utf-8") as json_file:
    json.dump(ewp, json_file, indent = 4, ensure_ascii=False)
with open("mwp.json", "w", encoding="utf-8") as json_file:
    json.dump(mwp, json_file, indent = 4, ensure_ascii=False)
with open("nwp.json", "w", encoding="utf-8") as json_file:
    json.dump(nwp, json_file, indent = 4, ensure_ascii=False)