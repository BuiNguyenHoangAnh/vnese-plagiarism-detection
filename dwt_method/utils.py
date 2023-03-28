import re, os, nltk

# đọc từ file .txt
def read_txt_file(path):
    f = open(path, "r", encoding="utf8")
    document = f.read().lower()
    f.close()
    return document

def read_txt_files(path):
    dirs = os.listdir( path )

    data = []

    for file in dirs:
        if file == '.DS_Store':
                continue
        path_to_file=path+'/'
        file_name = file
        path_to_file += file_name
        # with open(path_to_file, 'r', encoding = 'latin1') as f: #eng
        with open(path_to_file, 'r', encoding = 'utf8') as f: #vie
            mylist = f.read()
            sent_tokenize_list = nltk.sent_tokenize(mylist)
            temp = []
            for i in sent_tokenize_list:
                sent = i.lower()
                sent = re.sub('[^A-Za-z0-9]+', ' ', sent)
                temp.append(sent)
            mylist = re.sub(r"\n", "", mylist)
            data.append(mylist)
    return data

# loại bỏ ký tự đặc biệt
def remove_punctuation_marks(document):
    doc = re.sub(r"\W", " ", document)
    print("remove punctuation marks: ", doc)
    return doc

