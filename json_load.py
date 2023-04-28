import csv
import json

ads_csv = open('datasets/ads.csv', encoding='utf-8')
category_csv = open('datasets/categories.csv', encoding='utf-8')
ads_reader = csv.DictReader(ads_csv)
category_reader = csv.DictReader(category_csv)

ads_json = []
category_json = []

for i in ads_reader:
    i['Id'], i['price'], i['is_published'] = int(i['Id']), int(i['price']), json.loads(i['is_published'].lower())
    i['id'] = i.pop('Id')
    for k in i:
        if type(i[k]) == str:
            i[k] = i[k].replace("\n", " ")
    ads_json.append(i)

for i in category_reader:
    i['id'] = int(i['id'])
    category_json.append(i)

with open('datasets/ads.json', 'w', encoding='utf-8') as fp:
    json.dump(ads_json, fp, ensure_ascii=False, indent=4)

with open('datasets/categories.json', 'w', encoding='utf-8') as fp:
    json.dump(category_json, fp, ensure_ascii=False, indent=4)

