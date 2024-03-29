#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter
a from the database hbtn_0e_6_usa.
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states_with_a = session.query(State).filter(State.name.like("%a%"))
    for state in states_with_a:
        session.delete(state)
    session.commit()
