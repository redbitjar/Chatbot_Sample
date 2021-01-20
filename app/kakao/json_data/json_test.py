import json
from sample import get_default_skill_data, Data


default_skill_data =  get_default_skill_data()
d_skill_data = json.loads(default_skill_data)
# print(default_skill_data)
print(d_skill_data['intent'])

d = Data()
print(d.to_string())




