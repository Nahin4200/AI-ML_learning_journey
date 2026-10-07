import json

# json_srt = '{"name": "nahin","isteacher": true}'
# print (type(json_srt))

# py_obj = json.loads(json_srt)
# print (type(py_obj))
# print (py_obj)


# py_obj = {
#     "name": "nahin",
#     "isteacher": True
# }
# print(type(py_obj))

# json_str = json.dumps(py_obj)
# print(type(json_str))




# with open("data.json", "r") as f:
#     py_obj = json.load(f)
#     print (py_obj)
#     print(type(py_obj))





data = {
    "name": "nahin",
    "age": 23,
    "isteacher": True
}
with open("data.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)



