import json
import json_data.sample as j_data


default_skill_data =  j_data.default_skill_data
d_skill_data = json.loads(default_skill_data)
# print(default_skill_data)
print(d_skill_data['intent'])




