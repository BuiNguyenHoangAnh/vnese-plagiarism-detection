# train_data = read_txt_files(TRAINDATA_PATH)
# train_data = word_segmentation(train_data)
# train_data = remove_punctuation_marks(train_data)
# train_data = remove_stop_words(train_data)
# train_data = remove_numbers(train_data)
# train_data = remove_spaces(train_data)

# test_data = preprocessing_english(test_data)
# test_data = word_segmentation(test_data)
# test_data = remove_punctuation_marks(test_data)
# test_data = remove_stop_words(test_data)
# test_data = remove_numbers(test_data)
# test_data = remove_spaces(test_data)

list1=[u'language', u'world', u'human', u'decrease']
    list2=[u'language', u'apple', u'human', u'decrease']

    list=[]
    sum = 0
    count = 0
    for word1 in input:
            # print word1
            for word2 in list2:
                # print word2

                wordFromList1 = wordnet.synsets(word1)
                wordFromList2 = wordnet.synsets(word2)
                if wordFromList1 and wordFromList2:
                    s = wordFromList1[0].wup_similarity(wordFromList2[0])
                    w1= (wordFromList1[0].lemmas()[0].name())
                    w2=(wordFromList2[0].lemmas()[0].name())
                    similarity = (s, w1, w2)
                    sum = sum + s
                    count+=1
                    print("similarity: ", similarity)
    # print("fuzzy: ", sum/count)
