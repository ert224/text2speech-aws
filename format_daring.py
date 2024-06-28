import json

original_string ='''
{"time":25,"type":"word","start":2,"end":7,"value":"Let's"}
{"time":300,"type":"word","start":8,"end":13,"value":"begin"}
{"time":600,"type":"word","start":14,"end":17,"value":"the"}
{"time":675,"type":"word","start":18,"end":25,"value":"section"}
{"time":1162,"type":"word","start":26,"end":28,"value":"on"}
{"time":1400,"type":"word","start":29,"end":37,"value":"identity"}
{"time":1862,"type":"word","start":38,"end":43,"value":"theft"}
{"time":2175,"type":"word","start":44,"end":54,"value":"evaluation"}
{"time":3542,"type":"word","start":58,"end":60,"value":"It"}
{"time":3642,"type":"word","start":61,"end":65,"value":"will"}
{"time":3792,"type":"word","start":66,"end":70,"value":"take"}
{"time":4055,"type":"word","start":71,"end":77,"value":"around"}
{"time":4417,"type":"word","start":78,"end":80,"value":"10"}
{"time":4667,"type":"word","start":81,"end":88,"value":"minutes"}
{"time":4980,"type":"word","start":89,"end":91,"value":"to"}
{"time":5067,"type":"word","start":92,"end":100,"value":"complete"}
{"time":6185,"type":"word","start":104,"end":108,"value":"Find"}
{"time":6535,"type":"word","start":109,"end":112,"value":"out"}
{"time":6760,"type":"word","start":113,"end":117,"value":"your"}
{"time":6922,"type":"word","start":118,"end":126,"value":"identity"}
{"time":7335,"type":"word","start":127,"end":132,"value":"theft"}
{"time":7622,"type":"word","start":133,"end":143,"value":"resilience"}
{"time":8135,"type":"word","start":144,"end":149,"value":"score"}
{"time":9115,"type":"word","start":151,"end":155,"value":"Take"}
{"time":9365,"type":"word","start":156,"end":160,"value":"this"}
{"time":9565,"type":"word","start":161,"end":163,"value":"to"}
{"time":9715,"type":"word","start":164,"end":170,"value":"assess"}
{"time":10052,"type":"word","start":171,"end":175,"value":"your"}
{"time":10165,"type":"word","start":176,"end":189,"value":"understanding"}
{"time":10852,"type":"word","start":190,"end":192,"value":"of"}
{"time":11002,"type":"word","start":193,"end":201,"value":"identity"}
{"time":11440,"type":"word","start":202,"end":207,"value":"theft"}
{"time":11840,"type":"word","start":208,"end":211,"value":"and"}
{"time":11965,"type":"word","start":212,"end":216,"value":"earn"}
{"time":12127,"type":"word","start":217,"end":218,"value":"a"}
{"time":12190,"type":"word","start":219,"end":224,"value":"badge"}
'''
# Split the input string into individual JSON objects
original_data = [json.loads(line) for line in original_string.strip().split('\n')]

# Create a new list with modified elements
formatted_data = [{"time": entry["time"],
                   "type": entry["type"],
                   "value": entry["value"],
                   "element": "narrate-1-page"} for entry in original_data]

# Create a dictionary with the new list
formatted_json = {"daring": formatted_data}

with open("first.json", "w", encoding="utf-8") as output_file:
    output_file.write('{"daring": [\n')
    for i, item in enumerate(formatted_json["daring"]):
        if i < len(formatted_json["daring"]) - 1:
            # Item not last, append comma
            output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + ',\n')
        else:
            # Last item, do not append comma
            output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + '\n')
    output_file.write(']}\n')

with open("edit.json", "w", encoding="utf-8") as output_file:
    output_file.write('"daring": [\n')
    for i, item in enumerate(formatted_json["daring"]):
        if i < len(formatted_json["daring"]) - 1:
            # Item not last, append comma
            output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + ',\n')
        else:
            # Last item, do not append comma
            output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + '\n')
    output_file.write('],\n')

print("Formatted JSON written to first.json")
