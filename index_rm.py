import json
import os

def rm_index(filename):
    # Read the JSON file with index parameters
    input_filepath = os.path.join("./formatedJSON", f"{filename}.json")
    
    # Check if the file exists
    if not os.path.exists(input_filepath):
        print(f"Error: File {input_filepath} does not exist.")
        return None
    
    try:
        with open(input_filepath, "r", encoding="utf-8") as file:
            formatted_json = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file {input_filepath}: {e}")
        return None

    # Remove the index parameter from each dictionary
    for entry in formatted_json.get(filename, []):
        entry.pop("index", None)

    # Write the new data to a new file
    output_filepath = os.path.join("./final_format", f"{filename}.json")
    with open(output_filepath, "w", encoding="utf-8") as output_file:
        output_file.write('{"')
        output_file.write(f'{filename}')
        output_file.write('": [\n')
        for i, item in enumerate(formatted_json[filename]):
            if i < len(formatted_json[filename]) - 1:
                output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + ',\n')
            else:
                output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + '\n')
        output_file.write(']}\n')
    
    return formatted_json.get(filename, [])

def main():
    master_data = {}

    for filename in ['daring', 'intrepid', 'valiant']:
        data = rm_index(filename)
        if data is not None:
            master_data[filename] = data

    output_all = os.path.join("./final_format", "all.json")
    with open(output_all, "w", encoding="utf-8") as master_file:
        master_file.write('{\n')
        for idx, key in enumerate(master_data):
            master_file.write(f'"{key}": [\n')
            for i, item in enumerate(master_data[key]):
                if i < len(master_data[key]) - 1:
                    master_file.write('\t' + json.dumps(item, separators=(',', ': ')) + ',\n')
                else:
                    master_file.write('\t' + json.dumps(item, separators=(',', ': ')) + '\n')
            if idx < len(master_data) - 1:
                master_file.write('],\n')
            else:
                master_file.write(']\n')
        master_file.write('}\n')
    print("All index removed. \n Final JSON files found in final format")

if __name__ == "__main__":
    main()
