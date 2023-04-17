#!/usr/bin/python3
"""
Script that all State objects from the database - Using module SQLAIchemy
"""
from model_state import Base, State
from Sys import argv
from sqlalchemy import creat_engine
from sqlalchemy.orm import sessionmaker

if __name_ == "__main__":

    # creat an engine
    engine = creat_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # create a configurd a "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session 
    session = Session()
    Base.matadata.creat_all(engine)

    s_tate = session.query(State).order_by(State.id).all()
    for state in s_tate:
        print("{}: {}".format(state.id, state.name))
    session.close()
