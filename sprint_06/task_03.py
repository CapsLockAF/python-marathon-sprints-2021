# In user.json file we have information about users in format
# [{“id”: 1, “name”: “userName”, “department_id”: 1}, ...],
#
# in file department.json are information about departments in format:
# [{“id”: 1, “name”: “departmentName”}, ...].
#
# Function user_with_department(csv_file, user_json, department_json)
# should read from json files information and create csv file in format:
#
# header line - user, department
#
# next lines :  <userName>, <departmentName>
#
# If file department.json doesn't contain department with department_id
# from user.json we generate DepartmentName exception.
#
# Create appropriate json-schemas for user and department.
#
# If schema for user or department doesn't satisfy formats described above
# we should generate InvalidInstanceError exception
#
# To validate instances create function validate_json(data, schema)

import json
import jsonschema
from jsonschema import validate
import csv

schema_user = {
    "title": "user",
    "type": "array",
    "items": [
        {
            "type": "object",
            "properties": {
                    "id": {"type": "number"},
                    "name": {"type": "string"},
                    "department_id": {"type": "number"},
            },
            "required": [
                    "id",
                    "name",
                    "department_id",
                ],
        }
    ]

}
schema_department = {
    "title": "department",
    "type": "array",
    "items": [
            {
                "type": "object",
                "properties": {
                        "id": {"type": "number"},
                        "name": {"type": "string"},
            },
                "required": [
                        "id",
                        "name",
                    ],
                }
        ]
}


class DepartmentName(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


class InvalidInstanceError(Exception):
    def __str__(self):
        return None


def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)
        return data
    except jsonschema.exceptions.ValidationError:
        print(f"Error in {schema['title']} schema")


def user_with_department(csv_file, user_json, department_json):
    res = []
    dep_ids = []
    with open(user_json) as f:
        u_json = validate_json(json.load(f), schema_user)
        with open(department_json) as fd:
            dep_json = validate_json(json.load(fd), schema_department)

            try:
                dep_ids.extend(map(lambda x: x["id"], dep_json))

                for u_data in u_json:
                    if u_data["department_id"] not in dep_ids:
                        print(f"Department with id {u_data['department_id']} doesn't exists")

                    for d_data in dep_json:
                        if u_data["department_id"] == d_data["id"]:
                            res.append({"name": u_data["name"], "department": d_data["name"]})

            except TypeError:
                return

    with open(csv_file, 'w', newline='') as csv_file:
        fieldnames = ['name', 'department']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(res)

