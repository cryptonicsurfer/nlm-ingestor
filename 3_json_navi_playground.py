import json

with open('parsed_pdf_to_json/parsed_cykelstrategi.json', 'r') as file:
    data = json.load(file)


# Assuming 'data' has been loaded from your JSON file as before
for index, item in enumerate(data['sections']):
    if 'text' in item:  # Check if 'text' key exists in the dictionary
        print(f"{index}: {item['text']}, ---------------- {item['tag']}")
        for item in item['children']:
            print(f'\t{item} \n ----------- \n ')
    if index >= 10:  # Stop after 100 iterations
        break
