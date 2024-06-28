import json
import os

filename = os.environ.get('filename')
def format_strings_to_json():
    with open("./speechJson/"+filename+"_intrepid.json", "r", encoding="utf-8") as file:
        intrepid_string = file.read()

    with open("./speechJson/"+filename+"_valiant.json", "r", encoding="utf-8") as file:
        valiant_string = file.read()

    # INTREPID FORMATTING
    intrepid_data = [json.loads(line) for line in intrepid_string.strip().split('\n') if line.strip()]

    formatted_data = [{"time": entry["time"],
                       "type": entry["type"],
                       "value": entry["value"],
                       "element": "narrate-1-page"} for entry in intrepid_data]

    formatted_json = {"intrepid": formatted_data}

    with open("second.json", "w", encoding="utf-8") as output_file:
        output_file.write('{"intrepid": [\n')
        for i, item in enumerate(formatted_json["intrepid"]):
            if i < len(formatted_json["intrepid"]) - 1:
                output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + ',\n')
            else:
                output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + '\n')
        output_file.write(']}\n')

    print("Formatted Intrepid JSON written to second.json")

    # VALIANT FORMATTING
    valiant_data = [json.loads(line) for line in valiant_string.strip().split('\n') if line.strip()]

    formatted_data = [{"time": entry["time"],
                       "type": entry["type"],
                       "value": entry["value"],
                       "element": "narrate-1"} for entry in valiant_data]

    formatted_json = {"valiant": formatted_data}

    with open("third.json", "w", encoding="utf-8") as output_file:
        output_file.write('{"valiant": [\n')
        for i, item in enumerate(formatted_json["valiant"]):
            if i < len(formatted_json["valiant"]) - 1:
                output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + ',\n')
            else:
                output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + '\n')
        output_file.write(']}\n')

    print("Formatted Valiant JSON written to third.json")



# switch time and element
def switch_times_intrepid(first_json, second_json, intrepid_file):
    with open(first_json, 'r', encoding="utf-8") as file:
        data = json.load(file)

    with open(second_json, 'r', encoding="utf-8") as file:
        new_times = json.load(file)["intrepid"]

    for item, new_time in zip(data["daring"], new_times):
        item["time"] = new_time["time"]

    with open(intrepid_file, 'w', encoding="utf-8") as outfile:
        outfile.write('{"intrepid": [\n')

        # Write each item to the file, except the last, with a comma
        for item in data["daring"][:-1]:
            outfile.write(json.dumps(item, separators=(',', ': ')) + ',\n')
        # Write the last item without a comma
        if data["daring"]:  # Check if the list is not empty to avoid IndexError
            outfile.write(json.dumps(data["daring"][-1], separators=(',', ': ')))
        outfile.write('\n]}\n')

    # with open(intrepid_file, 'w', encoding="utf-8") as outfile:
    #     for item in data["daring"]:
    #         outfile.write(json.dumps(item, separators=(',', ': ')) + ',\n')

def switch_times_valiant(first_json, second_json, valiant_file):
    with open(first_json, 'r', encoding="utf-8") as file:
        data = json.load(file)

    with open(second_json, 'r', encoding="utf-8") as file:
        new_times = json.load(file)["valiant"]

    for item, new_time in zip(data["daring"], new_times):
        item["time"] = new_time["time"]

    # with open(valiant_file, 'w', encoding="utf-8") as outfile:
    #     for item in data["daring"]:
    #         outfile.write(json.dumps(item, separators=(',', ': ')) + ',\n')
 
    with open(valiant_file, 'w', encoding="utf-8") as outfile:
        outfile.write('{"valiant": [\n')

        # Write each item to the file, except the last, with a comma
        for item in data["daring"][:-1]:
            print('Printing')
            print(item)
            outfile.write(json.dumps(item, separators=(',', ': ')) + ',\n')
        # Write the last item without a comma
        if data["daring"]:  # Check if the list is not empty to avoid IndexError
            outfile.write(json.dumps(data["daring"][-1], separators=(',', ': ')))
            
        outfile.write('\n]}\n')

def main():
    # change strings into json
    format_strings_to_json()
    
    # Now
    # input files names
    first_json_file = "first.json"
    second_json_file = "second.json"
    third_json_file = "third.json"

    # output file names
    intrepid_json_file = "intrepid.json"
    valiant_json_file = "valiant.json"

    switch_times_intrepid(first_json_file, second_json_file, intrepid_json_file)

    print("Intrepid JSON written to " + intrepid_json_file)

    switch_times_valiant(first_json_file, third_json_file, valiant_json_file)

    print("Valiant JSON written to " + valiant_json_file)


if __name__ == "__main__":
    main()