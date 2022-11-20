import datetime
from db_connection import Session, engine
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

    def intro():
        print("Are you here to request a key?")
        print("0. View")
        print("1. Make A Request")
        print("2. Exit\n")





    # Do our database work within a context.  This makes sure that the session gets closed
    # at the end of the with, much like what it would be like if you used a with to open a file.
    # This way, we do not have memory leaks.
    with Session() as sess:
        sess.begin()

        #insert building
        b1: Building = Building("ECS")
        b2: Building = Building("Library")
        b3: Building = Building("VEC")
        b4: Building = Building("HC")
        b5: Building = Building("ET")
        b6: Building = Building("Rec")
        sess.add(b1)
        sess.add(b2)
        sess.add(b3)
        sess.add(b4)
        sess.add(b5)
        sess.add(b6)
        sess.commit()

        #insert rooms
        r1: Room = Room(100, b1)
        r2: Room = Room(101, b2)
        r3: Room = Room(102, b3)
        r4: Room = Room(103, b4)
        r5: Room = Room(104, b5)
        r6: Room = Room(105, b6)
        sess.add(r1)
        sess.add(r2)
        sess.add(r3)
        sess.add(r4)
        sess.add(r5)
        sess.add(r6)
        sess.commit()

        #insert doors types
        dt1: DoorType = DoorType("Front")
        dt2: DoorType = DoorType("Back")
        dt3: DoorType = DoorType("West")
        dt4: DoorType = DoorType("East")
        dt5: DoorType = DoorType("North-East")
        dt6: DoorType = DoorType("South-East")
        sess.add(dt1)
        sess.add(dt2)
        sess.add(dt3)
        sess.add(dt4)
        sess.add(dt5)
        sess.add(dt6)
        sess.commit()

        #insert door
        d1: Door = Door(dt1, r1)
        d2: Door = Door(dt2, r2)
        d3: Door = Door(dt3, r3)
        d4: Door = Door(dt4, r4)
        d5: Door = Door(dt1, r5)
        d6: Door = Door(dt3, r6)
        sess.add(d1)
        sess.add(d2)
        sess.add(d3)
        sess.add(d4)
        sess.add(d5)
        sess.add(d6)
        sess.commit()

        #create hook
        h1: Hook = Hook()
        h2: Hook = Hook()
        h3: Hook = Hook()
        h4: Hook = Hook()
        h5: Hook = Hook()
        h6: Hook = Hook()
        sess.add(h1)
        sess.add(h2)
        sess.add(h3)
        sess.add(h4)
        sess.add(h5)
        sess.add(h6)
        sess.commit()

        #add doors
        h1.add_door(d1)
        h2.add_door(d2)
        h3.add_door(d3)
        h4.add_door(d4)
        h5.add_door(d5)
        h6.add_door(d6)
        sess.commit()

        #create employees
        e1: Employee = Employee("Kevin", 1)
        e2: Employee = Employee("Bob", 2)
        e3: Employee = Employee("Ivy", 3)
        e4: Employee = Employee("Erika", 4)
        e5: Employee = Employee("Carina", 5)
        e6: Employee = Employee("John", 6)
        sess.add(e1)
        sess.add(e2)
        sess.add(e3)
        sess.add(e4)
        sess.add(e5)
        sess.add(e6)
        sess.commit()

        #create key request
        rq1: KeyRequest = KeyRequest(e1, r1, k1)
        rq2: KeyRequest = KeyRequest(e2, r5, k2)
        rq3: KeyRequest = KeyRequest(e3, r3, k4)
        rq4: KeyRequest = KeyRequest(e4, r2, k6)
        rq5: KeyRequest = KeyRequest(e5, r4, k5)
        rq6: KeyRequest = KeyRequest(e6, r6, k3)
        sess.add(rq1)
        sess.add(rq2)
        sess.add(rq3)
        sess.add(rq4)
        sess.add(rq5)
        sess.add(rq6)
        sess.commit()

        #create loss key
        loss1: Loss = Loss(rq1, datetime.datetime(2022, 3, 24))
        loss2: Loss = Loss(rq5, datetime.datetime(2022, 6, 1))
        loss3: Loss = Loss(rq2, datetime.datetime(2022, 1, 25))
        loss4: Loss = Loss(rq4, datetime.datetime(2012, 8, 10))
        loss5: Loss = Loss(rq2, datetime.datetime(2022, 5, 11))
        loss6: Loss = Loss(rq1, datetime.datetime(2022, 2, 18))
        loss7: Loss = Loss(rq5, datetime.datetime(2022, 12, 29))
        sess.add(loss1)
        sess.add(loss2)
        sess.add(loss3)
        sess.add(loss4)
        sess.add(loss5)
        sess.add(loss6)
        sess.add(loss7)
        sess.commit()

        #create return key
        rt1: Return = Return(rq1, datetime.datetime(2022, 1, 5))
        rt2: Return = Return(rq3, datetime.datetime(2022, 2, 10))
        rt3: Return = Return(rq2, datetime.datetime(2022, 3, 15))
        rt4: Return = Return(rq1, datetime.datetime(2022, 4, 20))
        rt5: Return = Return(rq6, datetime.datetime(2022, 5, 25))
        rt6: Return = Return(rq5, datetime.datetime(2022, 6, 21))
        rt7: Return = Return(rq6, datetime.datetime(2022, 7, 15))
        sess.add(rt1)
        sess.add(rt2)
        sess.add(rt3)
        sess.add(rt4)
        sess.add(rt5)
        sess.add(rt6)
        sess.add(rt7)
        sess.commit()

    # active = False
    # While not active:
    #     try:
    #         intro()
    #         choice = int(input())
    #         if choice >= 0 and choice <= 2:
    #             active = True
    #         else:
    #             print("Invalid range, please choose a number 0-2")
    #     except ValueError:
    #         print("Invalid input, please enter a number 0-2")
    #
    #     if choice == 2:
    #         print("Thank you for using our services.")
    #         exit()
    #     active = False
    #
    #     with Session() as sess:
    #         if choice == 0:
    #
    #         elif choice == 1: