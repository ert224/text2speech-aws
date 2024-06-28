import json

# switch time and element
def switch_times(first_json, second_json, output_file):
    with open(first_json, 'r', encoding="utf-8") as file:
        data = json.load(file)

    with open(second_json, 'r', encoding="utf-8") as file:
        new_times = json.load(file)["intrepid"]

    for item, new_time in zip(data["daring"], new_times):
        item["time"] = new_time["time"]

    with open(output_file, 'w', encoding="utf-8") as outfile:
        for item in data["daring"]:
            outfile.write(json.dumps(item, separators=(',', ': ')) + ',\n')
    
if __name__ == "__main__":
    first_json_file = "first.json"
    second_json_file = "second.json"
    output_json_file = "output.json"

    switch_times(first_json_file, second_json_file, output_json_file)
