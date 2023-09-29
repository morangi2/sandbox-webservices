#!/usr/bin/env python3

import json

people = [
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  }
]

people2 = [
  {
    "name": "Sabrina Green2",
    "username": "sgreen2",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones2",
    "username": "ejones2",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  }
]

# use dump() to write directly to a file
with open("/~/people.json", "w") as people_json:
    json.dump(people, people_json, indent = 2) #creates a line-delimited json file == more readable
    #json.dump(people, people_json) #creates a 1-liner json file

# use dumps() == returns s string, instead of writing directly to a file
people2_json = json.dumps(people2)
print(people2_json)

# use load() == inverse of dump() == deserializes JSON from a file into basic Python objects ==> JSON file 2 Python object
# loads() == same as load() but parses a string INSTEAD of a file ==> JSON string to Python object

with open("/~/people.json", "r") as people_json:
    people3 = json.load(people_json)
print(people3)

people4 = json.loads(people2_json)
print(people4)
"""
TO USE YAML instead:::
with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)
"""