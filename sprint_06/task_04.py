# Class Student has attributes full_name:str, avg_rank: float,
# courses: list
# Class Group has attributes title: str, students: list.
#
# Make both classes JSON serializable.
#
# Json-files represent information about student (students).
#
# Create methods:
#
# Student.from_json(json_file) that return Student instance from
# attributes from json-file;
#
# Group.serialize_to_json(list_of_groups, filename)
#
# Group.create_group_from_file(students_file)
#
# Parse given files, create instances of Student class and create
# instances of Group class (title for group is name of json-file without
# extension).

import json
from json import JSONEncoder


class Student:
    def __init__(self, full_name, avg_rank, courses):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    def __repr__(self):
         return f"{self.full_name} ({self.avg_rank}): {self.courses}"


    @classmethod
    def from_json(cls, json_file):
        with open(json_file) as f:
            data = json.load(f)
            full_name, avg_rank, courses = (data[key] for key in data)
            return cls(full_name, avg_rank, courses)


class Group:
    def __init__(self, title, students):
        self.title = title
        self.students = students

    def __repr__(self):
         return f"['title': {self.title}, 'students': {self.students}]]"

    @property
    def students(self):
        return self.students

    @property
    def title(self):
        return self.title

    @classmethod
    def serialize_to_json(cls, list_of_groups, filename):
        with open(filename, "w") as fw:
            res = []
            for lst in list_of_groups:
                res.append({"title": lst.title, "students": lst.students})
            json.dump(res, fw)


    @classmethod
    def create_group_from_file(cls, students_file):
        with open(students_file) as f:

            data = json.load(f)
            students = []
            students.extend(data)
            title = f.name[:-5]
            return cls(title, students)



user1 = Student.from_json("2020-01.json")
print(user1)

g1 = Group.create_group_from_file("2020_2.json")
g2 = Group.create_group_from_file("2020-01.json")
print()
print(g1)
print(g2)
Group.serialize_to_json([g1, g2], "g1")

