import json, nltk

TOKENS = []

with open('tokens.json', 'r', encoding='utf-8') as f:
    TOKENS = json.loads(f.read())

print(len(TOKENS))

def parser(qe: str):

    ...
