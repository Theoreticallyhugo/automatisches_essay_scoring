# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:41:30 2024

@author: anast
"""
import json
import re
import textacy
import pandas as pd
from textacy import text_stats as ts

language = textacy.load_spacy_lang("de_core_news_md") #loading german model

data = [json.loads(line) for line in open('essays.json', 'r')] #load data

#saving ids and texts as lists

ids = []
texts = []
for d in data:
    a = d.get("id")
    b = d.get("text")
    ids.append(str(a))
    texts.append(b)

#clean texts from id numbers inside the text and page numbers
#as well as digit typos

for text in texts:
    index = texts.index(text)
    t1 = re.sub(r'\d{6,}', '', text)
    t1 = re.sub(r'\s\d{1}', '', t1)
    t1 = re.sub(r'\n', '', t1)
    t1 = re.sub(r'\s{2,}', '', t1)
    t1 = re.sub(r' ,', ', ', t1)
    texts[index] = t1

dictionary = dict(map(lambda i,j : (i,j) , ids,texts))
keys_to_remove = []

#finding all texts smaller than 10 in length
for key in dictionary:
    if len(dictionary[key]) < 10:
        keys_to_remove.append(key)

for i in keys_to_remove:
    dictionary[i] = 0

#fehlerhafte Texte (found due to errors) - nur Sonderzeichen
del dictionary["6502471"]
del dictionary["6391089"]
del dictionary["6430700"]
del dictionary["4971946"]
del dictionary["6430707"]

#final dictionary, all elidgible texts and their IDs
final_dict = {k:v for k,v in dictionary.items() if v != 0}

#calculating the readability (flesch_reading_ease) score for each text
read_score = []

texts_final = list(final_dict.values())
ids_final = list(final_dict.keys())

for text in texts_final:
    try:
        doc = textacy.make_spacy_doc(text,  language)
        score = ts.flesch_reading_ease(doc)
        read_score.append(round(score))
    except:
        print(f"Error text {texts_final.index(text)}") #in case of ineligible texts 


df = pd.DataFrame(list(zip(ids_final, texts_final, read_score)), 
                  columns =['ID', 'text', 'read_score'])

def get_label(num):
    if 100 > num and num >= 80:
        return 1
    elif 80 > num and num >= 70:
        return 2
    elif 70 > num and num >= 60:
        return 3
    elif 60 > num and num >= 50:
        return 4
    elif 50 > num and num >= 10:
        return 5
 
df['label'] = df['read_score'].apply(get_label)

df['ID']=df['ID'].astype(int)

df1 = pd.read_excel('Ratings.xlsx') #Excel Datei, bei mir hat ich die als "Ratings"
df1.rename(columns={'Participant.Private.ID': 'ID'}, inplace=True)

del df1['Schule']
del df1['Lerngruppe']
del df1['Einwohnerzahl']
del df1['Study_ID']

df1.drop([1024,1025], axis=0, inplace=True)

df1['ID']=df1['ID'].astype(int)

result = pd.merge(df, df1, how="left", on='ID')

result_2_4 = result[result["label"].isin([2,4])]

result.to_csv('data_meta_readease.csv', index=False)
result_2_4.to_csv('data_label_2_4.csv', index = False)

result_2 = result[result["label"].isin([2])]

result_4 = result[result["label"].isin([4])]

result_3 = result[result["label"].isin([3])]

result_5 = result[result["label"].isin([5])]

#subseting labels 2,3,4
result = result[result.label != 2]
result = result[result.label != 3]
result = result[result.label != 4]
result = result[result.label != 5]

#reducing the amount of labels to balance the dataset
result_2 = result_2.sample(frac=0.2)
result_3 = result_3.sample(frac=0.1)
result_4 = result_4.sample(frac=0.2)
result_5 = result_5.sample(frac=0.6)

frames = [result, result_2, result_3, result_4, result_5]

#saving the balanced data together
result_final = pd.concat(frames)

#taking a look at the first few rows of the dataframes
print(result_final.head())

#writing csv-files
result_final.to_csv('data_balanced.csv', index=False)