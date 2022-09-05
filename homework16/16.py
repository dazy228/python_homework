import json

dictionary = {
    '194657': ('Void', 11),
    '194627': ('Tom', 8),
    '194117': ('Blade', 44),
    '195657': ('Daniel', 33),
    '194332': ('Jack', 19),
    '194646': ('Marcy', 23)
}

with open('dict.json', 'w') as f:
    json.dump(dictionary, f)
