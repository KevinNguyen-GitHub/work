"""This "application" is a demonstration using SQLAlchemy to create a small number of tables and populate
them.  Not evey possible use case for SQLAlchemy is explored in this demonstration, only those which are
required for this particular demonstration.

Technical Note: Be sure to have psycopg2 or whichever package you need to support whichever
relational dialect that you are using installed.  No imports call attention to the database
connectivity library, that is referenced when you run your entine."""

# Think of Session and engine like global variables.  A little ghetto, but the only
# other alternative would have been a singleton design pattern.

# the db_connection.py code sets up some connection objects for us, almost like Java class variables
# that get loaded up at run time.  This statement builds the Session class and the engine object
# that we will use for interacting with the database.
from db_connection import Session, engine
# orm_base defines the Base class on which we build all of our Python classes and in so doing,
# stipulates that the schema that we're using is 'demo'.  Once that's established, any class
# that uses Base as its supertype will show up in the postgres.demo schema.
from orm_base import metadata
import logging
from sqlalchemy import Column, String, Integer, Float, UniqueConstraint, \
    Identity, ForeignKey, distinct, bindparam
from sqlalchemy.orm import relationship, backref
from orm_base import Base

from Employee import Employee
from KeyRequest import KeyRequest
from DoorType import DoorType
from Door import Door
from Room import Room
from Building import Building
from CopyKey import CopyKey
from Hook import Hook
from HookLine import HookLine
from Return import Return
from Loss import Loss

if __name__ == '__main__':
    logging.basicConfig()
    # use the logging factory to create our first logger.
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    # use the logging factory to create our second logger.
    logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)

    metadata.drop_all(bind=engine)  # start with a clean slate while in development

    # Create whatever tables are called for by our "Entity" classes.  The simple fact that
    # your classes that are subtypes of Base have been loaded by Python has populated
    # the metadata object with their definition.  So now we tell SQLAlchemy to create
    # those tables for us.
    metadata.create_all(bind=engine)

    #set 1
    e1: Employee = Employee(name="Kevin", id=1)
    kr1: KeyRequest = KeyRequest(request_id=1, request_date='2022-01-31', employee_id=1, room_number=243,
                                 room_buildings_name='ECS', copy_key_id=1, copy_key_is_loss=True)
    b1: Building = Building(name="ECS")
    r1: Room = Room(num=243, building_name='ECS')
    d1: Door = Door(door_type_name='Front-Class', room_num=243, room_building_name='ECS')
    dt1: DoorType = DoorType(name='Front-Class')
    hl1: HookLine = HookLine(doors_door_type_name='Front-Class', doors_roon_num=243, doors_rooms_buildings_name='ECS',
                             hooks_id = 1)
    h1: Hook = Hook(id=1)


    # Do our database work within a context.  This makes sure that the session gets closed
    # at the end of the with, much like what it would be like if you used a with to open a file.
    # This way, we do not have memory leaks.
    with Session() as sess:
        sess.begin()
        print("Inside the session...")
        sess.add(e1)
        sess.add(kr1)
        sess.add(b1)
        sess.add(r1)
        sess.add(d1)
        sess.add(dt1)
        sess.add(hl1)
        sess.add(h1)
        sess.commit()

    print("Exiting normally.")


