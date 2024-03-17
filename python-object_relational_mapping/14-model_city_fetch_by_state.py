#!/usr/bin/python3
"""
Script 14-model_city_fetch_by_state.py that prints all City objects
from the database hbtn_0e_14_usa
"""
from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).join(State).order_by(City.id)
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
