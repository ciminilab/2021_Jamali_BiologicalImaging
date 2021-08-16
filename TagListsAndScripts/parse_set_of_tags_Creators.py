import csv
import json
import pandas as pd

reader = csv.reader(open("../List_tags_Creators.csv", "r"))
set_of_tags = []
for a_line in reader:
    _ = []
    for __ in a_line:
        if __:
            _.append(__)
    set_of_tags.append(_)
    # ['Trainable', 'AI', 'ML']
    print(a_line)

feature_columns = {"input_sentences": []}
for _ in set_of_tags:
    col_name = ";".join(_)
    feature_columns[col_name] = []
json.dump(feature_columns, open("feature_names.json", "w"), indent=4)

input_file_name = "CreatorsshouldDo.csv"
reader = open("../%s" % input_file_name, encoding="ISO-8859-1")
sentences = []
for sentence in reader:
    sentence = sentence.replace("\n", "")
    if not sentence:
        continue
    sentences.append(sentence)
    sentence_lower = sentence.lower()
    for a_feature_name in feature_columns:
        tags = a_feature_name.split(";")
        seen_feature = 0
        for a_tag in tags:
            if a_tag.lower() in sentence_lower:
                seen_feature = 1
        feature_columns[a_feature_name].append(seen_feature)
    print(sentence)
feature_columns["input_sentences"] = sentences
json.dump(feature_columns, open("feature_names.json", "w"), indent=4)

data_output = pd.DataFrame(feature_columns)
data_output.to_csv("../%s" % (input_file_name.replace(".csv", "_counts.csv")), index=False)