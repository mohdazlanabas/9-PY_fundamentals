# Manage multiple dictionaries

import collections

dict1 = {"Day1": "Monday", "Day2": 'Tuesday"'}
dict2 = {"Day3": "Wednesday", "Day4": "Thursday"}
dict3 = {"Day5": "Friday", "Day6": "Saturday"}

# create single dict
res = collections.ChainMap(dict1, dict2, dict3)
print("\nCOMBINE")
print(res.maps)

print("\nKEYS & VALUES")
print("Keys = {}".format(list(res.keys())))
print("Values = {}".format(list(res.values())))

# elements
print("\nELEMENTS")
for key, val in res.items():
    print("{}={}".format(key, val))

# specific value
print("\nSPECIFIC VALUE")
print("Day3 in res: {}".format(("Day1" in res)))
print("Day4 in res: {}".format(("Day7" in res)))
