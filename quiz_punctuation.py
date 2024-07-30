import json
import re
import os

filename = os.environ.get('filename')
data = None
first_json_file = "./index_format/daring.json"
with open(first_json_file, 'r', encoding="utf-8") as file:
    data = json.load(file)
    
def check_string(input_string):
    pattern = r'^[A-Za-z]\.$'  # Pattern to match any single alphabet character followed by a period
    if re.match(pattern, input_string):
        return True
    else:
        return False

# Function to increment a character
def increment_char(char):
    return chr(ord(char) + 1)

# Extract the data
entries = data['daring']

# Initialize variables to keep track of sentence punctuation
words = None
index = 0 
sentence_id = 1
letter = chr(ord('a') - 1)
holdBool = False 
# Iterate through the entries
for entry in entries:
    if entry['type'] == 'sentence':
        current_sentence = entry['value']
        clean_paragraph = re.sub(r'\s+', ' ', current_sentence).strip()
        words = clean_paragraph.split(' ')
        index = 0
        if "Select all that apply" in current_sentence:
            print("Slect")
            holdBool = True        
        if check_string(words[0]):
            sentence_id+=1
            letter = increment_char(letter)  # Increment the letter
            print(letter)
    elif entry['type'] == 'word':
        if not holdBool: 
            if entry['value'] in words[index]:
                entry['value'] = words[index]
                if sentence_id==1:
                    entry['element'] = 'narrate-1-quiz'
                else: 
                    entry['element'] =  entry['element'].replace('--', f'-{letter}-')
                index+=1
        else: 
            if entry['value'] in words[index]:
                entry['value'] = words[index]
                if sentence_id==1:
                    entry['element'] = 'narrate-1-quiz'
                else: 
                    entry['element'] =  entry['element'].replace('--', f'-{sentence_id}-')
                index+=1

                

# Filter out entries of type "sentence"
final_data = [entry for entry in entries if entry['type'] != 'sentence']


# Create a dictionary with the new list
formatted_json = {"daring": final_data}

output_filepath2 = "./index_format/daring.json"
with open(output_filepath2, "w", encoding="utf-8") as output_file:
    output_file.write('{"daring": [\n')
    for i, item in enumerate(formatted_json["daring"]):
        if i < len(formatted_json["daring"]) - 1:
            output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + ',\n')
        else:
            output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + '\n')
    output_file.write(']}\n')
