import pandas as pd
from utils import *

SOURCE = "../data/vie/dataset1/_vie.json"
TEST_EXACT = "../data/vie/dataset1/_exact.json"
TEST_MODIFIED = "../data/vie/dataset1/_modified.json"
TEST_NEUTRAL = "../data/vie/dataset1/_neu.json"

ewp = []
mwp = []
nwp = []

# đọc tài liệu
source_data = pd.read_json(SOURCE)[0]

exact_data = pd.read_json(TEST_EXACT)[0]
modified_data = pd.read_json(TEST_MODIFIED)[0]
neu_data = pd.read_json(TEST_NEUTRAL)[0]

# tiền xử lý - loại bỏ ký tự đặc biệt

# biến đổi thành chuỗi số
# chuyển thành mã unicode


# chuyển thành số thập phân

# chuyển thành số thực