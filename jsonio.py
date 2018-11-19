import json

data_out = [
    [1, 2, 3, 4], 
    [4, 5, 6, 7]
]
with open('data.json', 'w') as file_out:
    json.dump(data_out, file_out)

with open("data.json", "r") as file_in:
    data_in = json.load(file_in)
    print(data_in)