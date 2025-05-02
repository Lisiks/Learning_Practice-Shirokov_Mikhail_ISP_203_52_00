import json


def get_file_info(link):
    with open(link, 'r') as info_file:
        return json.load(info_file)


def set_file_info(link, info):
    with open(link, 'w') as output_file:
        json.dump(info, output_file, indent=2)