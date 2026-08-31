# Nested Dictionaries: we can create a dict and inside that dict create other dict as well.

parent = {
    "child1": {
        "name" : "Ram",
        "age": "30"
    },
    "child2" : {
        "name": "Hari",
        "age" :"25"
    },
    "child3" : {
        "name": "Sita",
        "age": "21"
    }
}

print(parent["child1"]["name"])
print(parent)