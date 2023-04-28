import json
from categories.models import Categories

with open('datasets/categories.json', 'r', encoding='utf-8') as f:
    print(json.load(f)[0])
    categories = Categories()
    categories.text = json.load(f)[0]
    categories.save()
    