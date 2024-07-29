import json
import re

jsonString= [
	{"index": 0,"time": 25,"type": "word","value": "Reflect","element": "narrate--reflection"},
	{"index": 1,"time": 1130,"type": "word","value": "Take","element": "narrate--reflection"},
	{"index": 2,"time": 1367,"type": "word","value": "a","element": "narrate--reflection"},
	{"index": 3,"time": 1417,"type": "word","value": "moment","element": "narrate--reflection"},
	{"index": 4,"time": 1817,"type": "word","value": "to","element": "narrate--reflection"},
	{"index": 5,"time": 1917,"type": "word","value": "think","element": "narrate--reflection"},
	{"index": 6,"time": 2192,"type": "word","value": "about","element": "narrate--reflection"},
	{"index": 7,"time": 2455,"type": "word","value": "the","element": "narrate--reflection"},
	{"index": 8,"time": 2530,"type": "word","value": "following","element": "narrate--reflection"},
	{"index": 9,"time": 3622,"type": "word","value": "1","element": "narrate--reflection"},
	{"index": 10,"time": 4527,"type": "word","value": "Reflecting","element": "narrate--reflection"},
	{"index": 11,"time": 5027,"type": "word","value": "on","element": "narrate--reflection"},
	{"index": 12,"time": 5190,"type": "word","value": "how","element": "narrate--reflection"},
	{"index": 13,"time": 5377,"type": "word","value": "grandparent","element": "narrate--reflection"},
	{"index": 14,"time": 5977,"type": "word","value": "scams","element": "narrate--reflection"},
	{"index": 15,"time": 6377,"type": "word","value": "work","element": "narrate--reflection"},
	{"index": 16,"time": 6902,"type": "word","value": "can","element": "narrate--reflection"},
	{"index": 17,"time": 7065,"type": "word","value": "you","element": "narrate--reflection"},
	{"index": 18,"time": 7165,"type": "word","value": "think","element": "narrate--reflection"},
	{"index": 19,"time": 7477,"type": "word","value": "of","element": "narrate--reflection"},
	{"index": 20,"time": 7590,"type": "word","value": "what","element": "narrate--reflection"},
	{"index": 21,"time": 7765,"type": "word","value": "personal","element": "narrate--reflection"},
	{"index": 22,"time": 8190,"type": "word","value": "information","element": "narrate--reflection"},
	{"index": 23,"time": 8827,"type": "word","value": "might","element": "narrate--reflection"},
	{"index": 24,"time": 9040,"type": "word","value": "be","element": "narrate--reflection"},
	{"index": 25,"time": 9177,"type": "word","value": "accessible","element": "narrate--reflection"},
	{"index": 26,"time": 9727,"type": "word","value": "about","element": "narrate--reflection"},
	{"index": 27,"time": 9952,"type": "word","value": "you","element": "narrate--reflection"},
	{"index": 28,"time": 10127,"type": "word","value": "online","element": "narrate--reflection"},
	{"index": 29,"time": 11182,"type": "word","value": "Is","element": "narrate--reflection"},
	{"index": 30,"time": 11320,"type": "word","value": "it","element": "narrate--reflection"},
	{"index": 31,"time": 11407,"type": "word","value": "something","element": "narrate--reflection"},
	{"index": 32,"time": 11857,"type": "word","value": "you've","element": "narrate--reflection"},
	{"index": 33,"time": 12045,"type": "word","value": "shared","element": "narrate--reflection"},
	{"index": 34,"time": 12432,"type": "word","value": "yourself","element": "narrate--reflection"},
	{"index": 35,"time": 12845,"type": "word","value": "on","element": "narrate--reflection"},
	{"index": 36,"time": 13007,"type": "word","value": "social","element": "narrate--reflection"},
	{"index": 37,"time": 13382,"type": "word","value": "media","element": "narrate--reflection"},
	{"index": 38,"time": 13695,"type": "word","value": "platforms","element": "narrate--reflection"},
	{"index": 39,"time": 14620,"type": "word","value": "or","element": "narrate--reflection"},
	{"index": 40,"time": 14745,"type": "word","value": "information","element": "narrate--reflection"},
	{"index": 41,"time": 15407,"type": "word","value": "shared","element": "narrate--reflection"},
	{"index": 42,"time": 15720,"type": "word","value": "about","element": "narrate--reflection"},
	{"index": 43,"time": 15945,"type": "word","value": "you","element": "narrate--reflection"},
	{"index": 44,"time": 16082,"type": "word","value": "by","element": "narrate--reflection"},
	{"index": 45,"time": 16232,"type": "word","value": "someone","element": "narrate--reflection"},
	{"index": 46,"time": 16582,"type": "word","value": "else","element": "narrate--reflection"}
]

# Input paragraph
paragraph = """Reflect
Take a moment to think about the following:

1. Reflecting on how grandparent scams work, can you think of what personal information might be accessible about you online? Is it something you've shared yourself on social media platforms, or information shared about you by someone else?"""

# Remove newlines and multiple white spaces
clean_paragraph = re.sub(r'\s+', ' ', paragraph).strip()

# Split the paragraph based on white spaces
words = clean_paragraph.split(' ')

# Print the result
print(words)

for i, item in enumerate(jsonString):
    if item['value'] in words[i]:
        item['value'] = words[i]

print("\njsostr\n")
# Convert the updated dictionary back to a JSON string
updated_json_str = json.dumps(jsonString, indent=4)

# Print the updated JSON string
print(updated_json_str)
print(jsonString)
