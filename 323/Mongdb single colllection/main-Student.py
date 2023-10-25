import pymongo
from pymongo import MongoClient
from pprint import pprint
import getpass
from menu_definitions import menu_main
from menu_definitions import add_menu
from menu_definitions import delete_menu
from menu_definitions import list_menu

# Define your MongoDB connection string
connection_string = "mongodb+srv://nguyenkevin828:Password@cecs-323-spring-2023.qhst2lw.mongodb.net/?retryWrites=true&w=majority"

# Use the connection string to connect to MongoDB
client = MongoClient(connection_string)

# Use your desired database name
db = client["Demonstration"]

def add(db):
    """
    Present the add menu and execute the user's selection.
    :param db:  The connection to the current database.
    :return:    None
    """
    add_action: str = ''
    while add_action != add_menu.last_action():
        add_action = add_menu.menu_prompt()
        exec(add_action)


def delete(db):
    """
    Present the delete menu and execute the user's selection.
    :param db:  The connection to the current database.
    :return:    None
    """
    delete_action: str = ''
    while delete_action != delete_menu.last_action():
        delete_action = delete_menu.menu_prompt()
        exec(delete_action)


def list_objects(db):
    """
    Present the list menu and execute the user's selection.
    :param db:  The connection to the current database.
    :return:    None
    """
    list_action: str = ''
    while list_action != list_menu.last_action():
        list_action = list_menu.menu_prompt()
        exec(list_action)


def add_student(db):
    """
    Add a new student, making sure that we don't put in any duplicates,
    based on all the candidate keys (AKA unique indexes) on the
    students collection.  Theoretically, we could query MongoDB to find
    the uniqueness constraints in place, and use that information to
    dynamically decide what searches we need to do to make sure that
    we don't violate any of the uniqueness constraints.  Extra credit anyone?
    :param collection:  The pointer to the students collection.
    :return:            None
    """
    # Create a "pointer" to the students collection within the db database.
    collection = db["students"]
    unique_name: bool = False
    unique_email: bool = False
    lastName: str = ''
    firstName: str = ''
    email: str = ''
    while not unique_name or not unique_email:
        lastName = input("Student last name--> ")
        firstName = input("Student first name--> ")
        email = input("Student e-mail address--> ")
        name_count: int = collection.count_documents({"last_name": lastName, "first_name": firstName})
        unique_name = name_count == 0
        if not unique_name:
            print("We already have a student by that name.  Try again.")
        if unique_name:
            email_count = collection.count_documents({"e_mail": email})
            unique_email = email_count == 0
            if not unique_email:
                print("We already have a student with that e-mail address.  Try again.")
    # Build a new students document preparatory to storing it
    student = {
        "last_name": lastName,
        "first_name": firstName,
        "e_mail": email
    }
    results = collection.insert_one(student)
    

def select_student(db):
    """
    Select a student by the combination of the last and first.
    :param db:      The connection to the database.
    :return:        The selected student as a dict.  This is not the same as it was
                    in SQLAlchemy, it is just a copy of the Student document from 
                    the database.
    """
    # Create a connection to the students collection from this database
    collection = db["students"]
    found: bool = False
    lastName: str = ''
    firstName: str = ''
    while not found:
        lastName = input("Student's last name--> ")
        firstName = input("Student's first name--> ")
        name_count: int = collection.count_documents({"last_name": lastName, "first_name": firstName})
        found = name_count == 1
        if not found:
            print("No student found by that name.  Try again.")
    found_student = collection.find_one({"last_name": lastName, "first_name": firstName})
    return found_student


def delete_student(db):
    """
    Delete a student from the database.
    :param db:  The current database connection.
    :return:    None
    """
    # student isn't a Student object (we have no such thing in this application)
    # rather it's a dict with all the content of the selected student, including
    # the MongoDB-supplied _id column which is a built-in surrogate.
    student = select_student(db)
    # Create a "pointer" to the students collection within the db database.
    students = db["students"]
    # student["_id"] returns the _id value from the selected student document.
    deleted = students.delete_one({"_id": student["_id"]})
    # The deleted variable is a document that tells us, among other things, how
    # many documents we deleted.
    print(f"We just deleted: {deleted.deleted_count} students.")


def list_student(db):
    """
    List all of the students, sorted by last name first, then the first name.
    :param db:  The current connection to the MongoDB database.
    :return:    None
    """
    # No real point in creating a pointer to the collection, I'm only using it
    # once in here.  The {} inside the find simply tells the find that I have
    # no criteria.  Essentially this is analogous to a SQL find * from students.
    # Each tuple in the sort specification has the name of the field, followed
    # by the specification of ascending versus descending.
    students = db["students"].find({}).sort([("last_name", pymongo.ASCENDING),
                                             ("first_name", pymongo.ASCENDING)])
    # pretty print is good enough for this work.  It doesn't have to win a beauty contest.
    for student in students:
        pprint(student)


def add_department(db):
    # Function to add a new department
    print("Add a New Department")

    while True:
        name = input("Department Name: ")
        if len(name) <= 50:
            # Check if the department with the same name already exists
            if db.departments.find_one({"name": name}):
                print(f"Department '{name}' already exists. Please enter a different name.")
            else:
                break
        else:
            print("Department Name must be 50 characters or less.")

    while True:
        abbreviation = input("Abbreviation: ")
        if len(abbreviation) <= 6:
            # Check if a department with the same abbreviation already exists
            if db.departments.find_one({"abbreviation": abbreviation}):
                print(f"Department with abbreviation '{abbreviation}' already exists. Please enter a different abbreviation.")
            else:
                break
        else:
            print("Abbreviation must be 6 characters or less.")

    while True:
        chair_name = input("Chair Name: ")
        if len(chair_name) <= 80:
            break
        else:
            print("Chair Name must be 80 characters or less.")

    while True:
        building = input("Building: ")
        if len(building) <= 10:
            break
        else:
            print("Building must be 10 characters or less.")

    while True:
        try:
            office = int(input("Office: "))
            if 1 <= office <= 1000:  # Adjust the range as needed
                # Check if a department with the same building and office already exists
                if db.departments.find_one({"building": building, "office": office}):
                    print(f"Another department already occupies the same room. Please enter a different office.")
                else:
                    break
            else:
                print("Office must be between 1 and 1000.")
        except ValueError:
            print("Please enter a valid integer for the office.")

    while True:
        description = input("Description: ")
        if len(description) <= 80:
            # Check if a department with the same description already exists
            if db.departments.find_one({"description": description}):
                print(f"Department with the same description already exists. Please enter a different description.")
            else:
                break
        else:
            print("Description must be 80 characters or less.")

    # Create a department document
    department = {
        "name": name,
        "abbreviation": abbreviation,
        "chair_name": chair_name,
        "building": building,
        "office": office,
        "description": description
    }

    # Insert the new department into the MongoDB collection
    db.departments.insert_one(department)
    print("Department added successfully.")


def delete_department(db):
    # Function to delete a department
    print("Delete a Department")
    list_department(db)  # List available departments

    name = input("Enter the name of the department to delete: ")

    # Check if the department exists
    department = db.departments.find_one({"name": name})
    if department:
        # Delete the department
        db.departments.delete_one({"name": name})
        print("Department deleted successfully.")
    else:
        print(f"Department '{name}' not found.")


def list_department(db):
    # Function to list all departments
    print("List of Departments")
    departments = db.departments.find().sort("name")

    for department in departments:
        print(department)

def boilerplate(db):
    preload_departments = [
        {
            "name": "Computer Science",
            "abbreviation": "CS",
            "chair_name": "John Smith",
            "building": "Building A",
            "office": 101,
            "description": "Computer Science Department",
        },
        {
            "name": "Biology",
            "abbreviation": "BIO",
            "chair_name": "Sarah Johnson",
            "building": "Building B",
            "office": 201,
            "description": "Biology Department",
        },
        {
            "name": "Physics",
            "abbreviation": "PHY",
            "chair_name": "Robert Davis",
            "building": "Building C",
            "office": 301,
            "description": "Physics Department",
        },
    ]

    # Insert the preloaded departments into the MongoDB collection
    db.departments.insert_many(preload_departments)

if __name__ == '__main__':
    main_action: str = ''
    while main_action != menu_main.last_action():
        main_action = menu_main.menu_prompt()
        print('next action: ', main_action)
        exec(main_action)

