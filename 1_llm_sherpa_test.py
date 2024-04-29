from llmsherpa.readers.file_reader import LayoutPDFReader
import json
import os

# Initialize the reader with the API URL
reader = LayoutPDFReader(parser_api_url='http://127.0.0.1:5010/api/parseDocument?renderFormat=all')

def block_to_dict(block):
    """Recursively convert a block to a dictionary."""
    block_dict = {
        "tag": getattr(block, 'tag', None),
        "level": getattr(block, 'level', None),
        "page_idx": getattr(block, 'page_idx', None),
        "block_idx": getattr(block, 'block_idx', None),
        "top": getattr(block, 'top', None),
        "left": getattr(block, 'left', None),
        "text": block.to_text() if hasattr(block, 'to_text') else None,
        "children": [block_to_dict(child) for child in getattr(block, 'children', [])]
    }
    return block_dict

def document_to_dict(doc):
    """Convert a Document object into a dictionary."""
    sections = doc.sections() if hasattr(doc, 'sections') else []
    return {
        "sections": [block_to_dict(section) for section in sections]
    }

def print_partial_data(data, length=1000):
    """Utility function to print only the first `length` characters of data"""
    print(data[:length])

def process_pdf(file_path):
    try:
        pdf_data = reader.read_pdf(file_path)
        if pdf_data:
            pdf_data_dict = document_to_dict(pdf_data)
            json_data = json.dumps(pdf_data_dict, ensure_ascii=False, indent=4)
            output_path = os.path.join('parsed_pdf_to_json', os.path.basename(file_path) + '.json')
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(json_data)
            
            # Optionally print the first 1000 characters of the JSON string
            print_partial_data(json_data)
        else:
            print(f"No data received from API for {file_path}.")
    except Exception as e:
        print(f"An error occurred while processing {file_path}:", e)

pdf_folder = 'raw_pdf_docs'
for filename in os.listdir(pdf_folder):
    if filename.lower().endswith('.pdf'):
        full_path = os.path.join(pdf_folder, filename)
        process_pdf(full_path)


# # ---------------- to process single file for testing of parsing, uncommented below code ------------------ #
# from llmsherpa.readers.file_reader import LayoutPDFReader
# import json

# # Initialize the reader with the API URL
# reader = LayoutPDFReader(parser_api_url='http://127.0.0.1:5010/api/parseDocument?renderFormat=all')

# def block_to_dict(block):
#     """Recursively convert a block to a dictionary."""
#     block_dict = {
#         "tag": getattr(block, 'tag', None),
#         "level": getattr(block, 'level', None),
#         "page_idx": getattr(block, 'page_idx', None),
#         "block_idx": getattr(block, 'block_idx', None),
#         "top": getattr(block, 'top', None),
#         "left": getattr(block, 'left', None),
#         "text": block.to_text() if hasattr(block, 'to_text') else None,
#         "children": [block_to_dict(child) for child in getattr(block, 'children', [])]
#     }
#     return block_dict

# def document_to_dict(doc):
#     """Convert a Document object into a dictionary."""
#     sections = doc.sections() if hasattr(doc, 'sections') else []
#     return {
#         "sections": [block_to_dict(section) for section in sections]
#     }

# def print_partial_data(data, length=1000):
#     """Utility function to print only the first `length` characters of data"""
#     print(data[:length])

# try:
#     pdf_data = reader.read_pdf('raw_pdf_docs/Cykelstrategi Falkenbergs kommun.pdf')
#     if pdf_data:
#         pdf_data_dict = document_to_dict(pdf_data)
#         json_data = json.dumps(pdf_data_dict, ensure_ascii=False, indent=4)
#         with open('parsed_pdf_to_json/parsed_cykelstrategi.json', 'w', encoding='utf-8') as file:
#             file.write(json_data)
        
#         # Save the raw JSON response for analysis
#         with open('raw_response.txt', 'w', encoding='utf-8') as file:
#             file.write(json_data)

#         # Optionally print the first 1000 characters of the JSON string
#         print_partial_data(json_data)
#     else:
#         print("No data received from the API.")
# except Exception as e:
#     print("An error occurred:", e)
