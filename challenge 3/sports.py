""|Info:

Printing Sports per Person, by looping through data, appending the sports to a list per person, which gets added to our dictionary.

Variables:
 group {dict} -- "the dictionary that we are building up"
 people {list} -- "list of people with their sport choices"
 for sportman in people: {[for-loop]} -- "iterating through our data, if the sport exists, continue, if not, apeend it to the list"
 print(group) {[dict]} -- "printing the results"
"""

group = {}
people = [
  {
      "name": "ruan",
      "sport": "cricket"
  },
  {
      "name": "stefan",
      "sport": "rugby"
  },
  {
      "name": "stefan",
      "sport": "cricket"
  },
  {
      "name": "james",
      "sport": "rugby"
  },
  {
      "name": "james",
      "sport": "golf"
  },
  {
      "name": "stefan",
      "sport": "rugby"
  },
  {
      "name": "james",
      "sport": "hockey"
  }
]

for sportman in people:
    if sportman['name'] in group:
        if sportman['sport'] not in group[sportman['name']]:
            group[sportman['name']].append(sportman['sport'])
        else:
            pass
    else:
        group[sportman['name']] = []
        group[sportman['name']].append(sportman['sport'])

print(group)