import json

person = {"Name" : "Jason", "Age" : 23, "City" : "NYC"}

person_str = json.dumps(person)
print(person_str)

person_back = json.loads(person_str)
print(person_back)