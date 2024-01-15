import json


with open('countries.json', 'r') as r,open('formatedcountries.json', 'w') as f:
        data = json.load(r)
        json.dump(data, f, indent=2)    

with open('countries.csv', 'r') as f, open('formatedconuntries.csv', 'w') as w:
    lines = f.read().split('\n')
    first_line_indent = False
    for line in lines:
        items = line.split(',')
        w.write("\n") if first_line_indent else ...
        for item in items:
            w.write(f"{item:<25}")
        first_line_indent = True
            
