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
            if j == "_id": continue
            if type(i[j]) == DBRef:
                res += str(j) + ":" + " " + str(i[j].id) + "  "
            else:
                res += str(j) + ":" + " " + str(i[j])
        final_res.append(res)

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


def deleteEmployee(id):
    userInput = id
    print(db.Employees.find_one({"employee_id": userInput}))
    if db.Employees.find_one({"employee_id": userInput}) == None:
        print("Sorry, could not find that employee.")
    else:
        if db.CopyKey.find_one({"key_id": userInput}) == None:
            db.Employees.delete_one({"employee_id": userInput})
            print("Employee succesfully deleted!")
            printTable(Employees)
        else:
            print('Sorry, employee still has access to rooms and cannot be deleted.')


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
    # putting all of the hooks into one List
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
    copykey.create_index([("key_id", pymongo.ASCENDING),
                          ("hook_id", pymongo.ASCENDING)], unique=True)
    copykey.create_index([("is_lost", pymongo.ASCENDING)])
    result = copykey.insert_many([
        {"key_id": 3452, "hook_id": DBRef("hooks", get_hook(db, 2919), ), "is_lost": False},
        {"key_id": 2343, "hook_id": DBRef("hooks", get_hook(db, 1212)), "is_lost": False}

    ])

    return copykey


def employeeCreateKey(i):
    userInput = i
    if db.Hooks.find_one({"hook_id": userInput}) == None:
        print("sorry, couldnt find that hook")
    else:
        db.CopyKeys.insert_many(
            [{"key_id": random.randint(1000, 9999), "hook_id": DBRef("hooks", userInput), "is_lost": False}])
        print("success!")
        print("new key added to table!")
        printTable(copykeys)


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


def delete_key(i):
    userInput = i
    print(db.CopyKeys.find_one({"key_id": userInput}))
    if db.CopyKeys.find_one({"key_id": userInput}) == None:
        print("sorry, could not find that key")
    else:
        if db.Employees.find_one({"key_id": userInput}) == None:
            db.CopyKeys.delete_one({"key_id": userInput})
            print("key succesfully deleted!")
            printTable(copykeys)
        else:
            print('sorry, key is in use and could not be deleted')


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


# someone test please
def roomAccess(room):
    employees = db.Employees.find({"rooms": room["room_num"]})
    for employee in employees:
        print(employee["name"])


def menu():
    print("\n✧･ﾟ: *✧･ﾟ:* 【 ｍｅｎｕ 】 *:･ﾟ✧*:･ﾟ✧")
    userInput = -math.inf
    while userInput != 0:
        print("0. exit")
        print("1. Display Tables")
        print("2. Create New Key ")
        print("3. NW Request access to a given room by a given employee ")
        print("4. NW Capture the issue of a key to an employee ")
        print("5. NW Issue a Key ")
        print("6. NW Capture losing a key ")
        print("7. NW Report out all the rooms that an employee can enter, given the keys that he/she already has.")
        print("8. NW Delete a key. ")
        print("9. NW Delete an employee. ")
        print("10. NW Add a new door that can be opened by an existing hook.")
        print("11. NW Update an access request to move it to a new employee. ")
        print("12. NW Report out all the employees who can get into a room. ")
        userInput = int(input("Please choose an option "))
        if userInput == 0:
            break

        elif userInput == 1:
            print("BUILDINGS")
            printTable(buildings)
            print("ROOMS")
            printTable(rooms)
            print("DOORS")
            printTable(doors)
            print("DOOR TYPES")
            printTable(doortypes)
            print("HOOKS")
            printTable(hooks)
            print("COPY KEYS")
            printTable(copykeys)
            print("HOOKLINE")
            printTable(hooklines)
            print("EMPLOYEES")
            printTable(employees)
            print("KEY REQUESTS")
            printTable(keyrequests)
            print("RETURNS")
            printTable(returns)
            print("LOSS")
            printTable(loss)


        elif userInput == 2:
            print("you selected: Create a new Key")
            print("here are your options")
            printTable(hooks)
            try:
                i = int(input("Please input Hook ID that you want a key of:"))
                employeeCreateKey(i)
            except:
                print("an expection has occured, try again")


        elif userInput == 3:
            print("you selected: Request access to a given room by a given employee")
            print("here are your options")
            printTable(employees)


        elif userInput == 4:
            print("you selected: Capture the issue of a key to an employee")
            print("here are your options")
            printTable(employees)

        elif userInput == 5:
            print("you selected: Issue a Key")
            print("here are your options")
            printTable(employees)

        elif userInput == 6:
            print("you selected: Capture losing a key ")
            print("here are your options")
            printTable(employees)

        elif userInput == 7:
            print(
                "you selected: Report out all the rooms that an employee can enter, given the keys that he/she already has.")
            print("here are your options")
            printTable(employees)
            employee = input(int("Enter employee ID: "))
            printTable(Rooms)
            room = input(int("Enter room number: "))

        elif userInput == 8:
            print("you selected: Delete a key")
            print("here are your options")
            printTable(copykeys)
            try:
                i = int(input("Please input the key id of the one you would like to delete:"))
                delete_key(i)
            except:
                print("an expection has occured, try again")



        elif userInput == 9:

            print('You selected: Delete an employee')
            print("here are your options")
            printTable(employees)
            try:
                id = int(input("Please input the employee id of the one you would like to delete:"))
                deleteEmployee(id)
            except:
                print("an expection has occured, try again")


        elif userInput == 10:
            print("you selected: Add a new door that can be opened by an existing hook.")
            print("here are your options")

            printTable(employees)
        elif userInput == 11:
            print("you selected: Update an access request to move it to a new employee.")
            print("here are your options")
            printTable(employees)

        elif userInput == 12:
            print("you selected: Report out all the employees who can get into a room.")
            print("here are your options")
            printTable(rooms)
            number = int(input("Room number: "))
            room = db.rooms.find_one({"number": number})
            if number not in room:
                print("Invalid Number. Please choose again")
                number = int(input("Room number: "))
            else:
                print("here")

        else:
            print("Invalid Selection. Please try again.")
            menu()
            break


# setup and connection to db
if __name__ == "__main__":
    client = MongoClient(
        "mongodb+srv://Group7:Group7@keyhooksphase3.mcuiog0.mongodb.net/keyhooksphase3?tlsAllowInvalidCertificates=true")
    db = client.KeyHookPhase3
    buildings, rooms, employees, doortypes, doors, hooks, copykeys, keyrequests, returns, loss, hooklines = createTables()
    menu()
    print("˜”*°•.˜”*°•ღ  Exiting...  ღ˜”*°•.˜”*°•")
    exit()
