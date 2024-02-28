import pymongo
from pymongo import MongoClient
from pprint import pprint

# Create the connection string
connect =  "mongodb+srv://nguyenkevin828:Password@cecs-323-spring-2023.qhst2lw.mongodb.net/?retryWrites=true&w=majority"

# Create a connection to the MongoDB cluster in Atlas
db = MongoClient(connect)

# Create a reference to the Demonstration database within your cluster
demo = db["Demonstration"]

# Make a reference to the departments collection in the Demonstration database
depts = demo["departments"]

# Make a reference to the courses collection in the Demonstration database
crses = demo["courses"]

# Set up a dictionary with two department definitions
departments = [
    {"name": "Computer Engineering Computer Science",
     "abbreviation": "CECS",
     "chair_name": "Mehrdad Aliasgari",
     "building": "ECS",
     "office": 526,
     "description": "All things computer"},
    {"name": "Chemical Engineering",
     "abbreviation": "CHE",
     "chair_name": "Roger C. Lo",
     "building": "EN2",
     "office": 101,
     "description": "Finding new ways to make the world better chemically"}
]

# Insert the new departments
depts.insert_many(departments)

# Define a utility function to pretty print iterables
from pprint import pprint

def pp(thing):
    for thingee in thing:
        pprint(thingee)

# Define a utility function that maps from the department abbreviation to the _id value for that department
# Interestingly enough, the ObjectID wrapper is unnecessary
def dept_id(abbreviation: str):
    # Honestly, the project is gratuitous since I just ask for
    # the _id from the resulting dict
    return depts.find_one({"abbreviation": abbreviation}, {"_id": 1})["_id"]

# Define two courses in the CECS department
courses = [
    {"department": dept_id("CECS"),
     "course_number": 323,
     "course_name": "Database Design Fundamentals",
     "description": "Relational & NoSQL design",
     "units": 3},
    {"department": dept_id("CECS"),
     "course_number": 274,
     "course_name": "Data Structures",
     "description": "Using basic data structures to solve problems in Object Oriented Python programming",
     "units": 3}
]

# Insert the courses
crses.insert_many(courses)

# Perform a "join from Department to Course using the migrating foreign key of _id in Department that migrates down into Course
pp(depts.aggregate([
    {"$lookup": {
        "from": "courses",
        "localField": "_id",
        "foreignField": "department",
        "as": "courses"
    }}
]))

# Perform a fake inner join, returning only departments with associated courses
pp(depts.aggregate([
    {"$lookup": {
        "from": "courses",
        "localField": "_id",
        "foreignField": "department",
        "as": "courses"
    }},
    {"$match": {"courses": {"$exists": True, "$type": 'array', "$not": {"$size": 0}}}}
]))

# Sort courses by course number and join to retrieve department information for each course
pp(crses.aggregate([
    {"$sort": {"course_number": 1}},
    {"$lookup": {
        "from": "departments",
        "localField": "department",
        "foreignField": "_id",
        "as": "department"
    }},
    {"$match": {"department": {"$exists": True, "$type": 'array', "$not": {"$size": 0}}}}
]))
