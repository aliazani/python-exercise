import json

color_file = open('F:\\learn.json', 'w')
# color = json.load(color_file)
# print(color['black'])
me = {
    'name': 'ali',
    'family': 'azani',
    'age': 21
}

paravid = {
    'course': 'python',
    'minutes': 1600,
    'activate': True,
    'teacher': me
}

data = json.dump([paravid, me], color_file)
