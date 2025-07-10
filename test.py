import json

input_file = open ('countries+cities.json')
json_array = json.load(input_file)

print("=== Extract All Names ===")
names = [item['name'] for item in json_array]
print(names)

print("\n=== Extract All Cities (flattened) ===")
all_cities = []
for item in json_array:
    all_cities.extend(item['cities'])
print(all_cities)

