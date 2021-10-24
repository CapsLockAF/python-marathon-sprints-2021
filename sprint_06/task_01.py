# Create function find(file, key)
# This function parses json-file and returns all unique values of the key.
#
# 1.json:
# [{"name": "user_1”, "password": "pass_1”},
# {"name": "user_2”, "password": ["pass_1", "qwerty“]} ]
# find("1.json", "password") returns ["pass_1", "qwerty"]
#
# 2.json:
# [
#   {
#       "name": "user_1”,
#       "credentials": {"username": "user_user”, "password":"1234qweQWE"}
#       },
#   {
#       "name": "user_2”,
#       "password": ["pass_1 ", "qwerty "]
#       }
# ]
# find("2.json", "password") returns ["1234qweQWE", "pass_1", "qwerty"]
#
# 3.json:
# {"name": "user_1",
# "credentials": {"username": "user_user","password": "1234qweQWE"}}
# find("3.json", "password") returns ["1234qweQWE"]

import json


def find(file, key):
    with open(file) as f:
        fp = json.load(f)
        res = []

        def find_key_in_deep_dict(d, k):
            for x in d:
                if isinstance(d.get(x), dict):
                    return find_key_in_deep_dict(d.get(x), k)
                elif x == k:
                    return d.get(k)


        if isinstance(fp, dict):
            passw_val = find_key_in_deep_dict(fp, key)
            if isinstance(passw_val, list):
                res.extend(passw_val)
            elif not passw_val:
                pass
            else:
                res.append(passw_val)
            return list(set(res))

        for i in fp:
           passw_val = find_key_in_deep_dict(i, key)
           if isinstance(passw_val, list):
               res.extend(passw_val)
           elif not passw_val:
               pass
           else:
               res.append(passw_val)
        return list(set(res))


