import json

# Load the JSON data from a file
with open('parsed_pdf_to_json/parsed_cykelstrategi.json', 'r') as file:
    data = json.load(file)

# Function to generate Python access paths for each level in the JSON structure
def generate_access_paths(data, path="data"):
    paths = []
    if isinstance(data, dict):
        # If there is a 'text' key at this level, save the access path
        if 'text' in data:
            paths.append(f"{path}['text']  # Access text at this level")

        # Recurse into other dictionary items
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                new_paths = generate_access_paths(value, f"{path}['{key}']")
                paths.extend(new_paths)
    elif isinstance(data, list):
        # Recurse into list items, using index-based access
        for index, item in enumerate(data):
            new_paths = generate_access_paths(item, f"{path}[{index}]")
            paths.extend(new_paths)

    return paths

# Generate paths starting from the 'sections' key if it exists
if 'sections' in data:
    access_paths = generate_access_paths(data['sections'], "data['sections']")
    for path in access_paths:
        print(path)
else:
    print("Key 'sections' not found in the JSON data.")


# --------------------- old script, outputs basically all data, but only 25 characters per line item -------------- #
# import json

# def print_header_text(data, indent=0, max_para_length=25):
#     """Recursively prints headers and their associated text with indentation, limiting paragraph text to a specified number of characters."""
#     for section in data['sections']:
#         print('  ' * indent + section['text'])  # Print the full header text
        
#         if 'children' in section:
#             for child in section['children']:
#                 if child['tag'] == 'para':
#                     # Truncate only paragraph text if it's longer than max_para_length
#                     child_text = (child['text'][:max_para_length] + '...') if len(child['text']) > max_para_length else child['text']
#                     print('  ' * (indent + 1) + child_text)  # Print truncated paragraph text directly under header
#                 else:
#                     print_header_text({'sections': [child]}, indent + 1, max_para_length)  # Recursive call for nested headers and subheaders

# # Load the JSON data from the file
# with open('parsed_pdf_to_json/parsed_cykelstrategi.json', 'r', encoding='utf-8') as file:
#     json_data = json.load(file)

# # Process and print the document structure with text length limitation for paragraphs
# print_header_text(json_data)
