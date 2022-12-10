from pymongo import MongoClient
from pymongo import collection
import pymongo
from bson.dbref import DBRef
import random
import getpass
import pymongo
from pymongo import MongoClient
import time
from datetime import datetime
import math


def printTable(table: collection):
    l = table.find()
    final_res = []
    for i in l:
        res = ""
        for j in i.keys():
            if j == "_id":
                continue
            if type(i[j]) == DBRef:
                t: DBRef = i[j]
                divider = str(t).split(',')
                res += str(j) + ":" + " " + divider[1][0:len(divider[1]) - 1] + "  "
            else:
                res += str(j) + ":" + " " + str(i[j])
        final_res.append(res)
    print("\n˜”*°•.˜”*°•ღ  " + t.collection + "  ˜”*°•.˜”*°•ღ \n")

    for i in final_res:
        print(i)


# Get method
def get_employee(db, employee):
    result = db.Employees.find_one({"employee_id": employee})['employee_id']
    return result


def createEmployees():
    db.Employees.drop()
    employee: collection = db.Employees
    employee.create_index([("employee_id", pymongo.ASCENDING)], unique=True)
    result = employee.insert_many([
        {"employee_id": 184749820, "employee_name": "Mark Scott"},
        {"employee_id": 123456789, "employee_name": "John Smith"},
        {"employee_id": 6394620, "employee_name": "Hank Flores"},
        {"employee_id": 164826292, "employee_name": "Debora Hilga"},
        {"employee_id": 134823831, "employee_name": "Marhajai Shrah"},
        {"employee_id": 194792011, "employee_name": "Jose Martinez"},
    ])
    return employee


# GET METHOD
def get_building(db, building):
    i = db.Buildings.find_one({"building_name": building})['building_name']
    return i


def createBuildings():
    db.Buildings.drop()
    building: collection = db.Buildings

    building.create_index([("building_name", pymongo.ASCENDING)], unique=True)
    building.insert_many([
        {"building_name": "ECS"},
        {"building_name": "VEC"},
        {"building_name": "ENG1"},
        {"building_name": "ENG2"},
        {"building_name": "ENG3"},
    ])
    return building


# GET METHOD
def get_room(db):
    res = []
    result = db.Rooms.find()
    for i in result:
        res.append((i['room_num'], i['building_name']))
    return res


def createRooms():
    db.Rooms.drop()
    room: collection = db.Rooms

    room_validator = {
        'validator': {
            '$jsonSchema': {

                'bsonType': "object",
                'description': "space in building",
                'required': ["building_name", "room_num"],
                'additionalProperties': False,
                'properties': {

                    '_id': {},
                    'building_name': {
                        'bsonType': "DBRef",
                        "description": "building where room is located"
                    },
                    'room_num': {

                        'bsonType': "number",
                        "description": "room number",
                    }
                }
            }
        }
    }

    room.create_index([("building_name", pymongo.ASCENDING), ("room_num", pymongo.ASCENDING)], unique=True)
    buildingList = []
    building = db.Buildings
    for i in building.find():
        buildingList.append(i["building_name"])

    for i in buildingList:
        room.insert_many([
            {"building_name": DBRef("Buildings", i), "room_num": random.randint(100, 300)},
            {"building_name": DBRef("Buildings", i), "room_num": random.randint(300, 450)},
            {"building_name": DBRef("Buildings", i), "room_num": random.randint(450, 550)},
        ])
    return room


# GET METHOD
def get_doortype(db):
    res = []
    doors = db.DoorTypes.find()
    for i in doors:
        res.append(i['door_type'])
    return res


def createDoorTypes():
    db.DoorTypes.drop()
    doortype: collection = db.DoorTypes
    doortype.create_index([("door_type", pymongo.ASCENDING)], unique=True)
    result = doortype.insert_many([
        {"door_type": "Front-Class"},
        {"door_type": "Back-Class"},
        {"door_type": "Front-Building"},
        {"door_type": "Back-Building"},
        {"door_type": "Side(L)-Building"},
        {"door_type": "Side(R)-Building"},
    ])

    return doortype


# GET METHOD
def get_random_hook(db):
    res = []
    # putting all of the hooks inot one List
    hooksList = db.Hooks.find()
    for i in hooksList: res.append(i["hook_id"])
    # returns the int value of the chosen random hook
    return res[random.randint(0, len(res) - 1)]


def get_hook(db, hook):
    res = db.Hooks.find_one({"hook_id": hook})['hook_id']
    return res


def createHooks():
    db.Hooks.drop()
    hook: collection = db.Hooks
    hook.create_index([("hook_id", pymongo.ASCENDING)], unique=True)

    result = hook.insert_many([
        {"hook_id": 2919},
        {"hook_id": 1212},
        {"hook_id": 3729},
        {"hook_id": 47291},
        {"hook_id": 7592},
        {"hook_id": 5932},
    ])

    return hook


def get_door(db):
    res = []
    doors = db.Doors.find()
    for i in doors: res.append((i['door_type'], i['room_num'], i['building_name']))
    return res


def createDoors():
    db.Doors.drop()
    door: collection = db.Doors
    door.create_index([("door_type", pymongo.ASCENDING),
                       ("room_num", pymongo.ASCENDING),
                       ("building_name", pymongo.ASCENDING)], unique=True)
    doortypeString = get_doortype(db)
    roomTuples = get_room(db)
    for room in roomTuples:
        randoms = random.sample(range(0, len(doortypeString)), 2)

        for i in range(2):
            result = door.insert_many([
                {"door_type": DBRef("DoorTypes", doortypeString[randoms[i]]),
                 "room_num": DBRef("Rooms", room[0]),
                 "building_name": room[1]}
            ])

    return door


def createHookLines():
    db.HookLines.drop()
    hookline: collection = db.HookLines
    hookline.create_index([("door_type", pymongo.ASCENDING),
                           ("hook_id", pymongo.ASCENDING),
                           ("room_num", pymongo.ASCENDING),
                           ("building_name", pymongo.ASCENDING)], unique=True)
    doorsList = get_door(db)
    for d in doorsList:
        hooknum = (get_random_hook(db))
        result = hookline.insert_many(
            [{"room_num": d[0], "building_name": d[1], "door_type": d[2], "hook_id": DBRef("Hooks", hooknum)}])
    return hookline


# GET METHOD
def get_copyKey(db, copykey):
    res = db.Keys.find_one({"key_id": copykey})['key_id']
    return res


def createCopyKeys():
    db.CopyKeys.drop()
    copykey: collection = db.CopyKeys
    result = copykey.insert_many([
        {"key_id": DBRef("hooks", get_hook(db, 2919))},
        {"key_id": DBRef("hooks", get_hook(db, 1212))},
        {"key_id": DBRef("hooks", get_hook(db, 3729))},
        {"key_id": DBRef("hooks", get_hook(db, 47291))},
        {"key_id": DBRef("hooks", get_hook(db, 7592))},
        {"key_id": DBRef("hooks", get_hook(db, 5932))},
    ])

    return copykey


# WORK IN PROGRESS
# need copy_key_id
def get_keyrequest(db, keyrequest):
    result = db.KeyRequests.find_one({"request_id": keyrequest})['request_id']
    return result


def createKeyRequests():
    db.KeyRequests.drop()
    keyrequest: collection = db.KeyRequests
    # validator
    key_request_validator = {
        'validator': {
            '$jsonSchema': {

                'bsonType': "object",
                'description': "check to see it room exist to give key?",
                'required': ["request_id", "room_num", "building_name", "employee_id", "request_date", "key_id",
                             "issued_date", "issued_time"],
                'additionalProperties': False,
                'properties': {
                    'request_id': {
                        'bsonType': "number",
                        "description": "request id"
                    },
                    'building_name': {
                        'bsonType': "DBRef",
                        "description": "building where room is located"
                    },
                    'room_num': {
                        'bsonType': "DBRef",
                        "description": "room number"
                    },
                    'employee_id': {
                        'bsonType': "DBRef",
                        "description": "employee id"
                    },
                    'key_id': {
                        'bsonType': "DBRef",
                        "description": "copy key id"
                    },
                    "issued_date": {
                        'bsonType': "datetime",
                        "description": "issued date"
                    },
                    "issued_time": {
                        'bsonType': "datetime",
                        "description": "issued time"
                    }

                }
            }
        }
    }

    keyrequest.create_index([("request_id", pymongo.ASCENDING)], unique=True)
    result = keyrequest.insert_many([
        {"request_id": 101,
         "room_num": 308,
         "building_name": "ECS",
         "employee_id": DBRef("Employees", get_employee(db, 123456789)),
         "key_id": 1234,
         "request_date": datetime(2022, 11, 30, 22, 0, 0),
         "issued_date": datetime(2022, 12, 8, 14, 30, 0),
         "issued_time": datetime(2022, 12, 8, 14, 30, 0)}
    ])
    return keyrequest


# WORK IN PROGRESS
def createReturns():
    db.Returns.drop()
    returns: collection = db.Returns
    returns.create_index([("request_id", pymongo.ASCENDING)], unique=True)
    result = returns.insert_many([
        {"return_date": datetime(2022, 12, 9, 22, 30, 1),
         "request_id": db.KeyRequests.find_one({"request_id": 101})['request_id'],
         "issued_date": db.KeyRequests.find_one({"request_id": 101})['issued_date'],
         "issued_time": db.KeyRequests.find_one({"request_id": 101})['issued_time']}
    ])
    return returns


# WORK IN PROGRESS
def createLoss():
    db.Loss.drop()
    loss: collection = db.Loss
    loss.create_index([("request_id", pymongo.ASCENDING)], unique=True)
    result = loss.insert_many([
        {"loss_date": datetime(2022, 12, 9, 22, 30, 1),
         "request_id": db.KeyRequests.find_one({"request_id": 101})['request_id'],
         "issued_date": db.KeyRequests.find_one({"request_id": 101})['issued_date'],
         "issued_time": db.KeyRequests.find_one({"request_id": 101})['issued_time']}
    ])
    return loss


def createTables():
    buildings = createBuildings()
    rooms = createRooms()
    employees = createEmployees()
    doortypes = createDoorTypes()
    hooks = createHooks()
    doors = createDoors()
    copykeys = createCopyKeys()
    keyrequests = createKeyRequests()
    returns = createReturns()
    loss = createLoss()
    hooklines = createHookLines()

    return buildings, rooms, employees, doortypes, doors, hooks, copykeys, keyrequests, returns, loss, hooklines


def menu():
    print("\n✧･ﾟ: *✧･ﾟ:* 【 ｍｅｎｕ 】 *:･ﾟ✧*:･ﾟ✧")
    userInput = -math.inf
    while userInput != 0:
        print("0. exit")
        print("1. Display Tables")
        print("2. Create New Key ")
        print("3. Request access to a given room by a given employee ")
        print("4. Capture the issue of a key to an employee ")
        print("5. Issue a Key ")
        print("6. Capture losing a key ")
        print("7. Report out all the rooms that an employee can enter, given the keys that he/she already has.")
        print("8. Delete a key. ")
        print("9. Delete an employee. ")
        print("10. Add a new door that can be opened by an existing hook.")
        print("11. Update an access request to move it to a new employee. ")
        print("12. Report out all the employees who can get into a room. ")
        userInput = int(input("Please choose an option "))
        if userInput == 0:
            break
        elif userInput == 1:
            printTable(rooms)
        else:
            print("Invalid Input")
            menu()
            break


# setup and connection to db
if __name__ == "__main__":
    client = MongoClient(
        "mongodb+srv://Group7:Group7@keyhooksphase3.mcuiog0.mongodb.net/keyhooksphase3?tlsAllowInvalidCertificates=true")
    db = client.KeyHookPhase3
    buildings, rooms, employees, doortypes, doors, hooks, copykeys, keyrequests, returns, loss, hooklines = createTables()
    input = menu()
    if input == 2:
        # db.Keys.insert_one(
        #     {
        #         "door_id": door_id,
        #         "employee_id": employee_id,
        #         "lost": false
        #     }
        # )
    elif input == 3:
        # db.AccessRequests.insert_one(
        #     {
        #         "room_id": room_id,
        #         "employee_id": employee_id,
        #         "status": "pending"
        #     }
        # )
    elif input == 4:
        # Capture the issue of a key to an employee
        # db.Keys.insert_one(
        #     {
        #         "door_id": door_id,
        #         "employee_id": employee_id
        #     }
        # )
    elif input == 5:
        # db.Keys.insert_one(
        #     {
        #         "door_id": door_id,
        #         "employee_id": employee_id,
        #         "lost": false
        #     }
        # )
    elif input == 6:
        # Capture losing a key
        # db.Keys.update_one(
        #     # Filter to find the key that was lost
        #     {"_id": key_id},
        #     # Use $set to update the lost field
        #     {"$set": {"lost": true}}
        # )
    elif input == 7:
        # Get all rooms
        # rooms = db.Rooms.find()
        #
        # # Get all keys that the employee has
        # keys = db.Keys.find({"employee_id": employee_id})
        #
        # # Iterate over rooms and keys
        # for room in rooms:
        #     for key in keys:
        #         # Check if the employee has a key that can open the room
        #         if key["door_id"] == room["door_id"]:
        #             print("Employee can access room " + room["room_num"])
    elif input == 8:

    elif input == 9:
        # db.Employees.delete_one(
        #     # Filter to match the employee you want to delete
        #     {"employee_id": employee_id}
        # )
    elif input == 10:
        # db.Doors.insert_one(
        #     {
        #         "door_name": "New Door",
        #         "hook_id": existing_hook_id
        #     }
        # )
    elif input == 11:
        # db.AccessRequests.update_one(
        #     # Filter to find the access request you want to move
        #     {"_id": access_request_id},
        #     # Use $set to update the employee_id field
        #     {"$set": {"employee_id": new_employee_id}}
        # )
    elif input == 12:
        # # Get all rooms
        # rooms = db.Rooms.find()
        #
        # # Get all employees
        # employees = db.Employees.find()
        #
        # # Iterate over rooms and employees
        # for room in rooms:
        #     for employee in employees:
        #         # Check if employee has access to room
        #         if employee["access_level"] >= room["access_level_required"]:
        #             print(employee["name"] + " can access room " + room["room_num"])
    print("˜”*°•.˜”*°•ღ  Exiting...  ღ˜”*°•.˜”*°•")
    exit()
