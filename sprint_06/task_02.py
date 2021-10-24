# Implement function parse_user(output_file, *input_files) for creating
# file that will contain only unique records (unique by key "name")
# by merging information from all input_files argument (if we find user
# with already existing name from previous file we should ignore it).
#
#
# If the function cannot find input files we need to log information with
# error level
#
# root - ERROR - File <file name> doesn't exists
#
# For example:
# user1.json :
# [{"name": "Bob1", "rate": 1, “languages": ["English"]},
# {"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
# ]
#
# user2.json :
# [{"name": "Bob1", "rate": 25, “languages": ["French"]},
# {"name": "Bob3", "rate": 78, "languages": ["Germany"]}
# ]
#
# If we execute parse_user(user3.json, user1.json, user2.json)
# then file user3.json should contain information:
# [{"name": "Bob1", "rate": 1, “languages": ["English"]},
# {"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
# {"name": "Bob3", "rate": 78, "languages": ["Germany"]}
# ]

import json
import logging

logging.basicConfig(filename='app.log',
                    filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')


def parse_user(output_file, *input_files):
    res = []
    users = []

    for file in input_files:
        try:
            with open(file) as f:
                fr = json.load(f)
                for user in fr:
                    if not user.get("name"):
                        continue

                    if user['name'] not in users:
                        users.append(user['name'])
                        res.append(user)
        except FileNotFoundError as err:
            logging.error(f"File {err.filename} doesn't exists")
            continue

    with open(output_file, "w") as fw:
        json.dump(res, fw, indent=4)
