import json

def wr_to_file(list_of_candidate):
    with open('result.json', mode='w') as f:
        f.write(json.dumps(list_of_candidate, indent=2))
    return

def get_maxID_from_json():
    with open('result.json') as f:
        previos_candidate = json.load(f)

    maxuserID = 0

    for user_dict in previos_candidate:
        if user_dict['id'] > maxuserID:
            maxuserID = user_dict['id']

    return maxuserID