import json
import os

# Fetch the filename from the environment variable
filename = os.environ.get('filename')
if filename is None:
    raise ValueError("Environment variable 'filename' is not set.")

# Read the original JSON file
input_filepath = os.path.join("./aws_downloads", f"{filename}_daring.json")
with open(input_filepath, "r", encoding="utf-8") as file:
    original_string = file.read()

# Split the input string into individual JSON objects
original_data = [json.loads(line) for line in original_string.strip().split('\n')]

# Create a new list with modified elements, including an index
formatted_data = [{"index": idx,
                   "time": entry["time"],
                   "type": entry["type"],
                   "value": entry["value"],
                   "element": "narrate--quiz-3"} for idx, entry in enumerate(original_data)]

# Create a dictionary with the new list
formatted_json = {"daring": formatted_data}

# Write to the first output file
output_filepath1 = "./editions/first.json"
with open(output_filepath1, "w", encoding="utf-8") as output_file:
    output_file.write('{"daring": [\n')
    for i, item in enumerate(formatted_json["daring"]):
        if i < len(formatted_json["daring"]) - 1:
            output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + ',\n')
        else:
            output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + '\n')
    output_file.write(']}\n')

# Write to the second output file
output_filepath2 = "./index_format/daring.json"
with open(output_filepath2, "w", encoding="utf-8") as output_file:
    output_file.write('{"daring": [\n')
    for i, item in enumerate(formatted_json["daring"]):
        if i < len(formatted_json["daring"]) - 1:
            output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + ',\n')
        else:
            output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + '\n')
    output_file.write(']}\n')

print("Formatted JSON written to first.json and daring.json")
